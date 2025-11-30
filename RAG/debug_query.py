#!/usr/bin/env python3
"""
Debug script to test query retrieval and see what's being found.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from retrieval.vector_store import VectorStore
from retrieval.hybrid_search import HybridSearch

def debug_query(query: str):
    """Debug a query to see what's being retrieved."""
    print(f"🔍 Debugging query: '{query}'\n")
    print("=" * 60)
    
    # Initialize vector store
    db_path = os.getenv('CHROMA_DB_PATH', './chroma_db')
    vector_store = VectorStore(db_path=db_path)
    
    # Test vector search
    print("\n1️⃣ Vector Search Results:")
    print("-" * 60)
    vector_results = vector_store.search(query, top_k=15)
    print(f"Found {len(vector_results)} results\n")
    
    for i, result in enumerate(vector_results[:10], 1):
        score = result.get('score', 'N/A')
        file_path = result.get('metadata', {}).get('file_path', 'Unknown')
        heading = result.get('metadata', {}).get('heading', '')
        content_preview = result.get('content', '')[:300]
        
        print(f"Result {i}:")
        print(f"  Score: {score}")
        print(f"  File: {file_path}")
        if heading:
            print(f"  Heading: {heading}")
        print(f"  Content: {content_preview}...")
        print()
    
    # Test hybrid search
    print("\n2️⃣ Hybrid Search Results:")
    print("-" * 60)
    hybrid = HybridSearch(vector_store)
    hybrid_results = hybrid.hybrid_search(query, top_k=15)
    print(f"Found {len(hybrid_results)} results\n")
    
    for i, result in enumerate(hybrid_results[:10], 1):
        vector_score = result.get('vector_score', 'N/A')
        keyword_score = result.get('keyword_score', 'N/A')
        combined_score = result.get('combined_score', 'N/A')
        file_path = result.get('metadata', {}).get('file_path', 'Unknown')
        heading = result.get('metadata', {}).get('heading', '')
        content_preview = result.get('content', '')[:300]
        
        print(f"Result {i}:")
        print(f"  Vector: {vector_score:.3f} | Keyword: {keyword_score:.3f} | Combined: {combined_score:.3f}")
        print(f"  File: {file_path}")
        if heading:
            print(f"  Heading: {heading}")
        print(f"  Content: {content_preview}...")
        print()
    
    # Check if query terms appear in results
    print("\n3️⃣ Query Term Analysis:")
    print("-" * 60)
    query_words = [w.lower() for w in query.split() if len(w) > 2]
    print(f"Query words: {query_words}\n")
    
    found_in_results = []
    for result in hybrid_results[:10]:
        content_lower = result.get('content', '').lower()
        matches = [word for word in query_words if word in content_lower]
        if matches:
            found_in_results.append({
                'file': result.get('metadata', {}).get('file_path', 'Unknown'),
                'matches': matches,
                'score': result.get('combined_score', 0)
            })
    
    if found_in_results:
        print("✅ Query terms found in top results:")
        for item in found_in_results:
            print(f"  {item['file']}: {', '.join(item['matches'])} (score: {item['score']:.3f})")
    else:
        print("⚠️  Query terms NOT found in top results - this might be the issue!")
        print("\n💡 Suggestions:")
        print("  - Try rephrasing your query")
        print("  - Check if the content was actually indexed")
        print("  - Verify the file path in metadata matches your Obsidian vault")
    
    # Check collection stats
    print("\n4️⃣ Collection Statistics:")
    print("-" * 60)
    try:
        count = vector_store.collection.count()
        print(f"Total chunks in database: {count}")
    except Exception as e:
        print(f"Could not get count: {e}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("Enter your query: ")
    
    debug_query(query)

