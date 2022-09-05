from packagePrediction.config.configuration import Configuartion
from packagePrediction.pipeline.pipeline import Pipeline
from packagePrediction.constant import CONFIG_DIR

config = Configuartion()
pipeline = Pipeline(config=config)

pipeline.run_pipeline()