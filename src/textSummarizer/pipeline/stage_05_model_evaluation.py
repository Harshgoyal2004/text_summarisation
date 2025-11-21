from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def run(self):
        config_manager = ConfigurationManager()
        model_evaluation_config = config_manager.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.evaluate()
        logger.info(f"Model evaluation completed")

