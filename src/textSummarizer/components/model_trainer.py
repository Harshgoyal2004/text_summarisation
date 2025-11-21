import os
from transformers import TrainingArguments, Trainer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import DataCollatorForSeq2Seq
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import ModelTrainerConfig
import torch

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)

        # Data collator
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        # FIXED: Correct dataset path
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # Training arguments
        trainer_args = TrainingArguments(
            **self.config.training_args,
            output_dir=self.config.root_dir,
            report_to="none",      # Important for Kaggle (prevents WandB crash)
            predict_with_generate=True
        )

        # Trainer setup
        trainer = Trainer(
            model=model,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["train"],
            eval_dataset=dataset_samsum_pt["validation"],
        )

        # Train
        trainer.train()

        # Save model + tokenizer properly
        model.save_pretrained(os.path.join(self.config.root_dir, "model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))

        
