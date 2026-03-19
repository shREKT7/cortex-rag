"""
Ollama LLM initialization with hardware-adaptive model selection.

Priority:
  1. Use OLLAMA_MODEL from .env if explicitly set.
  2. Otherwise auto-select based on available system RAM via psutil:
       < 6 GB  → phi3:mini
       6–10 GB → qwen2.5:3b
       > 10 GB → qwen3.5:9b
"""

import os

import psutil
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()


def _select_model() -> str:
    """Return the model name based on available RAM, unless overridden by .env."""
    env_model = os.getenv("OLLAMA_MODEL", "").strip()
    if env_model:
        return env_model

    available_gb = psutil.virtual_memory().available / (1024 ** 3)

    if available_gb < 6:
        chosen = "phi3:mini"
    elif available_gb <= 10:
        chosen = "qwen2.5:3b"
    else:
        chosen = "qwen3.5:9b"

    print(
        f"[CortexRAG] Available RAM: {available_gb:.1f} GB → auto-selected model: {chosen}"
    )
    return chosen


llm = ChatOllama(
    model=_select_model(),
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    temperature=0,
)
