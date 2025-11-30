# MindOS Projects: Acronyms & Glossary

**Master reference for all acronyms and technical terms across MindOS projects**

*This glossary is searchable by the RAG system and serves as a central reference for all projects.*

---

## Table of Contents

- [RAG System Acronyms](#rag-system-acronyms)
- [Trading Journal Acronyms](#trading-journal-acronyms)
- [General Technology Acronyms](#general-technology-acronyms)
- [Business & Project Management](#business--project-management)
- [Legal & Compliance](#legal--compliance)
- [File Formats & Extensions](#file-formats--extensions)
- [Quick Reference by Category](#quick-reference-by-category)

---

## RAG System Acronyms

### Core RAG Terms

- **RAG** - Retrieval-Augmented Generation. Technique that enhances LLMs by retrieving relevant context from external data sources before generating responses. Solves the "context loss" problem in monolithic LLMs.

- **LLM** - Large Language Model. AI models like GPT-4, Claude, Llama that generate human-like text based on input. Examples: OpenAI GPT-4, Anthropic Claude, Meta Llama.

- **Vector DB** - Vector Database. Database optimized for storing and searching high-dimensional vectors (embeddings). Used for semantic similarity search. Examples: ChromaDB, Pinecone, Weaviate.

- **Embedding** - Numerical representation of text that captures semantic meaning. Converts text into a list of numbers (vector) that can be compared for similarity. Used for finding similar content.

- **Chunking** - Process of splitting documents into smaller pieces for indexing. Prevents context loss and improves retrieval accuracy. Types: fixed-size, semantic, heading-based.

- **Semantic Search** - Search based on meaning, not just keywords. Finds content that means the same thing even if words are different.

- **Hybrid Search** - Combining vector similarity search with keyword matching. Improves retrieval accuracy by using both semantic and exact match.

- **Top-K** - Returns the top K most relevant results. Common values: top-3, top-5, top-10.

- **Re-ranking** - Second-pass ranking of retrieved results to improve relevance. More expensive but more accurate.

### RAG Technical Terms

- **ChromaDB** - Open-source vector database used in RAG system. Local, free, good for personal use.

- **LlamaIndex** - Python framework for building RAG applications. Provides document handling, chunking, and retrieval out-of-the-box.

- **LangChain** - Alternative framework for building LLM applications. More flexible but lower-level than LlamaIndex.

- **Ollama** - Tool for running LLMs locally (no API needed). Free, private, but requires local compute.

- **Pinecone** - Cloud-based vector database (alternative to ChromaDB). Scalable, managed service, costs money.

- **Weaviate** - Another vector database option. Open-source, can be self-hosted or cloud.

- **OpenAI Embeddings** - Text embedding models from OpenAI. `text-embedding-3-small` is cost-effective, `text-embedding-3-large` is more accurate.

- **GPT-4** - OpenAI's most capable language model. Used for generating responses in RAG systems.

- **GPT-4 Turbo** - Faster, cheaper version of GPT-4 with similar capabilities.

- **Claude** - Anthropic's language model. Alternative to GPT-4, known for longer context windows.

### RAG Process Terms

- **Indexing** - Process of processing documents, creating chunks, generating embeddings, and storing in vector database.

- **Ingestion** - Loading data from sources (Obsidian, Notion, GitHub) into the RAG system.

- **Ingestor** - Component that reads data from a specific source (e.g., ObsidianIngestor, NotionIngestor).

- **Query** - User's question or search request.

- **Retrieval** - Finding relevant chunks from vector database based on query.

- **Generation** - LLM creating response based on retrieved context.

- **Source Attribution** - Showing which document/chunk the answer came from.

---

## Trading Journal Acronyms

### Trading Terms

- **VWAP** - Volume Weighted Average Price. Key reference level for trading. Average price weighted by volume. Used as support/resistance.

- **ETH** - Extended Trading Hours. Trading outside regular market hours (pre-market, after-hours).

- **RTH** - Regular Trading Hours. Standard market trading hours (9:30 AM - 4:00 PM EST for US markets).

- **STD** - Standard Deviation. Statistical measure, used in VWAP bands to show price deviation.

- **LVN** - Low Volume Node. Price level with low trading volume. Often acts as support/resistance.

- **HVN** - High Volume Node. Price level with high trading volume. Strong support/resistance level.

- **MAE** - Maximum Adverse Excursion. Worst price move against your position after entry. Used for stop placement analysis.

- **MFE** - Maximum Favorable Excursion. Best price move in your favor after entry. Used for target placement analysis.

- **CVD** - Cumulative Volume Delta. Net buying/selling pressure indicator. Shows if buyers or sellers are in control.

- **VA** - Value Area. Price range containing 70% of volume. Most traded price range.

- **IB** - Initial Balance. First hour of trading session (9:30-10:30 AM EST). Sets tone for day.

- **FVG** - Fair Value Gap. Price gap indicating imbalance. Often gets filled. Part of ICT methodology.

- **ICT** - Inner Circle Trader. Trading methodology/style focusing on market structure, order flow, and institutional trading patterns.

- **DRC** - Daily Report Card. Summary of daily trading performance. Includes metrics, psychology, and coaching.

- **P&L** - Profit and Loss. Financial outcome of trades. Net result of winning and losing trades.

- **Entry** - Price at which trade is opened.

- **Exit** - Price at which trade is closed.

- **Stop Loss** - Price level to exit losing trade. Risk management tool.

- **Take Profit** - Price level to exit winning trade. Profit target.

- **Risk/Reward** - Ratio of potential loss to potential gain. Example: 1:2 means risking $1 to make $2.

### Trading Setup Types

- **LAF** - Look Above and Fail. Price looks above level then fails. Bearish reversal pattern.

- **LBF** - Look Below and Fail. Price looks below level then fails. Bullish reversal pattern.

- **Price Discovery** - Trading setup where price explores new areas. Often leads to reversals.

- **VWAP Bounce** - Price bounces off VWAP level. Common trading setup.

- **Order Flow** - Analysis of buying/selling pressure. Uses tools like Bookmap, Delta, CVD.

- **Market Structure** - Overall price action pattern. Balanced, imbalanced, trending, ranging.

- **Confluence** - Multiple factors aligning (e.g., VWAP + structure + order flow). Stronger setups.

### Trading Psychology Terms

- **Tilt** - Emotional state where trader makes bad decisions. Usually after losses.

- **FOMO** - Fear Of Missing Out. Entering trades due to fear of missing opportunity.

- **Revenge Trading** - Trading to recover losses. Emotional, usually leads to more losses.

- **Confidence** - Trader's belief in their setup/ability. Tracked in psychology layer.

- **Energy** - Physical/mental energy level. Affects trading performance.

- **Emotion** - Emotional state before/during/after trade. Tracked for pattern recognition.

---

## General Technology Acronyms

### Development

- **API** - Application Programming Interface. How software components communicate. Defines how to request data/services.

- **CLI** - Command Line Interface. Text-based user interface. Terminal/console interface.

- **UI** - User Interface. Visual interface users interact with. Buttons, forms, displays.

- **UX** - User Experience. Overall experience using a product. Includes usability, aesthetics, emotions.

- **SDK** - Software Development Kit. Tools for building applications. Libraries, documentation, examples.

- **SDLC** - Software Development Life Cycle. Process of developing software. Plan, design, build, test, deploy.

- **CI** - Continuous Integration. Automatically testing code changes. Catches bugs early.

- **CD** - Continuous Deployment. Automatically deploying code changes. Keeps production updated.

- **IDE** - Integrated Development Environment. Code editor with tools. Examples: VS Code, Cursor, IntelliJ.

- **OS** - Operating System. Software that manages computer resources. Examples: macOS, Windows, Linux.

### Programming Languages & Formats

- **TS** - TypeScript. Typed superset of JavaScript. Adds type safety.

- **JS** - JavaScript. Programming language for web development.

- **TSX** - TypeScript XML. React components written in TypeScript.

- **JSX** - JavaScript XML. React component syntax. HTML-like syntax in JavaScript.

- **CSS** - Cascading Style Sheets. Styling language for web pages.

- **HTML** - HyperText Markup Language. Web page markup language.

- **JSON** - JavaScript Object Notation. Data format. Lightweight, human-readable.

- **YAML** - YAML Ain't Markup Language. Configuration file format. Human-readable, uses indentation.

- **CSV** - Comma-Separated Values. Tabular data format. Spreadsheet-like.

- **PDF** - Portable Document Format. Document format. Preserves formatting.

- **MD** - Markdown. Lightweight markup language. Used for documentation, notes.

- **XML** - eXtensible Markup Language. Markup language for structured data.

### Databases

- **DB** - Database. Structured data storage system.

- **SQL** - Structured Query Language. Database query language. Used with relational databases.

- **PostgreSQL** - Open-source relational database. Used in trading journal.

- **MongoDB** - NoSQL document database. Stores JSON-like documents.

- **Prisma** - Database ORM (Object-Relational Mapping). Used in trading journal for database access.

- **ORM** - Object-Relational Mapping. Technique for accessing databases using objects instead of SQL.

### Infrastructure & Networking

- **HTTP** - HyperText Transfer Protocol. Web communication protocol. Standard for web pages.

- **HTTPS** - HTTP Secure. Encrypted web protocol. Secure version of HTTP.

- **URL** - Uniform Resource Locator. Web address. Example: https://example.com/page

- **URI** - Uniform Resource Identifier. Resource identifier. More general than URL.

- **ID** - Identifier. Unique identifier for an object.

- **UUID** - Universally Unique Identifier. Unique ID format. Example: 550e8400-e29b-41d4-a716-446655440000

- **VPN** - Virtual Private Network. Secure network connection. Encrypts internet traffic.

- **DNS** - Domain Name System. Converts domain names to IP addresses. Example: google.com → 142.250.191.14

- **TCP** - Transmission Control Protocol. Network protocol. Reliable, ordered data transmission.

- **IP** - Internet Protocol. Network addressing protocol. Routes data packets.

- **SSH** - Secure Shell. Secure remote access protocol. Encrypted terminal access.

- **SSL** - Secure Sockets Layer. Encryption protocol (deprecated, replaced by TLS).

- **TLS** - Transport Layer Security. Modern encryption protocol. Secures web connections.

- **OAuth** - Open Authorization. Authentication protocol. Allows apps to access user data.

- **JWT** - JSON Web Token. Authentication token format. Used for API authentication.

- **REST** - Representational State Transfer. API design pattern. Uses HTTP methods (GET, POST, etc.).

- **GraphQL** - Query language for APIs. Allows clients to request specific data.

- **gRPC** - Google Remote Procedure Call. High-performance API framework.

### Cloud Services

- **AWS** - Amazon Web Services. Cloud computing platform. Largest cloud provider.

- **GCP** - Google Cloud Platform. Google's cloud service.

- **Azure** - Microsoft Azure. Microsoft's cloud platform.

- **Docker** - Containerization platform. Packages applications with dependencies.

- **K8s** - Kubernetes. Container orchestration system. Manages container deployments.

- **VM** - Virtual Machine. Software emulation of a computer.

- **VMware** - Virtualization software. Creates and manages VMs.

### Package Managers

- **NPM** - Node Package Manager. Package manager for JavaScript/Node.js.

- **PIP** - Pip Installs Packages. Package manager for Python.

- **GEM** - Ruby package manager.

- **CRATES** - Rust package registry.

- **Maven** - Java build and dependency management.

- **Gradle** - Build automation tool for Java.

---

## Business & Project Management

### Project Terms

- **MVP** - Minimum Viable Product. Simplest version that works. Validates core concept.

- **PRD** - Product Requirements Document. Specifies what to build. Defines features, requirements.

- **SOP** - Standard Operating Procedure. Step-by-step process guide. Ensures consistency.

- **FAQ** - Frequently Asked Questions. Common questions and answers. Reduces support burden.

- **PKM** - Personal Knowledge Management. System for organizing knowledge. Examples: Obsidian, Notion, Roam.

- **GTD** - Getting Things Done. Productivity methodology by David Allen.

- **Zettelkasten** - Note-taking method. Creates linked knowledge network.

### Business Models

- **SaaS** - Software as a Service. Cloud-based software delivery. Subscription model.

- **B2B** - Business to Business. Selling to companies.

- **B2C** - Business to Consumer. Selling to individuals.

- **B2G** - Business to Government. Selling to government.

- **PaaS** - Platform as a Service. Cloud platform for building apps.

- **IaaS** - Infrastructure as a Service. Cloud infrastructure (servers, storage).

- **FaaS** - Function as a Service. Serverless computing. Run code without managing servers.

### Roles & Titles

- **CTO** - Chief Technology Officer. Technology leadership role.

- **CEO** - Chief Executive Officer. Company leadership role.

- **PM** - Product Manager. Manages product development.

- **EM** - Engineering Manager. Manages engineering team.

- **QA** - Quality Assurance. Testing and quality control.

- **DevOps** - Development + Operations. Combines software development and IT operations.

---

## Legal & Compliance

### Regulations

- **GDPR** - General Data Protection Regulation. EU data privacy law. Gives users control over their data.

- **CCPA** - California Consumer Privacy Act. California data privacy law. Similar to GDPR.

- **SEC** - Securities and Exchange Commission. US securities regulator. Oversees stock markets.

- **FINRA** - Financial Industry Regulatory Authority. US financial industry regulator. Self-regulatory organization.

- **CFTC** - Commodity Futures Trading Commission. US derivatives regulator. Oversees futures markets.

- **HIPAA** - Health Insurance Portability and Accountability Act. US health data privacy law.

### Legal Terms

- **ToS** - Terms of Service. Legal agreement for using software. Defines rights and responsibilities.

- **E&O** - Errors and Omissions. Type of insurance. Protects against mistakes.

- **IP** - Intellectual Property. Creative works and inventions. Copyrights, patents, trademarks.

- **PHI** - Protected Health Information. Health data privacy term. Regulated by HIPAA.

- **NDA** - Non-Disclosure Agreement. Confidentiality agreement. Prevents sharing of information.

- **DMCA** - Digital Millennium Copyright Act. US copyright law. Protects digital content.

- **CC** - Creative Commons. Copyright licensing. Allows sharing with conditions.

- **MIT License** - Open-source license. Permissive, allows commercial use.

- **GPL** - GNU General Public License. Open-source license. Requires derivative works to be open-source.

- **Apache License** - Open-source license. Permissive, includes patent grant.

---

## File Formats & Extensions

### Code Files
- **.py** - Python file
- **.js** - JavaScript file
- **.ts** - TypeScript file
- **.tsx** - TypeScript React component
- **.jsx** - JavaScript React component
- **.java** - Java file
- **.go** - Go file
- **.rs** - Rust file
- **.cpp/.c** - C/C++ file

### Data & Config Files
- **.json** - JSON data file
- **.yaml/.yml** - YAML configuration file
- **.xml** - XML data file
- **.csv** - Comma-separated values file
- **.tsv** - Tab-separated values file
- **.env** - Environment variables file
- **.ini** - Configuration file
- **.conf** - Configuration file

### Documentation
- **.md** - Markdown file
- **.txt** - Plain text file
- **.pdf** - PDF document
- **.docx** - Microsoft Word document
- **.xlsx** - Microsoft Excel spreadsheet
- **.pptx** - Microsoft PowerPoint presentation

### Archives
- **.zip** - Compressed archive
- **.tar.gz** - Compressed tar archive
- **.rar** - RAR archive
- **.7z** - 7-Zip archive

### System Files
- **.gitignore** - Git ignore rules file
- **.dockerfile** - Docker container definition
- **.sql** - SQL script file
- **.sh** - Shell script
- **.bat** - Windows batch file

### Database Files
- **.db** - SQLite database
- **.sqlite** - SQLite database
- **.mdb** - Microsoft Access database

---

## Quick Reference by Category

### RAG-Specific
**Core:** RAG, LLM, Vector DB, Embedding, Chunking, Semantic Search, Hybrid Search  
**Tools:** ChromaDB, LlamaIndex, LangChain, Ollama, Pinecone, Weaviate  
**Process:** Indexing, Ingestion, Ingestor, Query, Retrieval, Generation, Source Attribution  
**Models:** GPT-4, GPT-4 Turbo, Claude, text-embedding-3-small, text-embedding-3-large

### Trading-Specific
**Price/Volume:** VWAP, LVN, HVN, VA, IB, STD  
**Analysis:** MAE, MFE, CVD, FVG  
**Time:** ETH, RTH  
**Methodology:** ICT, DRC  
**Financial:** P&L  
**Setups:** LAF, LBF, Price Discovery, VWAP Bounce  
**Psychology:** Tilt, FOMO, Revenge Trading

### Development
**General:** API, CLI, UI, UX, SDK, SDLC, CI, CD, IDE, OS  
**Languages:** TS, JS, TSX, JSX, CSS, HTML  
**Data:** JSON, YAML, CSV, MD, PDF, XML  
**Databases:** DB, SQL, PostgreSQL, MongoDB, Prisma, ORM

### Legal/Compliance
**Regulations:** GDPR, CCPA, SEC, FINRA, CFTC, HIPAA  
**Terms:** ToS, E&O, IP, PHI, NDA, DMCA  
**Licenses:** MIT License, GPL, Apache License, CC

### Infrastructure
**Networking:** HTTP, HTTPS, URL, URI, ID, UUID, VPN, DNS, TCP, IP, SSH, SSL, TLS  
**APIs:** OAuth, JWT, REST, GraphQL, gRPC  
**Cloud:** AWS, GCP, Azure, Docker, K8s, VM, VMware  
**Package Managers:** NPM, PIP, GEM, CRATES, Maven, Gradle

### Business
**Project:** MVP, PRD, SOP, FAQ, PKM, GTD, Zettelkasten  
**Business Models:** SaaS, B2B, B2C, B2G, PaaS, IaaS, FaaS  
**Roles:** CTO, CEO, PM, EM, QA, DevOps

---

## How to Use This Glossary

1. **Search:** Use Ctrl+F (Cmd+F on Mac) to search for any acronym
2. **RAG Integration:** This file is indexed by the RAG system - ask "What does [acronym] mean?"
3. **Updates:** Add new acronyms as you encounter them
4. **Cross-Reference:** See related terms in the same category

---

## Contributing

When adding new acronyms:
1. Add to appropriate category
2. Include full name
3. Add brief explanation
4. Add context if domain-specific
5. Update Quick Reference section

---

**Last Updated:** November 29, 2025  
**Projects Covered:** RAG System, Trading Journal, MindOS Ecosystem  
**Maintained By:** MindOS Development Team

