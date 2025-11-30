# Deploying RAG System to Work Laptop

**Guide to moving your RAG system from personal laptop to work laptop**

---

## Quick Answer

**Yes, you can absolutely use this on your work laptop!** The system is designed to be portable. Here's how:

---

## Method 1: Git Repository (Recommended)

**Best if:** You have GitHub access from work laptop

### Steps:

1. **Push to GitHub from personal laptop:**
   ```bash
   cd /Users/guyrobo/MindOS/MindOS-Labs/RAG
   git init  # if not already a git repo
   git add .
   git commit -m "Initial RAG system"
   git remote add origin https://github.com/MindOS-Systems/rag-system.git
   git push -u origin main
   ```

2. **Clone on work laptop:**
   ```bash
   cd ~/Documents  # or wherever you want it
   git clone https://github.com/MindOS-Systems/rag-system.git
   cd rag-system
   ```

3. **Set up on work laptop:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env with your API keys
   ```

**Advantages:**
- Easy to sync changes between laptops
- Version control
- Can work on either machine

---

## Method 2: Direct Copy (USB/Cloud)

**Best if:** No GitHub access or want quick setup

### Steps:

1. **On personal laptop, create a clean copy:**
   ```bash
   cd /Users/guyrobo/MindOS/MindOS-Labs
   # Create archive (excludes venv, chroma_db, .env)
   tar -czf rag-system.tar.gz RAG/ \
     --exclude='RAG/venv' \
     --exclude='RAG/chroma_db' \
     --exclude='RAG/.env' \
     --exclude='RAG/__pycache__' \
     --exclude='RAG/**/__pycache__'
   ```

2. **Transfer to work laptop:**
   - USB drive
   - Cloud storage (Dropbox, Google Drive, iCloud)
   - Email (if small enough)

3. **Extract on work laptop:**
   ```bash
   cd ~/Documents  # or wherever
   tar -xzf rag-system.tar.gz
   cd RAG
   ```

4. **Set up on work laptop:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env with your API keys
   ```

---

## Method 3: GitHub + Private Repo

**Best if:** You want version control but keep it private

### Steps:

1. **Create private GitHub repo:**
   - Go to GitHub
   - Create new private repository
   - Don't initialize with README

2. **Push from personal laptop:**
   ```bash
   cd /Users/guyrobo/MindOS/MindOS-Labs/RAG
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/MindOS-Systems/rag-system-private.git
   git push -u origin main
   ```

3. **Clone on work laptop:**
   ```bash
   git clone https://github.com/MindOS-Systems/rag-system-private.git
   cd rag-system-private
   # Follow setup steps
   ```

---

## What to Configure on Work Laptop

### 1. Environment Variables

Create `.env` file:
```bash
cp .env.example .env
```

Edit `.env`:
```
OPENAI_API_KEY=sk-your-key-here
OBSIDIAN_VAULT_PATH=/path/to/work/obsidian/vault
CHROMA_DB_PATH=./chroma_db
```

