import re
from collections import Counter
from typing import List
from data import get_dataset

class SimpleTokenizer:
    PAD = "[PAD]"
    UNK = "[UNK]"
    CLS = "[CLS]"

    def __init__(self):
        self.vocab = {}
        self.inv_vocab = {}

    def _tokenize(self, text: str) -> List[str]:
        text = text.lower()
        text = re.sub(r"([,.!?;:()\"\-])", r" \1 ", text)
        tokens = [t for t in text.split() if t]
        return tokens

    def build_vocab(self, texts: List[str], max_vocab: int = 10000) -> None:
        token_freq = Counter()
        for text in texts:
            tokens = self._tokenize(text)
            token_freq.update(tokens)

        most_common = token_freq.most_common(max_vocab - 3)
        self.vocab = {self.PAD: 0, self.UNK: 1, self.CLS: 2}
        
        for i, (token, _) in enumerate(most_common, start=3):
            self.vocab[token] = i
        
        self.inv_vocab = {v: k for k, v in self.vocab.items()}

    def encode(self, text: str) -> List[int]:
        tokens = self._tokenize(text)
        # Se il token non esiste, usiamo l'ID di [UNK] (che è 1)
        return [self.vocab.get(t, self.vocab[self.UNK]) for t in tokens]

    def decode(self, ids: List[int]) -> str:
        # Trasforma gli ID in parole usando il vocabolario inverso
        return " ".join([self.inv_vocab.get(i, self.UNK) for i in ids])

# --- IL TEST SCRIPT DEVE ESSERE FUORI DALLA CLASSE (INDENTAZIONE ZERO) ---
if __name__ == "__main__":
    # 1. Caricamento del dataset reale
    print("Caricamento del dataset in corso...")
    dataset = get_dataset()
    train_texts = dataset['train']['text']
    
    # 2. Inizializzazione e building del vocabolario
    tok = SimpleTokenizer()
    print(f"Costruzione del vocabolario su {len(train_texts)} tweet...")
    tok.build_vocab(train_texts, max_vocab=5000)

    print("-" * 30)
    print(f"Vocabolario creato: {len(tok.vocab)} token")
    print(f"Esempio primi 10 token: {list(tok.vocab.items())[:10]}")
    print("-" * 30)

    # 3. Test di codifica
    frase_test = "The stock market is bullish today!"
    ids = tok.encode(frase_test)
    
    print(f"Test frase: '{frase_test}'")
    print(f"IDs: {ids}")
    print(f"Decodifica: '{tok.decode(ids)}'")
    print("-" * 30)

    # 4. Test con parole fuori vocabolario
    frase_unk = "Bitcoin skyrocketing with hyper-growth"
    ids_unk = tok.encode(frase_unk)
    
    print(f"Test parola sconosciuta: '{frase_unk}'")
    print(f"IDs (con UNK): {ids_unk}")
    print(f"Decodifica: '{tok.decode(ids_unk)}'")