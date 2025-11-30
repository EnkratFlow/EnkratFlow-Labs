# Privacy Policy - MindOS RAG System

**Last Updated:** [Date]  
**Product:** MindOS RAG System (Personal Knowledge Base with AI)  
**Version:** 1.0

---

## 1. Introduction

MindOS RAG System ("we", "our", "us") is committed to protecting your privacy. This Privacy Policy explains how we handle data in relation to the Software.

**Key Principle:** Your data stays local. We don't collect, store, or transmit your personal data.

---

## 2. Data Collection

### 2.1 What We Don't Collect
We do **NOT** collect:
- Your documents or content
- Your search queries
- Your API keys or credentials
- Your personal information
- Usage analytics or telemetry
- Location data
- Device information

### 2.2 What You Control
- All data indexing is done locally on your device
- All vector database storage is local
- All search operations are local
- You choose what to index

---

## 3. Third-Party Services

### 3.1 OpenAI API
When you use OpenAI API for embeddings and LLM:
- **Data Sent:** Your document content is sent to OpenAI for processing
- **OpenAI's Use:** Subject to OpenAI's Privacy Policy and Terms
- **Your Control:** You can opt out of data training (see OpenAI settings)
- **Our Role:** We do not store or access this data

**Recommendation:** Review OpenAI's Privacy Policy: https://openai.com/policies/privacy-policy

### 3.2 Notion API
When you connect Notion:
- **Data Access:** You authorize access to your Notion workspace
- **Notion's Control:** Data remains in your Notion account
- **Our Role:** We do not store Notion data, only process it locally
- **Your Control:** You can revoke access at any time

### 3.3 GitHub API
When you connect GitHub:
- **Data Access:** You authorize access via personal access token
- **GitHub's Control:** Data remains in your GitHub repositories
- **Our Role:** We do not store GitHub data, only process it locally
- **Your Control:** You can revoke access at any time

---

## 4. Local Data Storage

### 4.1 ChromaDB Vector Database
- Stored locally on your device
- Contains embeddings of your documents
- Not transmitted to us or third parties
- You can delete at any time

### 4.2 Configuration Files
- `.env` file contains your API keys (local only)
- `config.yaml` contains your settings (local only)
- Not shared or transmitted

### 4.3 Logs
- Any logs are stored locally
- No remote logging or telemetry
- You control log retention

---

## 5. Data Security

### 5.1 Your Responsibility
- Secure your API keys
- Use strong passwords
- Keep your system updated
- Use encryption for sensitive data

### 5.2 Our Commitment
- Software designed for local operation
- No network transmission of your data (except to APIs you authorize)
- No data collection or storage on our servers

---

## 6. Data Rights

### 6.1 Your Rights
You have the right to:
- **Access:** All your data is local and accessible
- **Delete:** Delete indexed data at any time
- **Export:** Export your data (vector database, configs)
- **Control:** Choose what to index and when

### 6.2 Data Deletion
- Delete vector database: Remove `chroma_db/` folder
- Delete configuration: Remove `.env` and `config.yaml`
- Uninstall: Delete the Software folder

---

## 7. Children's Privacy

The Software is not intended for users under 18. We do not knowingly collect data from children.

---

## 8. International Users

### 8.1 GDPR (EU Users)
- All data processing is local (on your device)
- No data transfer to third countries
- You have full control over your data
- Right to deletion: Delete local files

### 8.2 CCPA (California Users)
- We do not sell personal information (we don't collect it)
- You have right to know: All data is local and visible
- You have right to delete: Delete local files

---

## 9. Changes to Privacy Policy

We may update this Privacy Policy. Changes will be communicated through:
- Product documentation
- Version release notes
- Email (if provided)

---

## 10. Contact

For privacy questions, contact:
- Email: [Your Email]
- Website: [Your Website]

---

## 11. Effective Date

This Privacy Policy is effective as of [Date] and applies to all versions of the Software.

---

**Your privacy is important to us. This Software is designed to keep your data local and under your control.**

