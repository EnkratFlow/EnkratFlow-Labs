"""
GitHub Repository Indexer
Indexes code files, READMEs, and issues from GitHub repositories.
"""

from typing import List, Dict, Optional
import requests
from pathlib import Path
import base64


class GitHubIngestor:
    """Ingest and parse GitHub repository content."""
    
    def __init__(self, token: str, owner: str, repo: str):
        self.token = token
        self.owner = owner
        self.repo = repo
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.base_url = f"https://api.github.com/repos/{owner}/{repo}"
    
    def get_file_content(self, path: str) -> Optional[str]:
        """Get the content of a file from GitHub."""
        url = f"{self.base_url}/contents/{path}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            
            if data.get('type') == 'file':
                content = base64.b64decode(data.get('content', '')).decode('utf-8')
                return content
            return None
        except Exception as e:
            print(f"Error getting file {path}: {e}")
            return None
    
    def get_repo_tree(self, branch: str = "main") -> List[Dict]:
        """Get the file tree of the repository."""
        url = f"{self.base_url}/git/trees/{branch}?recursive=1"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            tree = response.json().get('tree', [])
            
            # Filter for code files and markdown
            code_extensions = ['.py', '.js', '.ts', '.md', '.txt', '.json', '.yaml', '.yml']
            files = [
                item for item in tree
                if item.get('type') == 'blob' and 
                any(item.get('path', '').endswith(ext) for ext in code_extensions)
            ]
            
            return files
        except Exception as e:
            print(f"Error getting repo tree: {e}")
            return []
    
    def parse_file(self, file_item: Dict) -> Optional[Dict]:
        """Parse a GitHub file into a document."""
        path = file_item.get('path', '')
        sha = file_item.get('sha', '')
        
        content = self.get_file_content(path)
        if not content:
            return None
        
        # Extract metadata
        file_ext = Path(path).suffix
        metadata = {
            'source': 'github',
            'repo': f"{self.owner}/{self.repo}",
            'file_path': path,
            'file_type': file_ext,
            'sha': sha,
        }
        
        return {
            'content': content,
            'metadata': metadata,
            'file_path': f"github:{self.owner}/{self.repo}/{path}",
        }
    
    def ingest_all(self, branch: str = "main") -> List[Dict]:
        """Ingest all code files from the repository."""
        files = self.get_repo_tree(branch)
        documents = []
        
        print(f"Found {len(files)} files in {self.owner}/{self.repo}")
        
        for file_item in files:
            doc = self.parse_file(file_item)
            if doc:
                documents.append(doc)
        
        print(f"Successfully parsed {len(documents)} files from GitHub")
        return documents

