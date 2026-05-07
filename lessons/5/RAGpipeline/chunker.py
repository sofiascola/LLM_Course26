# chunker.py
# Divide un testo in chunk di dimensione fissa con sovrapposizione.

from config import CHUNK_SIZE, CHUNK_OVERLAP


def split_in_chunks(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list:
    """
    Divide il testo in chunk di dimensione fissa con sovrapposizione.

    Parametri:
        text -> il testo da dividere
        size -> lunghezza massima di ogni chunk in caratteri
        overlap -> quanti caratteri condividere tra chunk adiacenti

    Perché la sovrapposizione?
    Evita di tagliare un concetto a metà: se una frase inizia
    alla fine di un chunk, il chunk successivo la ripete all'inizio.

    Esempio con size=20, overlap=5:
        testo:   "The cat sat on the mat and the dog slept"
        chunk 1: "The cat sat on the m"
        chunk 2: "he mat and the dog s" ripete "he m" dall'overlap
        chunk 3: "dog slept"
    """
    chunks = []
    start  = 0

    while start < len(text):
        end   = start + size
        chunk = text[start:end]
        chunks.append(chunk)
        start += size - overlap

    return chunks


if __name__ == "__main__":
    testo_prova = "The cat sat on the mat. " * 20
    chunks = split_in_chunks(testo_prova)

    print(f"Testo: {len(testo_prova)} caratteri")
    print(f"Chunk: {len(chunks)}")
    print(f"\nPrimo chunk:\n{chunks[0]}")
    print(f"\nSecondo chunk (nota l'overlap):\n{chunks[1]}")