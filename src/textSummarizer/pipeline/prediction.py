from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
import torch

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        
    def predict(self, text):
        # Get model path from config
        model_path = self.config.config.model_trainer.model_ckpt
        
        # Set device
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(device)
        
        # Set up generation parameters
        gen_kwargs = {
            "length_penalty": 0.8,
            "num_beams": 8,
            "max_length": 128,
            "min_length": 30,
            "no_repeat_ngram_size": 3
        }
        
        # Create pipeline
        pipe = pipeline(
            "summarization",
            model=model,
            tokenizer=tokenizer,
            device=0 if device == "cuda" else -1
        )
        
        print("\nDialogue:")
        print(text)
        
        # Generate summary
        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        
        print("\nSummary:")
        print(output)
        
        return output