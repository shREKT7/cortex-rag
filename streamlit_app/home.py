"""
CortexRAG – Main entry point.
Launches directly into the chat interface. No authentication required.
"""

import uuid
import streamlit as st

# Page config
st.set_page_config(
    page_title="CortexRAG – Agentic AI Knowledge Retrieval",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject a unique session ID on first load so MongoDB can track the conversation
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

# Redirect to the chat page
st.switch_page("pages/chat.py")
