# 🧠 CortexRAG – Local Agentic AI Knowledge Retrieval System

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-orange)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> 🚀 Fully local, agentic Retrieval-Augmented Generation (RAG) system with intelligent query routing across documents, LLM reasoning, and real-time web search.

---

## 📌 Overview

**CortexRAG** is a **local-first agentic AI system** that dynamically routes user queries through multiple pipelines:

- 📚 Document Retrieval (RAG)
- 🤖 General LLM Reasoning
- 🌐 Real-time Web Search

Built using **LangGraph workflows + Ollama LLMs**, the system operates **entirely offline (except optional web search)** — eliminating dependency on paid APIs.

---

## 🎯 Key Features

### 🧠 Intelligent Query Routing
Automatically classifies queries into:
- **Index** → Uses uploaded documents
- **General** → Uses LLM knowledge
- **Search** → Uses real-time web search

---

### 📚 Advanced RAG Pipeline
- Semantic chunking & embedding
- FAISS-based vector similarity search
- Query rewriting for better retrieval
- Relevance grading of documents
- Context-aware response generation

---

### 🤖 Agentic AI Architecture
Powered by **LangGraph multi-node workflows**:

- Query Analysis
- Query Classification
- Retriever Node
- Web Search Tool
- ReAct Agent Reasoning
- Response Generator

Implements the **ReAct (Reason + Act)** paradigm.

---

### 🧠 Fully Local AI Stack
No OpenAI. No paid APIs. Fully local.

| Component        | Technology                  |
|----------------|---------------------------|
| LLM            | Ollama                    |
| Models         | Qwen / Phi                |
| Embeddings     | sentence-transformers     |
| Vector Store   | FAISS                     |
| Orchestration  | LangGraph                 |
| Backend        | FastAPI                   |
| Frontend       | Streamlit                 |
| Memory         | MongoDB                   |
| Web Search     | Tavily (optional)         |

---

### ⚡ Hardware-Adaptive Model Selection

Automatically selects model based on RAM:

| RAM Available | Model Used        |
|--------------|------------------|
| < 6GB        | phi3:mini        |
| 6–10GB       | qwen2.5:3b       |
| > 10GB       | qwen3.5:9b       |

Override via `.env` if needed.

---

## 🏗️ Architecture
User
↓
Streamlit UI
↓
FastAPI Backend
↓
LangGraph Agent
├── Query Classifier
├── Retriever (FAISS)
├── Web Search (Tavily)
└── General LLM (Ollama)
↓
Response Generator
↓
User


---

## 📦 Project Structure
cortex-rag/
│
├── src/ # Core backend logic
│ ├── main.py # FastAPI entry point
│ ├── api/ # API routes
│ ├── core/ # Config & logging
│ ├── db/ # MongoDB client
│ ├── llms/ # Ollama integration
│ ├── memory/ # Chat history
│ ├── models/ # Data schemas
│ ├── rag/ # RAG pipeline
│ └── tools/ # Utility tools
│
├── streamlit_app/ # Frontend UI
│ ├── home.py
│ └── pages/chat.py
│
├── requirements.txt
├── README.md
└── .gitignore


---

## 🔌 API Endpoints

### ➤ Query
```http
POST /rag/query
{
  "query": "What is machine learning?",
  "session_id": "test_session"
}

➤ Upload Document
POST /rag/documents/upload
curl -X POST http://localhost:8000/rag/documents/upload \
-H "X-Description: Sample document" \
-F "file=@document.pdf"

Supported formats:

- PDF
- TXT

📖 Installation
1️⃣ Clone Repo
git clone https://github.com/shREKT7/cortex-rag.git
cd cortex-rag

2️⃣ Setup Environment

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install Ollama

👉 https://ollama.com/download

5️⃣ Download Models
ollama pull qwen3.5:9b

ollama pull phi3:mini

6️⃣ Configure Environment
Create a .env file in the project root:

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen3.5:9b

TAVILY_API_KEY=your_api_key_here

MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=cortexrag

🚀 Run the Project
Backend
python -m uvicorn src.main:app --reload

Docs:
http://localhost:8000/docs

Frontend
streamlit run streamlit_app/home.py

UI:
http://localhost:8501

🧪 Example Queries
General

What is machine learning?

Explain transformers in AI

Documents

Summarize the uploaded document

What topics are covered?

Search

Latest AI research news

Recent developments in LLMs

📊 Why CortexRAG?

✔ Fully local LLM system
✔ Zero API cost
✔ Agentic reasoning workflows
✔ Modular architecture
✔ Extensible tool integration
✔ Document-aware conversations

🚀 Roadmap

 Streaming responses

 Hybrid search (FAISS + BM25)

 Multi-document indexing

 Smarter agent planning

 Autonomous tool selection

 Self-improving retrieval

👤 Author

Uzair Teli
GitHub: https://github.com/shREKT7

📜 License

MIT License



