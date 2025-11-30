"""
Hybrid Search Implementation
Combines vector similarity search with keyword matching.
"""

import re
from typing import List, Dict
from collections import Counter


class HybridSearch:
    """Combine semantic and keyword search."""
    
    def __init__(self, vector_store, keyword_weight: float = 0.3):
        self.vector_store = vector_store
        self.keyword_weight = keyword_weight
    
    def extract_keywords(self, query: str) -> List[str]:
        """Extract keywords from query."""
        # Simple keyword extraction (can be enhanced)
        words = re.findall(r'\b\w+\b', query.lower())
        # Remove common stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'should', 'could', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which', 'who', 'whom', 'whose', 'where', 'when', 'why', 'how'}
        keywords = [w for w in words if w not in stop_words and len(w) > 2]
        return keywords
    
    def keyword_score(self, text: str, keywords: List[str]) -> float:
        """Calculate keyword match score."""
        text_lower = text.lower()
        matches = sum(1 for keyword in keywords if keyword in text_lower)
        if not keywords:
            return 0.0
        return matches / len(keywords)
    
    def hybrid_search(self, query: str, top_k: int = 5) -> List[Dict]:
        """Perform hybrid search combining vector and keyword search."""
        # Get vector search results
        vector_results = self.vector_store.search(query, top_k=top_k * 2)
        
        # Extract keywords
        keywords = self.extract_keywords(query)
        
        # Score and combine
        scored_results = []
        for result in vector_results:
            # Vector similarity score (normalized to 0-1)
            vector_score = result.get('score', 0.0) or 0.0
            if vector_score < 0:
                vector_score = 0.0
            if vector_score > 1:
                vector_score = 1.0
            
            # Keyword score
            keyword_score = self.keyword_score(result['content'], keywords)
            
            # Combined score
            combined_score = (1 - self.keyword_weight) * vector_score + self.keyword_weight * keyword_score
            
            scored_results.append({
                **result,
                'vector_score': vector_score,
                'keyword_score': keyword_score,
                'combined_score': combined_score
            })
        
        # Sort by combined score and return top_k
        scored_results.sort(key=lambda x: x['combined_score'], reverse=True)
        return scored_results[:top_k]

