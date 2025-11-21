from textSummarizer.components.data_validation import DataValidation
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        status = data_validation.validate_all_files_exist()
        logger.info("Data validation completed")
        logger.info(f"Validation status: {status}")





