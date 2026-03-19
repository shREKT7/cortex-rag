<div align="center">

<h1>🧠 CortexRAG</h1>
<h3>Local Agentic AI · Zero API Cost · Think Locally. Reason Deeply.</h3>

<br/>

<p align="center">
  <b>A fully local, agentic Retrieval-Augmented Generation system with intelligent query routing —<br/>no OpenAI, no paid APIs, no compromises.</b>
</p>

<br/>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangGraph-Agentic_Workflows-FF6B35?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Vector_Store-FAISS-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Memory-MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white"/>
  <img src="https://img.shields.io/badge/Embeddings-sentence--transformers-yellow?style=flat-square"/>
  <img src="https://img.shields.io/badge/Web_Search-Tavily_(optional)-9B59B6?style=flat-square"/>
</p>

</div>

---

## 📌 What is CortexRAG?

**CortexRAG** is a **local-first, agentic AI system** that dynamically routes user queries through three intelligent pipelines:

| Pipeline | Trigger | Description |
|----------|---------|-------------|
| 📚 **Document RAG** | Query matches indexed content | Retrieves from your uploaded files via FAISS |
| 🤖 **General LLM** | Casual / common knowledge queries | Answers directly using local Ollama model |
| 🌐 **Web Search** | Requires real-time information | Fetches live results via Tavily (optional) |

Built on **LangGraph + Ollama**, the system runs **entirely offline** (except optional web search) — cutting every dependency on expensive cloud APIs.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                           │
│                    Streamlit  (port 8501)                       │
└───────────────────────────┬─────────────────────────────────────┘
                            │ HTTP
┌───────────────────────────▼─────────────────────────────────────┐
│                      FASTAPI BACKEND                            │
│                       (port 8000)                               │
│    POST /rag/query          POST /rag/documents/upload          │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                    LANGGRAPH AGENT GRAPH                        │
│                                                                 │
│   ┌─────────────┐                                               │
│   │   START     │                                               │
│   └──────┬──────┘                                               │
│          │                                                      │
│   ┌──────▼──────────────┐                                       │
│   │   query_classifier  │  ← Classifies: index / general /     │
│   └──────┬──────────────┘    search                            │
│          │                                                      │
│    ┌─────┴──────┬──────────────┐                                │
│    │            │              │                                │
│  ┌─▼──────┐ ┌──▼──────┐ ┌────▼──────┐                         │
│  │retriever│ │general  │ │web_search │                         │
│  │ (ReAct) │ │  llm    │ │ (Tavily)  │                         │
│  └─┬───────┘ └──┬──────┘ └────┬──────┘                         │
│    │            │              │                                │
│  ┌─▼───────┐    │         ┌────▼──────┐                        │
│  │  grade  │    │         │ generate  │                        │
│  └─┬───────┘    │         └────┬──────┘                        │
│    │            │              │                                │
│  ┌─▼──────────┐ │              │                                │
│  │yes → gen   │ │              │                                │
│  │no  → rewrite│             │                                │
│  └─┬──────────┘ │              │                                │
│    │            │              │                                │
│   ┌▼────────────▼──────────────▼┐                              │
│   │            END              │                              │
│   └─────────────────────────────┘                              │
└─────────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────▼──────┐   ┌────────▼──────┐   ┌────────▼──────┐
│    FAISS     │   │    MongoDB    │   │    Ollama     │
│ Vector Store │   │  Chat Memory  │   │  Local LLM    │
└──────────────┘   └───────────────┘   └───────────────┘
```

---

## 🔄 RAG Pipeline — Step by Step

```
User Query
    │
    ▼
┌─────────────────────────────────────┐
│  1. QUERY CLASSIFICATION            │
│  • Fetch context from FAISS         │
│  • LLM decides: index/general/search│
└──────────────┬──────────────────────┘
               │
    ┌──────────┴──────────┐
    │  Route = "index"    │
    ▼                     ▼
┌───────────────┐   Route = "general" → Ollama → END
│  2. RETRIEVAL │   Route = "search"  → Tavily → Generate → END
│  ReAct Agent  │
│  queries FAISS│
└──────┬────────┘
       │
       ▼
