"""
Obsidian Vault Parser
Parses Markdown files from Obsidian vault and extracts metadata.
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
import frontmatter


class ObsidianIngestor:
    """Ingest and parse Obsidian vault files."""
    
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        if not self.vault_path.exists():
            raise ValueError(f"Vault path does not exist: {vault_path}")
    
    def get_all_markdown_files(self) -> List[Path]:
        """Get all .md files from the vault."""
        md_files = []
        for root, dirs, files in os.walk(self.vault_path):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for file in files:
                if file.endswith('.md'):
                    md_files.append(Path(root) / file)
        
        return md_files
    
    def extract_metadata(self, content: str, file_path: Path) -> Dict:
        """Extract metadata from Markdown file."""
        metadata = {
            'source': 'obsidian',
            'file_path': str(file_path.relative_to(self.vault_path)),
            'full_path': str(file_path),
            'tags': [],
            'links': [],
            'title': file_path.stem,
            'created': None,
            'modified': None,
        }
        
        # Try to parse frontmatter
        clean_content = content
        try:
            post = frontmatter.loads(content)
            if post.metadata:
                metadata.update(post.metadata)
                clean_content = post.content
        except:
            pass
        
        # Extract tags (#tag format)
        tags = re.findall(r'#(\w+)', clean_content)
        metadata['tags'] = list(set(tags))
        
        # Extract internal links [[link]]
        links = re.findall(r'\[\[([^\]]+)\]\]', clean_content)
        metadata['links'] = list(set(links))
        
        # Extract title from first heading
        heading_match = re.search(r'^#\s+(.+)$', clean_content, re.MULTILINE)
        if heading_match:
            metadata['title'] = heading_match.group(1)
        
        # Get file modification time
        try:
            stat = file_path.stat()
            metadata['modified'] = datetime.fromtimestamp(stat.st_mtime).isoformat()
            metadata['created'] = datetime.fromtimestamp(stat.st_ctime).isoformat()
        except:
            pass
        
        return metadata, clean_content
    
    def parse_file(self, file_path: Path) -> Optional[Dict]:
        """Parse a single Markdown file."""
        try:
            # Try UTF-8 first, then fallback to other encodings
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
            content = None
            
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding, errors='replace') as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                print(f"Error: Could not decode {file_path} with any encoding")
                return None
            
            metadata, clean_content = self.extract_metadata(content, file_path)
            
            return {
                'content': clean_content,
                'metadata': metadata,
                'file_path': str(file_path),
            }
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None
    
    def ingest_all(self) -> List[Dict]:
        """Ingest all Markdown files from the vault."""
        md_files = self.get_all_markdown_files()
        documents = []
        
        print(f"Found {len(md_files)} Markdown files")
        
        for file_path in md_files:
            doc = self.parse_file(file_path)
            if doc:
                documents.append(doc)
        
        print(f"Successfully parsed {len(documents)} files")
        return documents

