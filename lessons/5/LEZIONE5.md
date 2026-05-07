# Lezione 5 — RAG con Ollama e ChromaDB

Pipeline RAG (Retrieval-Augmented Generation) su articoli di notizie recenti.
Confronto diretto tra risposte con e senza contesto.

---

## Setup

```bash
pip install ollama chromadb 
ollama pull gemma2:2b
ollama pull nomic-embed-text
```

---

## Struttura

```
lezione5/
├── config.py              <- modelli, chunk size, modalità
├── chunker.py             <- split del testo in chunk
├── embedder.py            <- trasforma testo in vettori
├── indexer.py             <- carica documento e crea indice
├── retriever.py           <- cerca chunk rilevanti
├── generator.py           <- genera risposte con/senza RAG
├── pipeline.py            <- chat interattiva
├── eval.py                <- valutazione con visualizzazione contesto
├── prompts/
│   └── prompt_templates.py  <- template STRICT, CONVERSATIONAL, CITED, STRUCTURED, MULTILINGUAL
├── dataset/
│   └── dataset_qa.py        <- 21 domande sugli articoli
└── documents/
└── news.txt             <- 7 articoli BBC
```

---

## Utilizzo

**Chat interattiva:**
```bash
python pipeline.py
```

Cambia modalità in `config.py`:
```python
MODE = "rag"     # solo RAG
MODE = "no-rag"  # solo LLM
MODE = "both"    # confronto fianco a fianco
```

**Valutazione con visualizzazione contesto:**
```bash
python eval.py
```

Mostra per ogni domanda: i chunk recuperati, la risposta RAG e la risposta senza RAG.

---

## Cambiare strategia di prompting

Modifica `ACTIVE` in `prompts/prompt_templates.py`:
```python
ACTIVE = STRICT         # risposta solo dal contesto
ACTIVE = CONVERSATIONAL # può integrare con conoscenza generale
ACTIVE = CITED          # aggiunge citazione della fonte
ACTIVE = STRUCTURED     # risposta strutturata con livello di confidenza
ACTIVE = MULTILINGUAL   # risponde in italiano
```