"""
Vector Store Wrapper for ChromaDB
Manages embeddings and vector search.
"""

import os
import chromadb
from chromadb.config import Settings as ChromaSettings
from typing import List, Dict, Optional
from llama_index.core import VectorStoreIndex
from llama_index.core.settings import Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import yaml

# Load environment variables
load_dotenv()


class VectorStore:
    """Wrapper for ChromaDB vector store."""
    
    def __init__(self, db_path: str = "./chroma_db", collection_name: str = "mindos_rag"):
        self.db_path = db_path
        self.collection_name = collection_name
        
        # Initialize ChromaDB client
        self.client = chromadb.PersistentClient(
            path=db_path,
            settings=ChromaSettings(anonymized_telemetry=False)
        )
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )
        
        # Load config
        config_path = os.path.join(os.path.dirname(__file__), '../../config/config.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            self.config = {}
        
        # Initialize embedding model with batch size for efficient API usage
        embedding_model = self.config.get('embeddings', {}).get('model', 'text-embedding-3-small')
        embed_batch_size = self.config.get('embeddings', {}).get('batch_size', 100)
        self.embedding_model = OpenAIEmbedding(
            model=embedding_model,
            embed_batch_size=embed_batch_size  # Batch API calls for efficiency
        )
        
        # Initialize LLM
        llm_model = self.config.get('llm', {}).get('model', 'gpt-4-turbo-preview')
        self.llm = OpenAI(model=llm_model, temperature=0.7)
        
        # Set global settings
        Settings.llm = self.llm
        Settings.embed_model = self.embedding_model
        
        # Create vector store
        chroma_vector_store = ChromaVectorStore(chroma_collection=self.collection)
        
        # Create index
        self.index = VectorStoreIndex.from_vector_store(
            vector_store=chroma_vector_store
        )
    
    def add_documents(self, chunks: List[Dict]):
        """Add document chunks to the vector store with parallel processing and batch uploading."""
        from llama_index.core.schema import Document
        from concurrent.futures import ThreadPoolExecutor, as_completed
        import time
        import sys
        import json
        import multiprocessing as mp
        
        def flatten_metadata(metadata):
            """Flatten metadata to only include flat values (str, int, float, None) for ChromaDB."""
            flat_meta = {}
            for key, value in metadata.items():
                try:
                    if value is None:
                        flat_meta[key] = None
                    elif isinstance(value, bool):
                        flat_meta[key] = str(value)
                    elif isinstance(value, (str, int, float)):
                        flat_meta[key] = value
                    elif isinstance(value, list):
                        if len(value) == 0:
                            flat_meta[key] = ""
                        else:
                            flat_meta[key] = ", ".join(str(v) for v in value if v is not None)
                    elif isinstance(value, dict):
                        flat_meta[key] = json.dumps(value, default=str)
                    else:
                        flat_meta[key] = str(value) if value is not None else None
                except Exception:
                    flat_meta[key] = str(value) if value is not None else None
            return flat_meta
        
        def process_chunk_batch(chunk_batch):
            """Convert a batch of chunks to Documents."""
            documents = []
            for chunk in chunk_batch:
                flat_metadata = flatten_metadata(chunk.get('metadata', {}))
                doc = Document(
                    text=chunk['content'],
                    metadata=flat_metadata
                )
                documents.append(doc)
            return documents
        
        # Step 1: Parallel document conversion using ThreadPoolExecutor
        print(f"📝 Converting {len(chunks)} chunks to documents (parallel processing)...", flush=True)
        sys.stdout.flush()
        start_time = time.time()
        
        # Split chunks into batches for parallel processing
        num_workers = min(mp.cpu_count(), 8)
        chunk_batch_size = max(100, len(chunks) // (num_workers * 4))  # Adaptive batch size
        chunk_batches = [chunks[i:i + chunk_batch_size] for i in range(0, len(chunks), chunk_batch_size)]
        
        documents = []
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            future_to_batch = {
                executor.submit(process_chunk_batch, batch): idx
                for idx, batch in enumerate(chunk_batches)
            }
            
            completed_batches = 0
            for future in as_completed(future_to_batch):
                try:
                    batch_docs = future.result()
                    documents.extend(batch_docs)
                    completed_batches += 1
                    if completed_batches % 10 == 0 or completed_batches == len(chunk_batches):
                        print(f"  ✓ Processed {completed_batches}/{len(chunk_batches)} batches ({len(documents)} documents)...", flush=True)
                        sys.stdout.flush()
                except Exception as e:
                    print(f"  ⚠️  Error processing batch: {e}", flush=True)
                    sys.stdout.flush()
        
        conversion_time = time.time() - start_time
        print(f"  ✓ Converted all {len(documents)} chunks to documents in {conversion_time:.1f}s", flush=True)
        sys.stdout.flush()
        
        # Step 2: Batch insertion with larger batches
        embedding_batch_size = self.config.get('embeddings', {}).get('batch_size', 100)
        total_docs = len(documents)
        insertion_start = time.time()
        
        print(f"🚀 Starting optimized batch embedding generation and insertion...", flush=True)
        print(f"  Processing {total_docs} documents in batches", flush=True)
        sys.stdout.flush()
        
        try:
            current_count = self.collection.count()
            print(f"  📊 Starting from {current_count} existing chunks", flush=True)
            sys.stdout.flush()
        except:
            current_count = 0
        
        # Skip re-chunking since documents are already chunked
        # Convert Documents directly to Nodes without parsing
        from llama_index.core.schema import TextNode
        
        # Process in batches - use smaller size to avoid token limits
        # OpenAI has a 300k token limit per request, so we need to be conservative
        # Average chunk is ~512 tokens, so 50 chunks = ~25k tokens (safe margin)
        insert_batch_size = 50  # Conservative batch size to avoid token limits
        inserted_count = 0
        total_batches = (total_docs + insert_batch_size - 1) // insert_batch_size
        
        # Process batches sequentially but with larger batch size for efficiency
        for i in range(0, total_docs, insert_batch_size):
            batch = documents[i:i + insert_batch_size]
            batch_num = (i // insert_batch_size) + 1
            
            try:
                print(f"  🔄 Processing batch {batch_num}/{total_batches} ({len(batch)} documents)...", flush=True)
                sys.stdout.flush()
                batch_start = time.time()
                
                # Convert documents directly to nodes without re-chunking
                # Documents are already chunked, but we need to check for oversized chunks
                # OpenAI embedding model has 8192 token limit per text
                nodes = []
                for doc in batch:
                    # Estimate tokens (rough: 1 token ≈ 4 characters)
                    text_length = len(doc.text)
                    estimated_tokens = text_length // 4
                    
                    # If chunk is too large, split it further
                    if estimated_tokens > 7000:  # Safety margin below 8192 limit
                        # Split into smaller chunks
                        chunk_size = 6000 * 4  # ~6000 tokens in characters
                        text = doc.text
                        chunk_index = 0
                        for i in range(0, len(text), chunk_size):
                            chunk_text = text[i:i + chunk_size]
                            chunk_metadata = doc.metadata.copy()
                            chunk_metadata['split_index'] = chunk_index
                            node = TextNode(
                                text=chunk_text,
                                metadata=chunk_metadata
                            )
                            nodes.append(node)
                            chunk_index += 1
                    else:
                        # Normal sized chunk
                        node = TextNode(
                            text=doc.text,
                            metadata=doc.metadata
                        )
                        nodes.append(node)
                
                # Insert all nodes in this batch at once
                self.index.insert_nodes(nodes)
                inserted_count += len(nodes)
                
                batch_time = time.time() - batch_start
                elapsed = time.time() - insertion_start
                current_total = current_count + inserted_count
                progress = (current_total / total_docs) * 100
                avg_time_per_batch = elapsed / batch_num
                remaining_batches = total_batches - batch_num
                eta_seconds = avg_time_per_batch * remaining_batches
                eta_minutes = eta_seconds / 60
                docs_per_second = len(batch) / batch_time if batch_time > 0 else 0
                
                print(f"  ✓ Batch {batch_num}/{total_batches} complete: {current_total}/{total_docs} documents "
                      f"({progress:.1f}%) | Time: {batch_time:.1f}s | Speed: {docs_per_second:.1f} docs/s | "
                      f"ETA: ~{eta_minutes:.1f} min", flush=True)
                sys.stdout.flush()
                
            except Exception as e:
                error_msg = str(e)
                print(f"  ❌ Error inserting batch {batch_num}: {error_msg}", flush=True)
                
                # Check for rate limit errors and retry
                if "429" in error_msg or "rate limit" in error_msg.lower() or "RateLimitError" in error_msg:
                    print(f"  ⏳ Rate limit hit, waiting 10 seconds before retry...", flush=True)
                    sys.stdout.flush()
                    time.sleep(10)
                    try:
                        # Retry the batch
                        nodes = []
                        for doc in batch:
                            node = TextNode(text=doc.text, metadata=doc.metadata)
                            nodes.append(node)
                        self.index.insert_nodes(nodes)
                        inserted_count += len(nodes)
                        print(f"  ✓ Batch {batch_num} retry successful", flush=True)
                        sys.stdout.flush()
                        continue
                    except Exception as retry_error:
                        print(f"  ❌ Retry failed: {retry_error}", flush=True)
                        sys.stdout.flush()
                
                # Check for API key issues specifically
                if "401" in error_msg or "API key" in error_msg or "Authentication" in error_msg:
                    print(f"\n  ⚠️  OPENAI API KEY ERROR!", flush=True)
                    print(f"  Please check your .env file has OPENAI_API_KEY set correctly.", flush=True)
                    print(f"  The process will continue but this batch failed.", flush=True)
                
                import traceback
                traceback.print_exc()
                sys.stdout.flush()
                continue
        
        total_time = time.time() - start_time
        print(f"✅ Successfully added {inserted_count} chunks to vector store in {total_time/60:.1f} minutes", flush=True)
        print(f"   Conversion: {conversion_time:.1f}s | Insertion: {(time.time() - insertion_start)/60:.1f} min", flush=True)
        sys.stdout.flush()
    
    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search for similar documents."""
        retriever = self.index.as_retriever(similarity_top_k=top_k)
        results = retriever.retrieve(query)
        
        formatted_results = []
        for result in results:
            formatted_results.append({
                'content': result.text,
                'metadata': result.metadata,
                'score': result.score if hasattr(result, 'score') else None
            })
        
        return formatted_results
    
    def query(self, query: str) -> str:
        """Query the RAG system and get an answer."""
        query_engine = self.index.as_query_engine()
        response = query_engine.query(query)
        return str(response)
    
    def clear(self):
        """Clear all documents from the collection."""
        self.client.delete_collection(name=self.collection_name)
        self.collection = self.client.create_collection(name=self.collection_name)
        print("Vector store cleared")

