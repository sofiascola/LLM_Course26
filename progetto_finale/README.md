# Progetto finale
Scola Sofia

# Parte 1: fine-tuning 
- Modello scelto: DistilBERT, ideale per operare su testi brevi come i tweet
- Dataset scelto: dataset di financial tweets già etichettati, meno banale data la complessità del linguaggio
- Risultati ottenuti:
   - Accuracy finale: training 1: 0.8756, training 2: 0.8664
   - Loss:
       - training 1: loss decrescente e stabile,
       - training 2: loss crescente a partire dall'epoca 2, suggerendo difficoltà di convergenza.
   - Iperparametri: learning rate 2e-5 e 5e-5, epoche 3/4

 # Parte 2: Pipeline Ollama
- Task scelto: classificazione sentiment per confrontare fine-tuning e prompt engineering
- Strategie utilizzate:
    - Zero-shot
    - Few-shot
- Esempi di input/output:
    - Input: "Fed keeps rates unchanged, markets react with stability."
    - Output (Few-shot): NEUTRAL
    - Output (Zero-shot): "The sentiment of the tweet is neutral because..."
- Considerazioni sui risultati: accuracy di entrambe le strategie del 100%, il modello ha dimostrato di saper interpretare correttamente la terminologia. 
