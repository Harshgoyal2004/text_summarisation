import os
from pathlib import Path
from transformers import TrainingArguments, Trainer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import DataCollatorForSeq2Seq
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import ModelTrainerConfig
import torch
from textSummarizer.logging import logger

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    def _is_model_trained(self):
        """Check if model and tokenizer already exist in the output directory."""
        # Check for model in the expected directory structure
        model_dir = Path(self.config.root_dir) / "pegasus_summarizer"
        if model_dir.exists():
            # Check for required model files
            required_files = [
                'config.json',
                'model.safetensors',
                'tokenizer_config.json',
                'special_tokens_map.json',
                'tokenizer.json',
                'spiece.model',
                'generation_config.json'
            ]
            return all((model_dir / file).exists() for file in required_files)
        return False

    def train(self):
        # Check if model is already trained
        if self._is_model_trained():
            logger.info(f"Model already exists at {self.config.root_dir}. Skipping training.")
            return

        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Starting model training on device: {device}")

        # Create output directory if it doesn't exist
        os.makedirs(self.config.root_dir, exist_ok=True)

        try:
            # Check if we have a local model
            local_model_path = Path(self.config.root_dir) / "pegasus_summarizer"
            
            if local_model_path.exists():
                logger.info(f"Loading model from local directory: {local_model_path}")
                tokenizer = AutoTokenizer.from_pretrained(str(local_model_path))
                model = AutoModelForSeq2SeqLM.from_pretrained(str(local_model_path)).to(device)
            else:
                logger.info(f"Downloading model from {self.config.model_ckpt}")
                tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
                model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)

            # Data collator
            seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

            # Load dataset
            logger.info(f"Loading dataset from {self.config.data_path}")
            dataset_samsum_pt = load_from_disk(self.config.data_path)

            # Training arguments
            trainer_args = TrainingArguments(
                **self.config.training_args,
                output_dir=self.config.root_dir,
                report_to="none",  # Prevents WandB crash
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
            logger.info("Starting model training...")
            trainer.train()

            # Save model + tokenizer
            output_dir = Path(self.config.root_dir) / "pegasus_summarizer"
            output_dir.mkdir(parents=True, exist_ok=True)
            
            logger.info(f"Saving model and tokenizer to {output_dir}")
            model.save_pretrained(output_dir)
            tokenizer.save_pretrained(output_dir)
            
            logger.info("Model training and saving completed successfully")
            
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise

        
