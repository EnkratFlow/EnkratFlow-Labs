"""
Notion API Connector
Connects to Notion API to index pages and databases.
"""

from typing import List, Dict, Optional
import requests
from datetime import datetime


class NotionIngestor:
    """Ingest and parse Notion pages and databases."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        self.base_url = "https://api.notion.com/v1"
    
    def search_pages(self) -> List[Dict]:
        """Search for all pages in the workspace."""
        url = f"{self.base_url}/search"
        payload = {
            "filter": {
                "value": "page",
                "property": "object"
            }
        }
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json().get('results', [])
        except Exception as e:
            print(f"Error searching Notion pages: {e}")
            return []
    
    def get_page_content(self, page_id: str) -> Optional[str]:
        """Get the content of a Notion page."""
        url = f"{self.base_url}/blocks/{page_id}/children"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            blocks = response.json().get('results', [])
            
            # Extract text from blocks
            content_parts = []
            for block in blocks:
                block_type = block.get('type')
                if block_type == 'paragraph':
                    text = block.get('paragraph', {}).get('rich_text', [])
                    if text:
                        content_parts.append(''.join([t.get('plain_text', '') for t in text]))
                elif block_type == 'heading_1':
                    text = block.get('heading_1', {}).get('rich_text', [])
                    if text:
                        content_parts.append('# ' + ''.join([t.get('plain_text', '') for t in text]))
                elif block_type == 'heading_2':
                    text = block.get('heading_2', {}).get('rich_text', [])
                    if text:
                        content_parts.append('## ' + ''.join([t.get('plain_text', '') for t in text]))
                elif block_type == 'heading_3':
                    text = block.get('heading_3', {}).get('rich_text', [])
                    if text:
                        content_parts.append('### ' + ''.join([t.get('plain_text', '') for t in text]))
            
            return '\n'.join(content_parts)
        except Exception as e:
            print(f"Error getting page content {page_id}: {e}")
            return None
    
    def parse_page(self, page: Dict) -> Optional[Dict]:
        """Parse a Notion page into a document."""
        page_id = page.get('id')
        properties = page.get('properties', {})
        
        # Extract title
        title = "Untitled"
        for prop_name, prop_value in properties.items():
            if prop_value.get('type') == 'title':
                title_parts = prop_value.get('title', [])
                if title_parts:
                    title = ''.join([t.get('plain_text', '') for t in title_parts])
                break
        
        # Get content
        content = self.get_page_content(page_id)
        if not content:
            return None
        
        # Extract metadata
        metadata = {
            'source': 'notion',
            'page_id': page_id,
            'title': title,
            'url': page.get('url', ''),
            'created': page.get('created_time', ''),
            'modified': page.get('last_edited_time', ''),
        }
        
        return {
            'content': content,
            'metadata': metadata,
            'file_path': f"notion:{page_id}",
        }
    
    def ingest_all(self) -> List[Dict]:
        """Ingest all pages from Notion."""
        pages = self.search_pages()
        documents = []
        
        print(f"Found {len(pages)} Notion pages")
        
        for page in pages:
            doc = self.parse_page(page)
            if doc:
                documents.append(doc)
        
        print(f"Successfully parsed {len(documents)} Notion pages")
        return documents

