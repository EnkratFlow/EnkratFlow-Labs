# Quick Start: Work Laptop Setup

**Fastest way to get RAG running on your work laptop**

---

## Option 1: Git Clone (Recommended)

**If you have GitHub access:**

```bash
# On work laptop
cd ~/Documents  # or wherever you want it
git clone https://github.com/MindOS-Systems/rag-system.git
cd rag-system
./setup-work-laptop.sh
```

Then edit `.env` with your API key and vault path.

---

## Option 2: Copy Files

**If no GitHub access:**

1. **On personal laptop:**
   ```bash
   cd /Users/guyrobo/MindOS/MindOS-Labs
   # Copy RAG folder to USB/cloud
   ```

2. **On work laptop:**
   ```bash
   # Extract/copy RAG folder
   cd ~/Documents/rag-system  # or wherever
   ./setup-work-laptop.sh
   ```

---

## After Setup

1. **Edit `.env`:**
   ```
   OPENAI_API_KEY=sk-your-key-here
   OBSIDIAN_VAULT_PATH=/path/to/work/vault
   CHROMA_DB_PATH=./chroma_db_work
   ```

2. **Index:**
   ```bash
   source venv/bin/activate
   python src/cli.py index
   ```

3. **Use it:**
   ```bash
   python src/cli.py chat
   ```

---

## Work-Specific Tips

- **Keep separate:** Use `chroma_db_work` for work data
- **Work config:** Use `config/config.work.yaml` for work settings
- **Privacy:** Don't mix personal and work data in same index
- **Compliance:** Check company IT policies before indexing work data

---

**That's it!** See `plan/DEPLOYMENT_TO_WORK_LAPTOP.md` for detailed guide.

