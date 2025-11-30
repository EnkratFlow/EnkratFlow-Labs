#!/usr/bin/env python3
"""
Command-line interface for MindOS RAG System
"""

import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from ingestors.obsidian import ObsidianIngestor
from ingestors.notion import NotionIngestor
from ingestors.github import GitHubIngestor
from chunking.semantic_chunker import SemanticChunker
from retrieval.vector_store import VectorStore
from llm.chat import RAGChat
import yaml


def load_config():
    """Load configuration from config.yaml"""
    config_path = Path(__file__).parent.parent / 'config' / 'config.yaml'
    if config_path.exists():
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    return {}


def index_command(args):
    """Index documents from data sources."""
    print("🚀 Starting indexing process...")
    
    config = load_config()
    sources_config = config.get('sources', {})
    
    # Initialize vector store
    db_path = os.getenv('CHROMA_DB_PATH', './chroma_db')
    vector_store = VectorStore(db_path=db_path)
    
    all_chunks = []
    
    # Index Obsidian if enabled
    if sources_config.get('obsidian', {}).get('enabled', True):
        print("\n📚 Indexing Obsidian vault...")
        vault_path = sources_config.get('obsidian', {}).get('vault_path') or os.getenv('OBSIDIAN_VAULT_PATH')
        
        if not vault_path:
            print("❌ Obsidian vault path not configured")
            return
        
        if not os.path.exists(vault_path):
            print(f"❌ Vault path does not exist: {vault_path}")
            return
        
        ingestor = ObsidianIngestor(vault_path)
        documents = ingestor.ingest_all()
        
        # Chunk documents
        chunker_config = config.get('chunking', {})
        chunker = SemanticChunker(
            chunk_size=chunker_config.get('chunk_size', 512),
            chunk_overlap=chunker_config.get('chunk_overlap', 50),
            preserve_headers=chunker_config.get('preserve_headers', True)
        )
        
        chunks = chunker.chunk_documents(documents)
        all_chunks.extend(chunks)
        print(f"✅ Created {len(chunks)} chunks from Obsidian")
    
    # Index Notion if enabled
    if sources_config.get('notion', {}).get('enabled', False):
        print("\n📝 Indexing Notion workspace...")
        notion_key = os.getenv('NOTION_API_KEY')
        
        if not notion_key:
            print("❌ Notion API key not configured")
        else:
            try:
                ingestor = NotionIngestor(notion_key)
                documents = ingestor.ingest_all()
                
                chunks = chunker.chunk_documents(documents)
                all_chunks.extend(chunks)
                print(f"✅ Created {len(chunks)} chunks from Notion")
            except Exception as e:
                print(f"❌ Error indexing Notion: {e}")
    
    # Index GitHub if enabled
    if sources_config.get('github', {}).get('enabled', False):
        print("\n💻 Indexing GitHub repositories...")
        github_token = os.getenv('GITHUB_TOKEN')
        
        if not github_token:
            print("❌ GitHub token not configured")
        else:
            # Get repos from config or env
            repos = sources_config.get('github', {}).get('repos', [])
            if not repos:
                print("⚠️  No GitHub repositories configured")
            else:
                for repo_info in repos:
                    try:
                        owner = repo_info.get('owner')
                        repo = repo_info.get('repo')
                        branch = repo_info.get('branch', 'main')
                        
                        ingestor = GitHubIngestor(github_token, owner, repo)
                        documents = ingestor.ingest_all(branch)
                        
                        chunks = chunker.chunk_documents(documents)
                        all_chunks.extend(chunks)
                        print(f"✅ Created {len(chunks)} chunks from {owner}/{repo}")
                    except Exception as e:
                        print(f"❌ Error indexing {repo_info}: {e}")
    
    # Add to vector store
    if all_chunks:
        print(f"\n💾 Adding {len(all_chunks)} chunks to vector store...")
        vector_store.add_documents(all_chunks)
        print("✅ Indexing complete!")
    else:
        print("❌ No documents to index")


def chat_command(args):
    """Start interactive chat session."""
    print("💬 Starting RAG chat session...")
    print("Type 'exit' or 'quit' to end the session\n")
    
    # Initialize vector store
    db_path = os.getenv('CHROMA_DB_PATH', './chroma_db')
    vector_store = VectorStore(db_path=db_path)
    
    # Initialize chat
    config = load_config()
    use_hybrid = config.get('retrieval', {}).get('use_hybrid_search', True)
    chat = RAGChat(vector_store)
    debug = getattr(args, 'debug', False)
    
    while True:
        try:
            query = input("\n🤔 Your question: ").strip()
            
            if query.lower() in ['exit', 'quit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not query:
                continue
            
            print("\n🔍 Searching knowledge base...")
            response = chat.chat(query, use_hybrid=use_hybrid, debug=debug)
            print(f"\n💡 Answer:\n{response}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")


def query_command(args):
    """Run a single query."""
    # Initialize vector store
    db_path = os.getenv('CHROMA_DB_PATH', './chroma_db')
    vector_store = VectorStore(db_path=db_path)
    
    # Initialize chat
    config = load_config()
    use_hybrid = config.get('retrieval', {}).get('use_hybrid_search', True)
    chat = RAGChat(vector_store)
    
    print(f"🔍 Query: {args.query}")
    debug = getattr(args, 'debug', False)
    response = chat.chat(args.query, use_hybrid=use_hybrid, debug=debug)
    print(f"\n💡 Answer:\n{response}")


def clear_command(args):
    """Clear the vector store."""
    if getattr(args, 'yes', False):
        confirm = 'yes'
    else:
        confirm = input("⚠️  Are you sure you want to clear the vector store? (yes/no): ")
    
    if confirm.lower() == 'yes':
        db_path = os.getenv('CHROMA_DB_PATH', './chroma_db')
        vector_store = VectorStore(db_path=db_path)
        vector_store.clear()
        print("✅ Vector store cleared")
    else:
        print("❌ Cancelled")


def main():
    parser = argparse.ArgumentParser(description='MindOS RAG System CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Index command
    index_parser = subparsers.add_parser('index', help='Index documents from data sources')
    
    # Chat command
    chat_parser = subparsers.add_parser('chat', help='Start interactive chat session')
    chat_parser.add_argument('--debug', action='store_true', help='Show debug information about retrieved results')
    
    # Query command
    query_parser = subparsers.add_parser('query', help='Run a single query')
    query_parser.add_argument('query', help='The question to ask')
    query_parser.add_argument('--debug', action='store_true', help='Show debug information about retrieved results')
    
    # Clear command
    clear_parser = subparsers.add_parser('clear', help='Clear the vector store')
    clear_parser.add_argument('--yes', action='store_true', help='Skip confirmation prompt')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == 'index':
        index_command(args)
    elif args.command == 'chat':
        chat_command(args)
    elif args.command == 'query':
        query_command(args)
    elif args.command == 'clear':
        clear_command(args)


if __name__ == '__main__':
    main()

