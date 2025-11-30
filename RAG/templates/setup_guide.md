# MindOS RAG System - Setup Guide

Complete guide to setting up your personal RAG system.

## What is RAG?

RAG (Retrieval-Augmented Generation) solves the "context loss" problem with AI. Instead of relying on the AI's limited memory, RAG:

1. Stores your documents in a "vector database" (like a smart index)
2. Searches for relevant information when you ask a question
3. Provides that context to the AI
4. Gets accurate answers based on YOUR data

Think of it as giving the AI a "hard drive" to complement its "RAM."

## Quick Start (5 Minutes)

1. **Install Python 3.10+** (if not already installed)

2. **Clone or download this repository**

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment:**
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

5. **Configure your Obsidian vault path** in `config/config.yaml` or `.env`

6. **Index your data:**
```bash
python src/cli.py index
```

7. **Start chatting:**
```bash
python src/cli.py chat
```

## Detailed Setup

### Step 1: Python Environment

Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Get API Keys

**OpenAI API Key (Required):**
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Add to `.env` file:

```
OPENAI_API_KEY=sk-...
```

**Notion API Key (Optional):**
1. Go to https://www.notion.so/my-integrations
2. Create a new integration
3. Share your pages with the integration
4. Add to `.env`:

```
NOTION_API_KEY=secret_...
```

**GitHub Token (Optional):**
1. Go to https://github.com/settings/tokens
2. Create a personal access token
3. Add to `.env`:

```
GITHUB_TOKEN=ghp_...
```

### Step 4: Configure Data Sources

Edit `config/config.yaml`:

```yaml
sources:
  obsidian:
    enabled: true
    vault_path: /path/to/your/vault
  notion:
    enabled: false  # Set to true if using Notion
  github:
    enabled: false  # Set to true if using GitHub
```

### Step 5: Index Your Data

Run the indexing command:

```bash
python src/cli.py index
```

This will:
- Parse all your Obsidian notes
- Create semantic chunks
- Generate embeddings
- Store in vector database

**First time indexing may take a few minutes** depending on the size of your vault.

### Step 6: Test It Out

Try asking a question:

```bash
python src/cli.py query "What was my trading strategy from last month?"
```

Or start an interactive session:

```bash
python src/cli.py chat
```

## Troubleshooting

### "Module not found" errors

Make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

### "API key not found" errors

Check that your `.env` file exists and has the correct API keys.

### "Vault path does not exist"

Verify the path in `config/config.yaml` or `.env` is correct.

### Slow indexing

This is normal for large vaults. The first index takes time, but subsequent updates are faster.

## Next Steps

- Read the [Usage Guide](usage.md) for advanced features
- Check the [Architecture Documentation](architecture.md) to understand the system
- Customize the configuration for your needs
- Add more data sources (Notion, GitHub, etc.)

## Support

For issues or questions, check the documentation or open an issue in the repository.

