# prompts/prompt_templates.py
# Template di prompts.
# Cambia TEMPLATE_NAME in pipeline.py per provare strategie diverse.

# ------------------------------------------------------------------
# Template disponibili
# ------------------------------------------------------------------

STRICT = """Answer the question using ONLY the information provided in the context below.
If the answer is not in the context, say exactly: "I don't have information about this in the provided documents."
Do not use any knowledge outside of the context.

Context:
{context}

Question: {question}

Answer:"""
# uso: risposta fedele al documento, nessuna creatività
# ideale per: Q&A su documenti aziendali, compliance, citazioni


CONVERSATIONAL = """You are a helpful assistant. Use the context below to answer the question.
If the context doesn't contain enough information, say so and answer based on your general knowledge.

Context:
{context}

Question: {question}

Answer:"""
# uso: risposta più naturale, può integrare con conoscenza generale
# ideale per: chatbot, assistenti generici


CITED = """Answer the question based on the context below.
After your answer, add a line starting with "Source:" that quotes the exact sentence from the context you used.
If the answer is not in the context, say "I don't have information about this in the provided documents."

Context:
{context}

Question: {question}

Answer:
Source:"""
# uso: risposta con citazione della fonte
# ideale per: giornalismo, ricerca, verifica delle informazioni


STRUCTURED = """You are an expert analyst. Based only on the context provided, answer the question.
Format your response as:
Summary: <one sentence answer>
Details: <more detailed explanation if available>
Confidence: <HIGH if clearly stated in context / LOW if inferred>

Context:
{context}

Question: {question}"""
# uso: risposta strutturata e con indicazione della confidenza
# ideale per: analisi, report, decision making


MULTILINGUAL = """Rispondi alla domanda usando SOLO le informazioni nel contesto fornito.
Se la risposta non è nel contesto, dì esattamente: "Non ho informazioni su questo nei documenti forniti."
Rispondi sempre in italiano, anche se il contesto è in inglese.

Contesto:
{context}

Domanda: {question}

Risposta:"""
# uso: risposta in italiano anche su documenti in inglese


# ------------------------------------------------------------------
# Template attivo — cambia questo per usare un template diverso
# ------------------------------------------------------------------

ACTIVE = STRICT
# opzioni: STRICT, CONVERSATIONAL, CITED, STRUCTURED, MULTILINGUAL


# ------------------------------------------------------------------
# Funzione di rendering
# ------------------------------------------------------------------

def render(context: str, question: str) -> str:
    """
    Riempie il template attivo con contesto e domanda.

    Uso:
        from prompt_templates import render
        prompt = render(context, question)
    """
    return ACTIVE.format(context=context, question=question)


if __name__ == "__main__":
    # mostra tutti i template disponibili
    templates = {
        "STRICT":        STRICT,
        "CONVERSATIONAL": CONVERSATIONAL,
        "CITED":         CITED,
        "STRUCTURED":    STRUCTURED,
        "MULTILINGUAL":  MULTILINGUAL,
    }

    print(f"Template attivo: {[k for k, v in templates.items() if v == ACTIVE][0]}\n")
    print("Template disponibili:")
    for name in templates:
        print(f"  - {name}")

    print("\n--- Esempio di prompt renderizzato (ACTIVE) ---")
    esempio = render(
        context="Project Freedom was announced by Trump on Sunday.",
        question="When was Project Freedom announced?"
    )
    print(esempio)