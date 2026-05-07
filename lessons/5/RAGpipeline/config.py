# config.py

# ── modelli ───────────────────────────────────────────────────────
MODEL_LLM       = "gemma2:2b"
MODEL_EMBEDDING = "nomic-embed-text"

# ── documento ─────────────────────────────────────────────────────
DOCUMENT_PATH = "documents/news.txt"

# ── chunking ──────────────────────────────────────────────────────
CHUNK_SIZE    = 500   # caratteri per chunk
CHUNK_OVERLAP = 50    # caratteri di sovrapposizione tra chunk adiacenti

# ── retrieval ─────────────────────────────────────────────────────
N_RESULTS = 3         # quanti chunk recuperare per ogni domanda

# ── modalità pipeline ─────────────────────────────────────────────
MODE = "both"
# opzioni:
#   "rag" -> risposta solo con RAG
#   "no-rag" -> risposta solo senza RAG
#   "both" -> confronto fianco a fianco