**Important:** Use the same OpenAI API key (it's tied to your account, not machine)

---

### 2. Obsidian Vault Path

**If you have Obsidian on work laptop:**
- Find your vault path
- Update `config/config.yaml` or `.env`

**If Obsidian vault is on work laptop:**
- Point to work vault path
- Or sync vault between laptops

**If no Obsidian on work laptop:**
- You can still use RAG with other sources (Notion, GitHub)
- Or install Obsidian on work laptop

---

### 3. Python Environment

**Check Python version:**
```bash
python3 --version
# Need 3.10+
```

**If Python not installed:**
- Install Python 3.10+ from python.org
- Or use Homebrew: `brew install python@3.11`

**Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Work Laptop Considerations

### Corporate Policies

**Check:**
- ✅ Can you install Python?
- ✅ Can you access GitHub?
- ✅ Can you use OpenAI API? (some companies block)
- ✅ Can you install pip packages?
- ✅ Are there firewall restrictions?

**If blocked:**
- Ask IT for Python installation
- Use company-approved cloud storage
- May need VPN for API access
- Consider local-only mode (Ollama)

---

### Data Privacy at Work

**Important Considerations:**
- Work laptop = company property
- Company may monitor/access files
- Don't index sensitive company data without permission
- Keep personal API keys secure
- Consider separate `.env` for work vs personal

**Recommendations:**
- Use separate ChromaDB for work data
- Don't mix personal and work data in same index
- Be aware of company data policies
- Consider work-only vault/configuration

---

### Network/Firewall Issues

**Potential Problems:**
- OpenAI API blocked
- GitHub API blocked
- Notion API blocked
- pip install blocked

**Solutions:**
- Use VPN if needed
- Use local embedding option (Ollama)
- Install packages from local cache
- Use company proxy if required

---

## Recommended Setup for Work

### Separate Configuration

Create work-specific config:

```bash
# On work laptop
cp config/config.yaml config/config.work.yaml
cp .env .env.work
```

**Work config should:**
- Point to work Obsidian vault (if separate)
- Use separate ChromaDB: `CHROMA_DB_PATH=./chroma_db_work`
- Index work-specific sources only
- Keep personal data separate

---

### Work-Only Index

**Index only work-related data:**
- Work Obsidian vault
- Work Notion workspace
- Work GitHub repos
- Work documents

**Keep separate from:**
- Personal notes
- Trading data
- Personal projects

---

## Quick Setup Script for Work Laptop

Create this script to make setup easier:

```bash
#!/bin/bash
# setup-work-rag.sh

echo "Setting up RAG system on work laptop..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.10+"
    exit 1
fi

# Create venv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup env
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ Created .env file. Please edit it with your API keys."
fi

# Create work-specific config
if [ ! -f config/config.work.yaml ]; then
    cp config/config.yaml config/config.work.yaml
    echo "✅ Created work config. Please update paths."
fi

echo "✅ Setup complete!"
echo "Next steps:"
echo "1. Edit .env with your OpenAI API key"
echo "2. Update config/config.work.yaml with work vault path"
echo "3. Run: python src/cli.py index"
```

---

## Syncing Between Laptops

### Option 1: Git (Best for Code)

**Workflow:**
- Make changes on either laptop
- Commit and push
- Pull on other laptop
- Keeps code in sync

**Note:** Don't commit `.env` or `chroma_db/` (in .gitignore)

---

### Option 2: Separate Indexes

**Workflow:**
- Personal laptop: Personal data index
- Work laptop: Work data index
- No syncing needed
- Each machine independent

**Advantages:**
- Privacy (work data stays on work laptop)
- No conflicts
- Faster (smaller indexes)

---

### Option 3: Cloud Sync (ChromaDB)

**If you want same index on both:**
- Sync `chroma_db/` folder via cloud storage
- Use same `.env` (API keys)
- Keep vaults in sync

**Warning:** 
- Large database files
- Sync conflicts possible
- Privacy concerns

---

## Step-by-Step: First Time Setup on Work Laptop

### Step 1: Transfer Files (Choose method above)
- Git clone, or
- Copy files, or
- Cloud sync

### Step 2: Install Python (if needed)
```bash
# Check if installed
python3 --version

# If not, install:
# Mac: brew install python@3.11
# Or download from python.org
```

### Step 3: Set Up Environment
```bash
cd ~/Documents/rag-system  # or wherever you put it
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 4: Configure
```bash
cp .env.example .env
# Edit .env:
# - Add OpenAI API key
# - Set work Obsidian vault path
# - Set CHROMA_DB_PATH=./chroma_db_work
```

### Step 5: Test
```bash
# Test parser
python -c "from src.ingestors.obsidian import ObsidianIngestor; print('OK')"

# Index work vault
python src/cli.py index

# Test query
python src/cli.py query "What did I write about [work topic]?"
```

---

## Troubleshooting Work Laptop Issues

### "Python not found"
- Install Python 3.10+
- Check PATH
- Use full path: `/usr/local/bin/python3`

### "pip install fails"
- Company firewall blocking
- Need VPN
- Use company proxy
- Install from local cache

### "OpenAI API error"
- Company blocking API
- Need VPN
- Check firewall rules
- Use local Ollama instead

### "Can't access Obsidian vault"
- Vault on different path
- Vault not synced
- Permissions issue
- Use relative path

### "Import errors"
- Virtual environment not activated
- Dependencies not installed
- Python version wrong
- Check `pip list`

---

## Best Practices for Work Laptop

1. **Separate Data:**
   - Work index separate from personal
   - Work config file
   - Work ChromaDB folder

2. **Security:**
   - Don't commit `.env` to git
   - Use strong API key security
   - Be aware of company monitoring

3. **Compliance:**
   - Follow company IT policies
   - Don't index sensitive data without permission
   - Understand data retention policies

4. **Backup:**
   - Regular backups of work index
   - Export important queries/results
   - Version control for code

---

## Quick Checklist

Before transferring:
- [ ] Code is in git or backed up
- [ ] `.env` is NOT included (has API keys)
- [ ] `chroma_db/` excluded (too large, personal data)
- [ ] `venv/` excluded (recreate on new machine)

On work laptop:
- [ ] Python 3.10+ installed
- [ ] Can access GitHub (if using git)
- [ ] Can access OpenAI API (or use local)
- [ ] Obsidian vault path known
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] `.env` configured
- [ ] First index successful
- [ ] First query works

---

## Recommended Approach

**For your situation (work laptop for work purposes):**

1. **Use Git** (if allowed) - easiest to sync
2. **Separate work index** - keep work data separate from personal
3. **Work-specific config** - `config.work.yaml` and `.env.work`
4. **Test incrementally** - start with small index, expand

**Command sequence:**
```bash
# On work laptop
git clone https://github.com/MindOS-Systems/rag-system.git
cd rag-system
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your settings
python src/cli.py index
python src/cli.py query "test"
```

---

**You're ready to deploy to work laptop!** The system is designed to be portable. Just make sure you have Python installed and can access the OpenAI API (or use local Ollama).

