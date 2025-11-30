# Installation Guide

## Prerequisites

- Python 3.10 or higher
- OpenAI API key (for embeddings and LLM)
- Git (for version control)

## Step 1: Clone or Navigate to RAG Directory

```bash
cd /Users/guyrobo/MindOS/MindOS-Labs/RAG
```

## Step 2: Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Configure Environment

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your API keys:
```bash
OPENAI_API_KEY=your_openai_api_key_here
OBSIDIAN_VAULT_PATH=/path/to/your/obsidian/vault
```

## Step 5: Configure Data Sources

Edit `config/config.yaml` to enable/disable data sources and set paths.

## Step 6: Index Your Data

```bash
python src/cli.py index
```

## Step 7: Start Chatting

```bash
python src/cli.py chat
```

Or run a single query:

```bash
python src/cli.py query "What was my trading strategy from last month?"
```

## Troubleshooting

### Import Errors

If you get import errors, make sure you're in the RAG directory and have activated your virtual environment.

### API Key Errors

Ensure your `.env` file has the correct API keys and is in the RAG directory.

### Vector Store Errors

If you encounter vector store errors, try clearing and re-indexing:

```bash
python src/cli.py clear
python src/cli.py index
```

