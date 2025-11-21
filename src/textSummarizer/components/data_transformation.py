import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset
from textSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(
            example_batch['dialogue'],
            max_length=1024,
            truncation=True
        )
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(
                example_batch['summary'],
                max_length=128,
                truncation=True
            )
        
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        # Load CSV files properly
        dataset_samsum = load_dataset(
            "csv",
            data_files={
                "train": os.path.join(self.config.data_path, "train.csv"),
                "validation": os.path.join(self.config.data_path, "validation.csv"),
                "test": os.path.join(self.config.data_path, "test.csv"),
            }
        )

        # Map tokenizer
        dataset_samsum_pt = dataset_samsum.map(
            self.convert_examples_to_features,
            batched=True
        )

        # Save as HF dataset
        save_path = os.path.join(self.config.root_dir, "samsum_dataset")
        dataset_samsum_pt.save_to_disk(save_path)

        logger.info(f"Data transformation completed. Dataset saved to {save_path}")
