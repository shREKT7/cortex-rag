# CortexRAG – Local Agentic AI Knowledge Retrieval System

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20Workflow-orange.svg)](https://python.langchain.com/langgraph/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black.svg)](https://ollama.com/)

---

# 🧠 CortexRAG

CortexRAG is a **fully local agentic Retrieval-Augmented Generation (RAG) system** that intelligently routes user queries across:

• Document retrieval  
• General LLM reasoning  
• Real-time web search  

The system is powered by **LangGraph agent workflows** and runs **entirely locally using Ollama models**, eliminating the need for paid LLM APIs.

This architecture enables **context-aware responses, document reasoning, and tool-based decision making**.

---

# 🎯 Key Features

## 🧠 Intelligent Query Routing

Automatically classifies queries and routes them to the correct processing pipeline.

Three query types:

| Type | Description |
|-----|-------------|
| **Index** | Answer using uploaded documents |
| **General** | Answer using LLM knowledge |
| **Search** | Perform real-time web search |

---

# 📚 Advanced RAG Pipeline

• Intelligent document chunking  
• Semantic embeddings using sentence-transformers  
• Vector similarity search via FAISS  
• Relevance grading of retrieved documents  
• Query rewriting for improved retrieval  
• Context-aware answer generation  

---

# 🤖 Agentic AI Architecture

CortexRAG uses **LangGraph agent orchestration** implementing a multi-node reasoning workflow.

Core nodes include:

• Query analysis  
• Query classification  
• Retriever  
• Web search tool  
• ReAct agent reasoning  
• Response generation  

This follows the **ReAct (Reason + Act) agent pattern**.

---

# 🧠 Fully Local AI Stack

Unlike typical RAG systems, CortexRAG runs **entirely locally**.

| Component | Technology |
|-----------|------------|
| LLM | Ollama |
| Models | Qwen / Phi |
| Embeddings | sentence-transformers |
| Vector Store | FAISS |
| Workflow Engine | LangGraph |
| Backend API | FastAPI |
| UI | Streamlit |
| Chat Memory | MongoDB |
| Web Search | Tavily |

No OpenAI or external LLM APIs are required.

---

# ⚡ Hardware-Adaptive LLM Selection

CortexRAG automatically selects the best model based on available RAM.

| Available RAM | Selected Model |
|---------------|---------------|
| < 6GB | phi3:mini |
| 6-10GB | qwen2.5:3b |
| >10GB | qwen3.5:9b |

Users can override this manually using `.env`.

---

# 🏗 System Architecture


User
↓
Streamlit UI
↓
FastAPI Backend
↓
LangGraph Agent

├── Query Classifier
│
├── Document Retriever (FAISS)
│
├── Web Search Tool (Tavily)
│
└── General LLM Reasoning (Ollama)

↓
Response Generator
↓
User


---

# 📦 Project Structure


cortex-rag/

src/
├── main.py
├── api/
│ └── routes.py
│
├── core/
│ ├── config.py
│ └── logger.py
│
├── db/
│ └── mongo_client.py
│
├── llms/
│ └── ollama.py
│
├── memory/
│ ├── chat_history_mongo.py
│ └── chathistory_in_memory.py
│
├── models/
│ ├── state.py
│ ├── query_request.py
│ └── route_identifier.py
│
├── rag/
│ ├── graph_builder.py
│ ├── retriever_setup.py
│ ├── document_upload.py
│ └── reAct_agent.py
│
└── tools/
├── common_tools.py
└── graph_tools.py

streamlit_app/
├── home.py
└── pages/
└── chat.py

requirements.txt
README.md


---

# 🔌 API Endpoints

Base URL:


http://localhost:8000


---

## Query Endpoint


POST /rag/query


Example request:

```json
{
  "query": "What is machine learning?",
  "session_id": "test_session"
}

Response:

{
  "result": {
    "content": "Machine learning is..."
  }
}
Upload Document
POST /rag/documents/upload

Example:

curl -X POST http://localhost:8000/rag/documents/upload \
-H "X-Description: Sample document about AI" \
-F "file=@document.pdf"

Supported file types:

• PDF
• TXT

📖 Installation
1 Clone Repository
git clone https://github.com/shREKT7/cortex-rag.git
cd cortex-rag
2 Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
3 Install Dependencies
pip install -r requirements.txt
Install Ollama

Download from:

https://ollama.com/download

Install LLM Models

Recommended models:

ollama pull qwen2.5:3b
ollama pull qwen3.5:9b
ollama pull phi3:mini
Environment Configuration

Create .env

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen3.5:9b

TAVILY_API_KEY=your_api_key_here

MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=cortexrag
🚀 Running the System

Start FastAPI backend:

python -m uvicorn src.main:app --reload

API docs:

http://localhost:8000/docs

Start Streamlit UI:

streamlit run streamlit_app/home.py

Open UI:

http://localhost:8501
🧪 Example Queries

General knowledge:

What is machine learning?
Explain transformers in AI.

Document questions:

What topics are discussed in the uploaded document?
Summarize the document.

Search queries:

Latest AI research news.
Recent developments in large language models.
🔧 Technology Stack
Component	Technology
LLM	Ollama
Models	Qwen / Phi
Embeddings	sentence-transformers
Vector Store	FAISS
Workflow Engine	LangGraph
Backend	FastAPI
UI	Streamlit
Chat Memory	MongoDB
Web Search	Tavily
📊 Advantages of CortexRAG

✔ Fully local LLM inference
✔ No API costs
✔ Agentic reasoning workflows
✔ Modular RAG architecture
✔ Document-aware conversations
✔ Easily extensible tools

🚀 Future Improvements

Planned upgrades:

• Streaming responses
• Hybrid search (vector + BM25)
• Multi-document indexing
• Better agent planning
• Autonomous tool selection
• Self-improving retrieval pipelines

👤 Author

Uzair Teli

GitHub
[text](https://github.com/shREKT7)

📜 License

MIT License