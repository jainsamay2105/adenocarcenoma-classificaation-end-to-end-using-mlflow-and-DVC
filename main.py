from cnn_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnn_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnn_classifier import logger


STAGE_NAME = "Data Ingestion stage"

logger.info("We have already downloaded the data. But to check dataingestion pipeline , we are doing this")
try:
    logger.info(f"<<<<<<<< {STAGE_NAME} started >>>>>>>>")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"<<<<<<<< {STAGE_NAME} completed >>>>>>>>")
except Exception as e:
    logger.info(e)
    raise e



STAE_NAME = 'Prepare Base Model'

logger.info('We have already preepared our base model. But to check prepare_base_model pipeline , we are doing this...')
try:
    logger.info(f"<<<<<<<< {STAGE_NAME} started >>>>>>>>")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f"<<<<<<<< {STAGE_NAME} completed >>>>>>>>")
except Exception as e:
    logger.info(e)
    raise e