from cnn_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnn_classifier import logger


STAGE_NAME = "Data Ingestion stage"

logger.info("We have already downloaded the data. But to check dataingestion pipeline , we are doing this")
try:
    logger.info("<<<<<<<< Data Ingestion Pipeline started >>>>>>>>")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info("<<<<<<<< Data Ingestion Pipeline completed >>>>>>>>")
except Exception as e:
    logger.info(e)
    raise e