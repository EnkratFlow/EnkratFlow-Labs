# EnkratFlow RAG System

Personal RAG (Retrieval-Augmented Generation) system for semantic search across all your data sources.

## Features

- **Obsidian Vault Indexing** - Index all your Markdown notes with metadata
- **Semantic Search** - Find information by meaning, not just keywords
- **Multi-Source Support** - Connect Obsidian, Notion, GitHub, and more
- **Hybrid Search** - Combines vector similarity with keyword matching
- **CLI Interface** - Simple command-line chat interface

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy and configure environment:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Index your Obsidian vault:
```bash
python src/cli.py index
```

4. Start chatting:
```bash
python src/cli.py chat
```

## Architecture

- `src/ingestors/` - Data source connectors
- `src/chunking/` - Document chunking strategies
- `src/retrieval/` - Vector search and retrieval
- `src/llm/` - LLM integration for generation
- `src/cli.py` - Command-line interface

## Documentation

- [Installation Guide](docs/installation.md) - Step-by-step setup
- [Usage Guide](docs/usage.md) - How to use the system
- [Architecture](docs/architecture.md) - Technical details
- [Setup Guide](templates/setup_guide.md) - Complete setup walkthrough
- [Glossary & Acronyms](../reference/GLOSSARY.md) - Master reference for all acronyms and terms

## Quick Start

1. Install dependencies: `pip install -r requirements.txt`
2. Configure: Copy `.env.example` to `.env` and add your API keys
3. Index: `python src/cli.py index`
4. Chat: `python src/cli.py chat`

## Use Cases

- **Traders:** "What was my trading strategy from last month?"
- **Builders:** "Show me all my notes about RAG implementation"
- **Knowledge Workers:** "Find everything I wrote about project X"
- **Researchers:** "What did I learn about topic Y?"

## Technology

Built with:
- **LlamaIndex** - RAG framework
- **ChromaDB** - Local vector database
- **OpenAI** - Embeddings and LLM
- **Python** - Core language

## License

MIT License - See [LICENSE](LICENSE) file

## Support

For issues, questions, or contributions, please refer to the documentation or open an issue.

