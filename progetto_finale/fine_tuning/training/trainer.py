# training/trainer.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import (
    OUTPUT_DIR,
    EPOCHS,
    TRAIN_BATCH_SIZE,
    EVAL_BATCH_SIZE,
    LEARNING_RATE,
    EVAL_STRATEGY,
    SAVE_STRATEGY,
    LOGGING_STEPS,
    SEED,
)

from transformers import TrainingArguments, Trainer, DataCollatorWithPadding


def build_training_args():
    """
    Configura gli iperparametri del training.
    Tutto viene da config.py — nessun numero hardcoded qui.
    """
    return TrainingArguments(
        output_dir=OUTPUT_DIR,
        

        num_train_epochs=EPOCHS,
        

        per_device_train_batch_size=TRAIN_BATCH_SIZE,
       

        per_device_eval_batch_size=EVAL_BATCH_SIZE,
       
        learning_rate=LEARNING_RATE,
      
        eval_strategy=EVAL_STRATEGY,
     

        save_strategy=SAVE_STRATEGY,
        

        save_total_limit = 2,
        

        load_best_model_at_end=True,
        

        logging_steps=LOGGING_STEPS,
       

        seed=SEED,
        
    )


def build_trainer(model, tokenized_dataset, tokenizer, compute_metrics):
    
    training_args = build_training_args()

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["validation"],
        compute_metrics=compute_metrics,
        data_collator=data_collator,
    )

    return trainer



# Test 


if __name__ == "__main__":
    args = build_training_args()
    print(f"Output dir:      {args.output_dir}")
    print(f"Epoche:          {args.num_train_epochs}")
    print(f"Batch size:      {args.per_device_train_batch_size}")
    print(f"Learning rate:   {args.learning_rate}")
    print(f"Eval strategy:   {args.eval_strategy}")