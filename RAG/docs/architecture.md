# Architecture Documentation

## System Overview

The MindOS RAG system is built with a modular architecture that separates concerns into distinct layers:

1. **Data Ingestion Layer** - Connects to various data sources
2. **Chunking Layer** - Splits documents into optimal chunks
3. **Vector Store Layer** - Manages embeddings and similarity search
4. **Retrieval Layer** - Implements hybrid search (vector + keyword)
5. **LLM Layer** - Generates responses using retrieved context
6. **Interface Layer** - CLI and future web/desktop interfaces

## Component Details

### Data Ingestion (`src/ingestors/`)

**ObsidianIngestor**
- Parses Markdown files from Obsidian vault
- Extracts frontmatter, tags, links, headings
- Handles file metadata (created/modified dates)

**NotionIngestor**
- Connects to Notion API
- Indexes pages and databases
- Extracts rich text content

**GitHubIngestor**
- Indexes code repositories
- Parses code files, READMEs, documentation
- Extracts file metadata

**PDFIngestor**
- Parses PDF documents
- Extracts text and metadata
- Handles multi-page documents

### Chunking (`src/chunking/`)

**SemanticChunker**
- Preserves semantic meaning when splitting documents
- Supports heading-based chunking for Markdown
- Falls back to size-based chunking
- Configurable overlap to maintain context

### Vector Store (`src/retrieval/vector_store.py`)

**VectorStore**
- Wraps ChromaDB for local vector storage
- Manages embeddings using OpenAI
- Provides similarity search
- Handles document insertion and retrieval

### Hybrid Search (`src/retrieval/hybrid_search.py`)

**HybridSearch**
- Combines vector similarity with keyword matching
- Extracts keywords from queries
- Scores results using both methods
- Returns top-k most relevant results

### LLM Integration (`src/llm/chat.py`)

**RAGChat**
- Formats retrieved context for LLM
- Manages conversation flow
- Generates responses using GPT-4/Claude
- Includes source attribution

## Data Flow

1. **Indexing Flow:**
   ```
   Data Source → Ingestor → Documents → Chunker → Chunks → Vector Store
   ```

2. **Query Flow:**
   ```
   User Query → Hybrid Search → Retrieve Context → Format → LLM → Response
   ```

## Technology Stack

- **Framework:** LlamaIndex (RAG framework)
- **Vector DB:** ChromaDB (local, free)
- **Embeddings:** OpenAI `text-embedding-3-small`
- **LLM:** OpenAI GPT-4 Turbo (configurable)
- **Language:** Python 3.10+

## Configuration

All configuration is managed through:
- `config/config.yaml` - System settings
- `.env` - API keys and secrets

## Extensibility

The system is designed to be easily extended:

1. **New Data Sources:** Add new ingestor classes in `src/ingestors/`
2. **New Chunking Strategies:** Implement in `src/chunking/`
3. **New Search Methods:** Extend `src/retrieval/`
4. **New Interfaces:** Add to `src/cli.py` or create new interface modules

## Performance Considerations

- **Embedding Generation:** One-time cost per document chunk
- **Vector Search:** Fast similarity search using ChromaDB
- **LLM Calls:** Per-query cost, can be optimized with caching
- **Storage:** Local ChromaDB, scales to thousands of documents

## Security & Privacy

- All data stored locally (ChromaDB)
- API keys stored in `.env` (not committed)
- No data sent to third parties except OpenAI/Anthropic for embeddings/LLM
- Option to use fully local models (Ollama) for complete privacy

