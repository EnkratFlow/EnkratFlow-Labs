# Work Laptop Deployment Checklist

**Safe deployment guide: What you need and how to keep sensitive data separate**

---

## ✅ What You Need (Checklist)

### Required Files (Safe to Copy)
- [ ] **Source code** (`src/` folder) - No sensitive data
- [ ] **Configuration templates** (`config/config.yaml`) - Template only
- [ ] **Documentation** (`docs/`, `README.md`) - Safe
- [ ] **Requirements** (`requirements.txt`) - Safe
- [ ] **Setup scripts** (`setup-work-laptop.sh`) - Safe
- [ ] **Reference materials** (`../reference/`) - Safe
- [ ] **Legal documents** (`LEGAL/`) - Safe (templates)

### Files to NEVER Copy (Sensitive)
- [ ] **`.env` file** - Contains API keys, personal paths
- [ ] **`chroma_db/` folder** - Contains your personal indexed data
- [ ] **`venv/` folder** - Can be recreated, large
- [ ] **Any personal data** - Trading notes, personal vaults, etc.

---

## 🔒 Security & Privacy Setup

### Step 1: Create Work-Specific Configuration

**On work laptop, create separate config:**

```bash
# Create work-specific environment file
cp .env.example .env.work

# Create work-specific config
cp config/config.yaml config/config.work.yaml
```

**Edit `.env.work`:**
```bash
# Work-specific settings
OPENAI_API_KEY=sk-your-key-here  # Same key is OK (it's your account)
OBSIDIAN_VAULT_PATH=/path/to/work/vault  # WORK vault only
CHROMA_DB_PATH=./chroma_db_work  # Separate database
NOTION_API_KEY=  # Work Notion if different
GITHUB_TOKEN=  # Work GitHub if different
```

**Edit `config/config.work.yaml`:**
```yaml
sources:
  obsidian:
    enabled: true
    vault_path: /path/to/work/vault  # WORK vault only
  notion:
    enabled: false  # Or point to work Notion
  github:
    enabled: false  # Or point to work repos only
```

---

### Step 2: Use Separate Database

**Critical:** Use different ChromaDB folder for work data

```bash
# In .env.work
CHROMA_DB_PATH=./chroma_db_work  # NOT chroma_db (that's personal)
```

**Why:** Keeps work and personal indexes completely separate

---

### Step 3: Point to Work Data Sources Only

**Obsidian Vault:**
- ✅ Point to work Obsidian vault (if you have one)
- ❌ Don't point to personal vault
- ❌ Don't sync personal vault to work laptop

**Notion:**
- ✅ Use work Notion workspace (if separate)
- ❌ Don't connect personal Notion

**GitHub:**
- ✅ Index work repositories only
- ❌ Don't index personal repos

**PDFs/Documents:**
- ✅ Index work documents only
- ❌ Don't index personal documents

---

## 📋 Deployment Steps

### Phase 1: Transfer Code (No Sensitive Data)

**Option A: Git (Recommended)**
```bash
# On personal laptop
cd /Users/guyrobo/MindOS/MindOS-Labs/RAG
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/rag-system.git
git push -u origin main

# On work laptop
cd ~/Documents
git clone https://github.com/your-username/rag-system.git
cd rag-system
```

**Option B: Direct Copy (No Git)**
```bash
# On personal laptop - create clean archive
cd /Users/guyrobo/MindOS/MindOS-Labs
tar -czf rag-system-clean.tar.gz RAG/ \
  --exclude='RAG/venv' \
  --exclude='RAG/chroma_db' \
  --exclude='RAG/.env' \
  --exclude='RAG/__pycache__' \
  --exclude='RAG/**/__pycache__' \
  --exclude='RAG/.DS_Store'

# Transfer to work laptop (USB, cloud, etc.)
# Extract on work laptop
tar -xzf rag-system-clean.tar.gz
cd RAG
```

---

### Phase 2: Setup on Work Laptop

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create work-specific config
cp .env.example .env.work
cp config/config.yaml config/config.work.yaml

# 4. Edit .env.work (add your API keys, work vault path)
# 5. Edit config/config.work.yaml (point to work data sources)
```

---

### Phase 3: Configure for Work Use

**1. Set Work Vault Path:**
```bash
# In .env.work
OBSIDIAN_VAULT_PATH=/Users/yourname/Documents/work-obsidian
```

**2. Set Separate Database:**
```bash
# In .env.work
CHROMA_DB_PATH=./chroma_db_work
```

**3. Update Config:**
```yaml
# In config/config.work.yaml
sources:
  obsidian:
    vault_path: /Users/yourname/Documents/work-obsidian
```

**4. Test Configuration:**
```bash
# Activate venv
source venv/bin/activate

# Test parser (should find work vault)
python -c "from src.ingestors.obsidian import ObsidianIngestor; print('OK')"

# Index work vault only
python src/cli.py index

