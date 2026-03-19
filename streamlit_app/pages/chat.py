"""
CortexRAG – Chat interface page.
Sends queries to the FastAPI backend and displays streamed responses.
"""

import uuid
import streamlit as st

from utils.api_client import query_backend, document_upload_rag

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CortexRAG – Chat",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": None,
        "Report a Bug": None,
        "About": "CortexRAG – Agentic AI Knowledge Retrieval System",
    },
)

# ── Session bootstrap ─────────────────────────────────────────────────────────
# Ensure a session_id exists even if users land directly on this page
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = {}

# ── Sidebar – Document upload ─────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🧠 CortexRAG")
    st.caption(f"Session: `{st.session_state['session_id'][:8]}…`")
    st.divider()

    st.header("📂 Upload Documents")
    uploaded_file = st.file_uploader(
        "Upload a PDF or TXT file",
        type=["pdf", "txt"],
        help="Documents are embedded locally using sentence-transformers.",
    )

    if uploaded_file:
        file_description = st.text_input(
            "📄 Describe your document (required)",
            max_chars=300,
            placeholder="E.g. LangGraph tutorial with workflows and code examples",
        )

        file_key = f"{uploaded_file.name}_{file_description}"

        if file_description:
            if file_key not in st.session_state.uploaded_files:
                with st.spinner("Embedding document…"):
                    success = document_upload_rag(uploaded_file, file_description)
                if success:
                    st.success(f"✅ Uploaded: {uploaded_file.name}")
                    st.session_state.uploaded_files[file_key] = True
                else:
                    st.error(f"❌ Upload failed: {uploaded_file.name}")
            else:
                st.info(f"Already indexed: {uploaded_file.name}")
        else:
            st.warning("Please describe your document before uploading.")

    st.divider()
    st.markdown("**Stack**")
    st.markdown(
        "🤖 LLM: `qwen3.5:9b` (Ollama)\n\n"
        "🔍 Embeddings: `all-MiniLM-L6-v2`\n\n"
        "🗄️ Vector DB: FAISS\n\n"
        "💾 Memory: MongoDB"
    )

    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# ── Main chat area ────────────────────────────────────────────────────────────
st.title("💬 CortexRAG – Agentic Chat")
st.caption("Powered by LangGraph · Ollama · FAISS · MongoDB")

# Render existing chat messages
for role, text in st.session_state.chat_history:
    st.chat_message(role).write(text)

# Handle new user input
user_input = st.chat_input("Ask a question…")
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            response = query_backend(user_input, st.session_state["session_id"])
        st.write(response)

    st.session_state.chat_history.append(("assistant", response))
