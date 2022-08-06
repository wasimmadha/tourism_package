import os
import sys

from packagePrediction.config.configuration import Configuartion
from packagePrediction.exception import PackageException
from packagePrediction.logger import logging
from packagePrediction.entity.config_entity import DataIngestionConfig, DataValidationConfig
from packagePrediction.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact
from packagePrediction.components.data_ingestion import DataIngestion
from packagePrediction.components.data_validation import DataValidation
from packagePrediction.components.data_transformation import DataTransformation

class Pipeline():
    def __init__(self, config: Configuartion ) -> None:
        try:
            os.makedirs(config.training_pipeline_config.artifact_dir, exist_ok=True)
            self.config = config
        except Exception as e:
            raise PackageException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise PackageException(e, sys) from e

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) \
            -> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
                                             )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise PackageException(e, sys) from e

    def start_data_transformation(self,
                                  data_ingestion_artifact: DataIngestionArtifact,
                                  data_validation_artifact: DataValidationArtifact
                                  ) -> DataTransformationArtifact:
        try:
            data_transformation = DataTransformation(
                data_transformation_config=self.config.get_data_transformation_config(),
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact
            )
            return data_transformation.initiate_data_transformation()
        except Exception as e:
            raise PackageException(e, sys)

    def run_pipeline(self):
        try:
            # data ingestion
            logging.info("Pipeline starting.")
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact
            )
            logging.info("Pipeline Finished.")
        except Exception as e:
            raise PackageException(e, sys) from e
