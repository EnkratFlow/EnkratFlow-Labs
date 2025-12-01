# 🗺️ EnkratFlow Strategic Roadmap

## 🚩 The North Star

**To build the Operating System for Self-Mastery.**

We start by solving the most expensive pain point (Trading Psychology) and expand to the widest pain point (Work Productivity).

---

## 🏗️ Phase 1: The Core & The Internal Tool (Current)

*Goal: Prove the RAG engine works on my own messy data (Notion/Obsidian).*

- [ ] **CoreLattice Engine**

    - [x] Set up Python + LlamaIndex environment.

    - [ ] Build "Universal Schema" (SQLite) for storing disparate data types (Trades vs. Tasks).

    - [ ] Implement `NotionIngestor` to pull meeting notes automatically.

- [ ] **The "Dogfood" Dashboard (Internal Only)**

    - [ ] Build a simple Streamlit UI (`src/app.py`).

    - [ ] Feature: "Chat with my Meetings" (RAG).

    - [ ] Feature: "Auto-Extract Action Items" to a Todo list.

- [ ] **Data Pipeline**

    - [ ] Connect Obsidian Vault for personal knowledge retrieval.

## 🚀 Phase 2: The Wedge (The Commercial Trading Product)

*Goal: Launch a Minimum Viable Product (MVP) for Traders to generate revenue.*

- [ ] **The "EnkratFlow" Trading UI**

    - [ ] Build a separate, high-performance Frontend (React/Next.js or Streamlit Pro).

    - [ ] Design "Dark Mode" aesthetic (Red/Teal accents).

- [ ] **Trading Features**

    - [ ] **Journal Ingestor:** Allow users to upload trade logs (CSV/PDF).

    - [ ] **Psych-Analysis:** RAG prompts that identify "Tilt" or "Revenge Trading" patterns.

    - [ ] **The "Pre-Flight" Check:** A wizard that forces users to confirm their state before trading.

- [ ] **Business Logic**

    - [ ] Integrate Stripe for subscriptions.

    - [ ] Set up User Auth (Supabase/Firebase).

## 🔮 Phase 3: The Expansion (Work Mode)

*Goal: Turn the internal tool into a "Pro" feature for retention.*

- [ ] **The "Lobby" Interface**

    - [ ] Create a unified login screen that lets users choose: `[ ⚔️ TRADING ]` or `[ 🛡️ WORK ]`.

- [ ] **Work Features**

    - [ ] **Privacy Lock:** Ensure Work data (PDFs/Meetings) never leaks into Trading context.

    - [ ] **Executive Assistant:** "What did I promise to do in the last meeting?"

- [ ] **Cross-Pollination**

    - [ ] Feature: "Context Awareness" (e.g., "You had a rough trading morning; maybe skip the high-stakes negotiation meeting?").

---

## 📉 Technical Debt & Infrastructure

- [ ] **Hosting:** Deploy backend to Render/Railway.

- [ ] **Database:** Migrate SQLite to PostgreSQL (Supabase) before Phase 2 launch.

- [ ] **Domain:** Secure `enkratflow.com` and `enkratflow.ai`.

