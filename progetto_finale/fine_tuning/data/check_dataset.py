from datasets import load_dataset

# 1. Caricamento del dataset specifico per news finanziarie
d = load_dataset("zeroshot/twitter-financial-news-sentiment")

# 2. Estrazione delle etichette (Sentiment: 0, 1, 2)
# label_binary qui diventa semplicemente 'label'
labels = set(d["train"]["label"])
print(f"Etichette uniche: {labels}") 
# Nota: 0 = Bearish, 1 = Bullish, 2 = Neutral

# 3. Chiavi del dataset (mostra train e validation)
print(f"Split disponibili: {d.keys()}")

# 4. Nomi delle colonne nello split di validazione
print(f"Colonne: {d['validation'].column_names}")

# 5. Esempio del primo elemento del validation set
print("Esempio di tweet e label:")
print(d["validation"][0])

# 6. Numero totale di esempi nel set di validazione
print(f"Esempi totali (Validation): {len(d['validation'])}")