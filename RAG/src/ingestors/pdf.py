"""
PDF Document Parser
Parses PDF files and extracts text content.
"""

from typing import List, Dict, Optional
from pathlib import Path
from pypdf import PdfReader


class PDFIngestor:
    """Ingest and parse PDF documents."""
    
    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)
        if not self.pdf_path.exists():
            raise ValueError(f"PDF path does not exist: {pdf_path}")
    
    def parse_pdf(self) -> Optional[Dict]:
        """Parse a single PDF file."""
        try:
            reader = PdfReader(str(self.pdf_path))
            
            # Extract text from all pages
            text_parts = []
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    text_parts.append(text)
            
            content = '\n\n'.join(text_parts)
            
            # Extract metadata
            metadata = {
                'source': 'pdf',
                'file_path': str(self.pdf_path),
                'file_name': self.pdf_path.name,
                'num_pages': len(reader.pages),
            }
            
            # Try to get PDF metadata
            if reader.metadata:
                if reader.metadata.title:
                    metadata['title'] = reader.metadata.title
                if reader.metadata.author:
                    metadata['author'] = reader.metadata.author
                if reader.metadata.subject:
                    metadata['subject'] = reader.metadata.subject
            
            return {
                'content': content,
                'metadata': metadata,
                'file_path': str(self.pdf_path),
            }
        except Exception as e:
            print(f"Error parsing PDF {self.pdf_path}: {e}")
            return None
    
    def ingest_all(self, directory: str) -> List[Dict]:
        """Ingest all PDF files from a directory."""
        pdf_dir = Path(directory)
        if not pdf_dir.exists():
            raise ValueError(f"Directory does not exist: {directory}")
        
        pdf_files = list(pdf_dir.glob("*.pdf"))
        documents = []
        
        print(f"Found {len(pdf_files)} PDF files")
        
        for pdf_file in pdf_files:
            ingestor = PDFIngestor(str(pdf_file))
            doc = ingestor.parse_pdf()
            if doc:
                documents.append(doc)
        
        print(f"Successfully parsed {len(documents)} PDF files")
        return documents