┌─────────────────┐
│  3. GRADING     │
│  Is retrieved   │
│  context        │
│  relevant?      │
└──────┬──────────┘
       │
  ┌────┴────┐
  │         │
 YES        NO
  │         │
  ▼         ▼
Generate  Rewrite Query → Back to Retrieval
  │
  ▼
┌─────────────────┐
│  4. GENERATION  │
│  Format final   │
│  answer for     │
│  the user       │
└──────┬──────────┘
       │
       ▼
    Response
```

---

## ✨ Key Features

### 🧠 Intelligent Query Routing
Three-way classification ensures every query hits the most appropriate pipeline — no manual configuration needed.

### 📚 Advanced RAG Pipeline
- Semantic chunking with overlap for context continuity
- FAISS vector similarity search (locally hosted)
- Automatic **query rewriting** when retrieval quality is poor
- **Relevance grading** before generating a response
- Context-aware, human-readable response generation

### 🤖 ReAct Agent Architecture
The retriever node uses the **ReAct (Reason + Act)** paradigm via LangChain's agent executor — it reasons about which tool to call and iterates if needed.

### 🏠 Fully Local Stack
No tokens billed. No data sent to the cloud. Everything runs on your machine.

### 🧠 Hardware-Adaptive Model Selection

The system reads your available RAM and picks the right model automatically:

```python
if ram < 6GB:
    model = "phi3:mini"
elif ram < 10GB:
    model = "qwen2.5:3b"
else:
    model = "qwen3.5:9b"   # ← default for 10GB+ machines
```

Override anytime via `.env`.

### 💾 Persistent Chat Memory
Conversation history is stored in **MongoDB** per session — restart the server and pick up exactly where you left off.

---

## 🧰 Full Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **LLM** | Ollama (Qwen / Phi) | Local inference |
| **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` | Semantic encoding |
| **Vector Store** | FAISS | Document similarity search |
| **Orchestration** | LangGraph | Agentic graph workflows |
| **Agent** | LangChain ReAct | Tool-using reasoning loop |
| **Backend** | FastAPI + Uvicorn | REST API server |
| **Frontend** | Streamlit | Chat UI |
| **Memory** | MongoDB (Motor async) | Persistent chat history |
| **Web Search** | Tavily | Real-time retrieval (optional) |

---

## 📦 Project Structure

```
cortex-rag/
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py              # POST /rag/query, /rag/documents/upload
│   │
│   ├── config/
│   │   ├── prompts.yaml           # All LLM prompt templates
│   │   └── settings.py            # Pydantic settings loader
│   │
│   ├── core/
│   │   ├── config.py              # Hardware-adaptive model selection
│   │   └── logger.py              # Centralized logging
│   │
│   ├── db/
│   │   └── mongo_client.py        # Async MongoDB connection
│   │
│   ├── llms/
│   │   └── ollama.py              # Ollama LLM wrapper
│   │
│   ├── memory/
│   │   ├── chat_history_mongo.py  # MongoDB-backed session memory
│   │   └── chathistory_in_memory.py
│   │
│   ├── models/                    # Pydantic schemas
│   │   ├── grade.py
│   │   ├── query_request.py
│   │   ├── route_identifier.py
│   │   ├── state.py               # LangGraph State TypedDict
│   │   └── verification_result.py
│   │
│   ├── rag/
│   │   ├── graph_builder.py       # LangGraph node + edge definitions
│   │   ├── nodes.py               # Node logic (classify, grade, generate…)
│   │   ├── reAct_agent.py         # ReAct agent + executor setup
│   │   ├── retriever_setup.py     # FAISS vectorstore + retriever tool
│   │   └── document_upload.py     # PDF/TXT ingestion pipeline
│   │
│   ├── tools/
│   │   ├── common_tools.py        # LLM-enhanced description util
│   │   └── graph_tools.py         # Routing + grading edge functions
│   │
│   └── main.py                    # FastAPI app entry point
│
├── streamlit_app/
│   ├── pages/
│   │   └── chat.py                # Main chat interface
│   ├── utils/
│   │   └── api_client.py          # HTTP client for FastAPI
│   └── home.py                    # App entry → redirects to chat
│
├── .env                           # Your local secrets (not committed)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/download) installed and running
- MongoDB running locally (or a free Atlas cluster)
- (Optional) [Tavily API key](https://tavily.com) for web search

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shREKT7/cortex-rag.git
cd cortex-rag
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Pull Your Ollama Models

```bash
# For 10GB+ RAM (recommended)
ollama pull qwen3.5:9b

