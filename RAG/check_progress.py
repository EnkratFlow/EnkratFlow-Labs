#!/usr/bin/env python3
"""
Quick script to check indexing progress by counting items in ChromaDB.
"""
import os
import sys
import chromadb
from chromadb.config import Settings as ChromaSettings

def check_progress():
    db_path = "./chroma_db"
    collection_name = "enkratflow_rag"
    
    if not os.path.exists(db_path):
        print("❌ ChromaDB folder doesn't exist yet. Indexing hasn't started.")
        return
    
    try:
        client = chromadb.PersistentClient(
            path=db_path,
            settings=ChromaSettings(anonymized_telemetry=False)
        )
        
        try:
            collection = client.get_collection(name=collection_name)
            count = collection.count()
            print(f"✅ Current progress: {count} chunks indexed in ChromaDB")
            
            if count > 0:
                # Get a sample to verify it's working
                results = collection.peek(limit=1)
                if results['ids']:
                    print(f"   Sample ID: {results['ids'][0][:50]}...")
                    print(f"   ✓ Data is being stored correctly")
        except Exception as e:
            print(f"⚠️  Collection '{collection_name}' not found or empty: {e}")
            print("   This might mean indexing hasn't started yet or is still initializing.")
            
    except Exception as e:
        print(f"❌ Error checking progress: {e}")

if __name__ == "__main__":
    check_progress()

