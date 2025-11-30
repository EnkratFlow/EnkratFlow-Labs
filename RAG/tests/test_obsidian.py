"""
Basic tests for Obsidian ingestor
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from ingestors.obsidian import ObsidianIngestor


def test_obsidian_ingestor():
    """Test Obsidian ingestor with a sample vault."""
    # This is a basic test - adjust path as needed
    test_vault = Path(__file__).parent.parent.parent / "MindOS-Core" / "MindOS"
    
    if not test_vault.exists():
        print(f"Test vault not found at {test_vault}")
        print("Skipping test")
        return
    
    ingestor = ObsidianIngestor(str(test_vault))
    documents = ingestor.ingest_all()
    
    print(f"✅ Successfully ingested {len(documents)} documents")
    
    if documents:
        print(f"\nSample document:")
        print(f"  Title: {documents[0]['metadata'].get('title', 'N/A')}")
        print(f"  Path: {documents[0]['metadata'].get('file_path', 'N/A')}")
        print(f"  Content length: {len(documents[0]['content'])} chars")


if __name__ == '__main__':
    test_obsidian_ingestor()

