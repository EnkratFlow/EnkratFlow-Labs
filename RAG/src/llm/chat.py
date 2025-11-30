"""
LLM Chat Integration
Handles conversation with LLM using retrieved context.
"""

from typing import List, Dict
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.llms.openai import OpenAI
import yaml
import os


class RAGChat:
    """Chat interface with RAG context."""
    
    def __init__(self, vector_store):
        self.vector_store = vector_store
        
        # Load config
        config_path = os.path.join(os.path.dirname(__file__), '../../config/config.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            self.config = {}
        
        # Initialize LLM
        llm_config = self.config.get('llm', {})
        self.llm = OpenAI(
            model=llm_config.get('model', 'gpt-4-turbo-preview'),
            temperature=llm_config.get('temperature', 0.7),
            max_tokens=llm_config.get('max_tokens', 1000)
        )
    
    def format_context(self, results: List[Dict], max_content_length: int = 2000) -> str:
        """Format retrieved context for LLM."""
        context_parts = []
        for i, result in enumerate(results, 1):
            source = result.get('metadata', {}).get('file_path', 'Unknown')
            heading = result.get('metadata', {}).get('heading', '')
            content = result['content'][:max_content_length]  # Configurable length
            
            context_part = f"[Source {i}: {source}"
            if heading:
                context_part += f" - {heading}"
            context_part += f"]\n{content}\n"
            context_parts.append(context_part)
        
        return "\n---\n".join(context_parts)
    
    def chat(self, query: str, use_hybrid: bool = True, debug: bool = False) -> str:
        """Chat with RAG system."""
        # Get retrieval settings from config
        retrieval_config = self.config.get('retrieval', {})
        top_k = retrieval_config.get('top_k', 10)
        max_content_length = retrieval_config.get('max_content_length', 2000)
        
        # Retrieve relevant context
        if use_hybrid:
            from retrieval.hybrid_search import HybridSearch
            hybrid = HybridSearch(self.vector_store)
            results = hybrid.hybrid_search(query, top_k=top_k)
        else:
            results = self.vector_store.search(query, top_k=top_k)
        
        # Debug output
        if debug:
            print(f"\n🔍 Retrieved {len(results)} results:")
            for i, result in enumerate(results[:5], 1):
                score = result.get('score') or result.get('combined_score', 'N/A')
                file_path = result.get('metadata', {}).get('file_path', 'Unknown')
                print(f"  {i}. Score: {score} | File: {file_path}")
        
        # Format context
        context = self.format_context(results, max_content_length=max_content_length)
        
        # Build prompt
        system_message = """You are a helpful assistant that answers questions based on the provided context from the user's personal knowledge base. 
        
If the context doesn't contain enough information to answer the question, say so. 
Always cite which source you're using when providing information.
Be concise and accurate."""
        
        user_message = f"""Context from knowledge base:
{context}

Question: {query}

Answer based on the context above:"""
        
        # Get response from LLM
        messages = [
            ChatMessage(role=MessageRole.SYSTEM, content=system_message),
            ChatMessage(role=MessageRole.USER, content=user_message)
        ]
        
        response = self.llm.chat(messages)
        return response.message.content

