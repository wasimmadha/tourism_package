from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig", ["raw_data_dir","ingested_train_dir","ingested_test_dir"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])