# Test query
python src/cli.py query "What did I write about [work topic]?"
```

---

## 🔐 What Stays on Personal Laptop

**Never transfer these:**
- ❌ Personal Obsidian vault
- ❌ Personal trading notes
- ❌ Personal Notion workspace
- ❌ Personal GitHub repos
- ❌ Personal documents/PDFs
- ❌ `.env` file with personal paths
- ❌ `chroma_db/` with personal data

**These are safe to transfer:**
- ✅ Source code
- ✅ Documentation
- ✅ Configuration templates
- ✅ Setup scripts
- ✅ Reference materials

---

## 🛡️ Privacy Best Practices

### 1. Separate Everything

**Database:**
- Personal: `chroma_db/`
- Work: `chroma_db_work/`

**Configuration:**
- Personal: `.env`, `config/config.yaml`
- Work: `.env.work`, `config/config.work.yaml`

**Data Sources:**
- Personal: Personal vault, personal Notion, personal GitHub
- Work: Work vault, work Notion, work GitHub

---

### 2. API Keys

**OpenAI API Key:**
- ✅ Same key is OK (it's your account)
- ✅ Can be used on both laptops
- ⚠️ Be aware of usage costs
- ⚠️ Company may monitor API usage

**Notion/GitHub Tokens:**
- ✅ Use separate tokens for work vs personal
- ✅ Work token only accesses work data
- ✅ Personal token only accesses personal data

---

### 3. Company Policies

**Check before deploying:**
- [ ] Can you install Python? (usually yes)
- [ ] Can you access OpenAI API? (may need VPN)
- [ ] Can you use GitHub? (check IT policy)
- [ ] Can you install pip packages? (may need approval)
- [ ] Are there data privacy restrictions?
- [ ] Can you store local databases?

**If blocked:**
- Use VPN for API access
- Use local Ollama (no API needed)
- Ask IT for Python installation
- Use company-approved storage

---

### 4. Data Separation Strategy

**Option A: Completely Separate (Recommended)**
- Work laptop: Only work data
- Personal laptop: Only personal data
- No syncing between them
- Maximum privacy

**Option B: Selective Sharing**
- Work laptop: Work data + reference materials
- Personal laptop: Personal data + reference materials
- Reference folder can be shared (no sensitive data)

---

## 📁 Recommended Folder Structure on Work Laptop

```
~/Documents/
├── rag-system/              # RAG code (from git/copy)
│   ├── src/
│   ├── config/
│   │   └── config.work.yaml  # Work-specific config
│   ├── .env.work             # Work-specific env
│   ├── chroma_db_work/       # Work data index
│   └── venv/                 # Python environment
└── work-obsidian/            # Work Obsidian vault (separate)
    └── ...
```

**Key Points:**
- RAG system in `~/Documents/rag-system/`
- Work vault separate: `~/Documents/work-obsidian/`
- Work database: `chroma_db_work/`
- No personal data anywhere

---

## ✅ Pre-Deployment Checklist

Before deploying to work laptop:

- [ ] Code is clean (no personal data in code)
- [ ] `.env` is NOT included (has personal paths)
- [ ] `chroma_db/` is NOT included (has personal data)
- [ ] `venv/` is NOT included (can recreate)
- [ ] Personal vault path removed from templates
- [ ] Work vault path identified
- [ ] Separate database folder planned (`chroma_db_work`)
- [ ] API keys ready (OpenAI, work Notion/GitHub if needed)
- [ ] Company IT policies checked
- [ ] Python 3.10+ available or can be installed

---

## 🚀 Quick Start Commands for Work Laptop

```bash
# 1. Clone/copy code
cd ~/Documents
git clone https://github.com/your-username/rag-system.git
cd rag-system

# 2. Setup environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Create work config
cp .env.example .env.work
cp config/config.yaml config/config.work.yaml

# 4. Edit .env.work:
#    - Add OPENAI_API_KEY
#    - Set OBSIDIAN_VAULT_PATH to work vault
#    - Set CHROMA_DB_PATH=./chroma_db_work

# 5. Edit config/config.work.yaml:
#    - Set work vault path
#    - Enable only work data sources

# 6. Index work data
python src/cli.py index

# 7. Test
python src/cli.py query "test query"
```

---

## 🔍 Verification Steps

After deployment, verify:

1. **No Personal Data:**
   ```bash
   # Check .env.work doesn't have personal paths
   cat .env.work | grep -i personal
   # Should return nothing
   ```

2. **Work Data Only:**
   ```bash
   # Check indexed files
   python src/cli.py query "list all indexed files"
   # Should only show work files
   ```

3. **Separate Database:**
   ```bash
   # Verify database location
   ls -la chroma_db_work/
   # Should exist and be separate from chroma_db
   ```

4. **No Personal Vault Access:**
   ```bash
   # Verify config points to work vault
   cat config/config.work.yaml | grep vault_path
   # Should show work vault path, not personal
   ```

---

## ⚠️ Important Warnings

1. **Never Index Personal Data on Work Laptop**
   - Work laptop = company property
   - Company may monitor/access files
   - Keep personal data on personal laptop only

2. **Separate Databases**
   - Use `chroma_db_work/` for work
   - Never use `chroma_db/` on work laptop
   - Prevents accidental mixing

3. **Separate Configurations**
   - Use `.env.work` and `config.work.yaml`
   - Never use personal configs on work laptop
   - Prevents pointing to personal data

4. **API Usage**
   - Company may monitor API calls
   - Be aware of usage costs
   - Consider local Ollama for sensitive queries

5. **Data Privacy**
   - Work laptop = company property
   - Assume company can access files
   - Don't store sensitive personal data

---

## 📝 Summary

**What you need:**
- ✅ Source code (no sensitive data)
- ✅ Configuration templates
- ✅ Documentation
- ✅ Python 3.10+
- ✅ OpenAI API key (your account)
- ✅ Work Obsidian vault path
- ✅ Work data sources (Notion, GitHub if using)

**What to keep separate:**
- ❌ Personal vault/data
- ❌ Personal database
- ❌ Personal configuration
- ❌ Any sensitive personal information

**Result:**
- Work laptop has RAG system
- Only indexes work data
- Completely separate from personal data
- Safe and private

---

**You're ready to deploy!** Follow the steps above to safely set up RAG on your work laptop while keeping all personal data separate and secure.

