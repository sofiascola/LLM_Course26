from datasets import load_dataset

d = load_dataset("zeroshot/twitter-financial-news-sentiment")


labels = set(d["train"]["label"])
print(f"Etichette uniche: {labels}") 
# 0 = Bearish, 1 = Bullish, 2 = Neutral


print(f"Split disponibili: {d.keys()}")


print(f"Colonne: {d['validation'].column_names}")


print("Esempio di tweet e label:")
print(d["validation"][0])


print(f"Esempi totali (Validation): {len(d['validation'])}")