#!/bin/bash
# Quick setup script for work laptop deployment

echo "🚀 Setting up RAG system on work laptop..."
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.10+"
    echo "   Mac: brew install python@3.11"
    echo "   Or download from python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Found Python $PYTHON_VERSION"

# Check Python version (need 3.10+)
if [ "$(printf '%s\n' "3.10" "$PYTHON_VERSION" | sort -V | head -n1)" != "3.10" ]; then
    echo "⚠️  Warning: Python 3.10+ recommended. You have $PYTHON_VERSION"
fi

# Create venv
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo ""
echo "📥 Installing dependencies (this may take a few minutes)..."
pip install --upgrade pip
pip install -r requirements.txt

# Setup env
echo ""
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ Created .env file"
    echo "   ⚠️  IMPORTANT: Edit .env and add your OpenAI API key"
    echo "   ⚠️  Set OBSIDIAN_VAULT_PATH to your work vault path"
else
    echo "✅ .env file already exists"
fi

# Create work-specific config
if [ ! -f config/config.work.yaml ]; then
    cp config/config.yaml config/config.work.yaml
    echo "✅ Created config/config.work.yaml"
    echo "   You can customize this for work-specific settings"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "   1. Edit .env file:"
echo "      - Add OPENAI_API_KEY=sk-your-key-here"
echo "      - Set OBSIDIAN_VAULT_PATH=/path/to/work/vault"
echo "      - Set CHROMA_DB_PATH=./chroma_db_work (to keep separate from personal)"
echo ""
echo "   2. Activate virtual environment:"
echo "      source venv/bin/activate"
echo ""
echo "   3. Index your work vault:"
echo "      python src/cli.py index"
echo ""
echo "   4. Test it:"
echo "      python src/cli.py query 'What did I write about [topic]?'"
echo ""
echo "💡 Tip: Keep work and personal indexes separate for privacy!"