# For 6–10GB RAM
ollama pull qwen2.5:3b

# For < 6GB RAM
ollama pull phi3:mini
```

### 5️⃣ Configure Your Environment

Create a `.env` file in the project root:

```env
# ── LLM ────────────────────────────────
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen3.5:9b          # override auto-selection if needed

# ── Web Search (optional) ───────────────
TAVILY_API_KEY=your_tavily_key_here

# ── Database ───────────────────────────
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=cortexrag
```

### 6️⃣ Start the Backend

```bash
python -m uvicorn src.main:app --reload
```

API docs available at → `http://localhost:8000/docs`

### 7️⃣ Start the Frontend

```bash
streamlit run streamlit_app/home.py
```

Chat UI available at → `http://localhost:8501`

---

## 🔌 API Reference

### `POST /rag/query`

Send a query to the agentic pipeline.

```bash
curl -X POST http://localhost:8000/rag/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is machine learning?", "session_id": "user_abc"}'
```

**Response:**
```json
{
  "result": {
    "type": "ai",
    "content": "Machine learning is a subset of AI that..."
  }
}
```

---

### `POST /rag/documents/upload`

Upload a PDF or TXT document for indexing.

```bash
curl -X POST http://localhost:8000/rag/documents/upload \
  -H "X-Description: LangGraph tutorial with code examples" \
  -F "file=@my_document.pdf"
```

**Supported formats:** `.pdf`, `.txt`

**What happens internally:**
1. File is loaded and split into 1000-char chunks (150 overlap)
2. LLM enhances your description for the retriever tool
3. Chunks are embedded with `all-MiniLM-L6-v2`
4. Stored in the FAISS vectorstore

---

## 🧪 Example Queries

| Query Type | Example |
|-----------|---------|
| 📚 Document | `"Summarize the uploaded document"` |
| 📚 Document | `"What topics are covered in the file I uploaded?"` |
| 🤖 General | `"What is machine learning?"` |
| 🤖 General | `"Explain the transformer architecture"` |
| 🌐 Search | `"Latest AI research news this week"` |
| 🌐 Search | `"Recent developments in open-source LLMs"` |

---

## 🗺️ Roadmap

- [ ] **Streaming responses** — real-time token streaming to the UI
- [ ] **Hybrid search** — combine FAISS semantic search with BM25 keyword matching
- [ ] **Multi-document indexing** — persistent cross-session document storage (Qdrant integration)
- [ ] **Smarter agent planning** — multi-step tool chaining
- [ ] **Autonomous tool selection** — agent decides which tool without explicit routing
- [ ] **Self-improving retrieval** — feedback loop to improve retrieval quality over time
- [ ] **Answer verification node** — wire the existing `verify_answer` logic into the graph
- [ ] **Streaming chat UI** — progressive response rendering in Streamlit

---

## 🤔 Why CortexRAG?

| Feature | CortexRAG | Typical Cloud RAG |
|--------|-----------|------------------|
| API Cost | ✅ Zero | ❌ Per-token billing |
| Data Privacy | ✅ 100% local | ❌ Data sent to cloud |
| Agentic Routing | ✅ 3-way intelligent routing | ⚠️ Usually single pipeline |
| Query Rewriting | ✅ Auto-retries on bad retrieval | ❌ Rarely included |
| Hardware Adaptive | ✅ Auto model selection | N/A |
| Offline Operation | ✅ Fully offline (sans web search) | ❌ Requires internet |

---

## 👤 Author

**Uzair Teli**
GitHub: [@shREKT7](https://github.com/shREKT7)

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

**If you found this useful, drop a ⭐ on the repo — it helps a lot!**

</div>
