# Usage Guide

## Basic Commands

### Index Documents

Index all configured data sources:

```bash
python src/cli.py index
```

This will:
- Parse all Markdown files from your Obsidian vault
- Extract metadata (tags, links, titles)
- Chunk documents semantically
- Create embeddings and store in vector database

### Interactive Chat

Start an interactive chat session:

```bash
python src/cli.py chat
```

Type your questions and press Enter. Type `exit` or `quit` to end the session.

### Single Query

Run a single query without starting a chat session:

```bash
python src/cli.py query "What was my trading strategy from last month?"
```

### Clear Vector Store

Clear all indexed data:

```bash
python src/cli.py clear
```

## Example Queries

- "What was my trading strategy from last month?"
- "Show me all notes about RAG"
- "What did I write about MindOS?"
- "Find my notes on trading psychology"
- "What are my goals for this year?"

## Configuration

### Obsidian Vault

Set your Obsidian vault path in `config/config.yaml`:

```yaml
sources:
  obsidian:
    enabled: true
    vault_path: /path/to/your/vault
```

Or set it in `.env`:

```
OBSIDIAN_VAULT_PATH=/path/to/your/vault
```

### Notion Integration

1. Create a Notion integration at https://www.notion.so/my-integrations
2. Share your pages with the integration
3. Add your API key to `.env`:

```
NOTION_API_KEY=your_notion_api_key
```

4. Enable in `config/config.yaml`:

```yaml
sources:
  notion:
    enabled: true
```

### GitHub Integration

1. Create a GitHub personal access token
2. Add to `.env`:

```
GITHUB_TOKEN=your_github_token
```

3. Configure repositories in `config/config.yaml`:

```yaml
sources:
  github:
    enabled: true
    repos:
      - owner: your-username
        repo: your-repo
        branch: main
```

## Advanced Usage

### Custom Chunking

Adjust chunking parameters in `config/config.yaml`:

```yaml
chunking:
  strategy: semantic
  chunk_size: 512
  chunk_overlap: 50
  preserve_headers: true
```

### Hybrid Search

Hybrid search combines vector similarity with keyword matching. Enable/disable in config:

```yaml
retrieval:
  use_hybrid_search: true
  top_k: 5
```

### LLM Settings

Configure the LLM model and parameters:

```yaml
llm:
  model: gpt-4-turbo-preview
  temperature: 0.7
  max_tokens: 1000
```

