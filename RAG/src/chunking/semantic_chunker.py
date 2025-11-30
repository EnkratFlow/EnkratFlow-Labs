"""
Semantic Chunking Strategy
Chunks documents while preserving semantic meaning and context.
"""

import re
from typing import List, Dict
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.core.schema import Document, NodeWithScore


class SemanticChunker:
    """Chunk documents semantically while preserving context."""
    
    def __init__(self, chunk_size: int = 512, chunk_overlap: int = 50, preserve_headers: bool = True):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.preserve_headers = preserve_headers
    
    def chunk_by_heading(self, content: str, metadata: Dict) -> List[Dict]:
        """Chunk by Markdown headings to preserve semantic structure."""
        chunks = []
        
        # Split by headings
        heading_pattern = r'^(#{1,6})\s+(.+)$'
        lines = content.split('\n')
        
        current_chunk = ""
        current_heading = metadata.get('title', '')
        current_level = 0
        
        for line in lines:
            heading_match = re.match(heading_pattern, line)
            
            if heading_match:
                # Found a heading - save current chunk if it has content
                if current_chunk.strip():
                    chunks.append({
                        'content': current_chunk.strip(),
                        'metadata': {
                            **metadata,
                            'heading': current_heading,
                            'heading_level': current_level,
                        }
                    })
                
                # Start new chunk with this heading
                level = len(heading_match.group(1))
                current_heading = heading_match.group(2).strip()
                current_level = level
                current_chunk = line + "\n"  # Include heading in chunk
            else:
                # Regular content line
                current_chunk += line + "\n"
        
        # Add final chunk
        if current_chunk.strip():
            chunks.append({
                'content': current_chunk.strip(),
                'metadata': {
                    **metadata,
                    'heading': current_heading,
                    'heading_level': current_level,
                }
            })
        
        # If no headings found, fall back to size-based chunking
        if len(chunks) == 0:
            return self.chunk_by_size(content, metadata)
        
        return chunks
    
    def chunk_by_size(self, content: str, metadata: Dict) -> List[Dict]:
        """Chunk by fixed size with overlap."""
        chunks = []
        words = content.split()
        
        i = 0
        while i < len(words):
            chunk_words = words[i:i + self.chunk_size]
            chunk_text = ' '.join(chunk_words)
            
            chunks.append({
                'content': chunk_text,
                'metadata': {
                    **metadata,
                    'chunk_index': len(chunks),
                }
            })
            
            i += self.chunk_size - self.chunk_overlap
        
        return chunks
    
    def chunk_document(self, document: Dict) -> List[Dict]:
        """Chunk a document using the configured strategy."""
        content = document['content']
        metadata = document['metadata']
        
        if self.preserve_headers and 'obsidian' in metadata.get('source', ''):
            # Try heading-based chunking first
            chunks = self.chunk_by_heading(content, metadata)
        else:
            chunks = self.chunk_by_size(content, metadata)
        
        return chunks
    
    def chunk_documents(self, documents: List[Dict]) -> List[Dict]:
        """Chunk multiple documents."""
        all_chunks = []
        
        for doc in documents:
            chunks = self.chunk_document(doc)
            all_chunks.extend(chunks)
        
        return all_chunks

