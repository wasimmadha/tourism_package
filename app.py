from unittest import result
from flask import Flask, request
import sys, os
from packagePrediction import pipeline
from packagePrediction.entity import package_predictor
from packagePrediction.exception import PackageException
from packagePrediction.components.data_ingestion import DataIngestion
from packagePrediction.config.configuration import Configuartion
from packagePrediction.pipeline.pipeline import Pipeline
from packagePrediction.constant import CONFIG_DIR

app = Flask(__name__)

ROOT_DIR = os.getcwd()
LOG_FOLDER_NAME = "logs"
PIPELINE_FOLDER_NAME = "housing"
SAVED_MODELS_DIR_NAME = "saved_models"
MODEL_CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, "model.yaml")
LOG_DIR = os.path.join(ROOT_DIR, LOG_FOLDER_NAME)
PIPELINE_DIR = os.path.join(ROOT_DIR, PIPELINE_FOLDER_NAME)
MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)
print(MODEL_DIR)

@app.route('/train', methods=['POST', 'GET'])
def train():
        try: 
            config = Configuartion()
            pipeline = Pipeline(config=config)

            pipeline.run_pipeline()

            return "Pipeline Successfully completed and model is trained"
        except Exception as e:
            raise PackageException(e, sys) from e

@app.route('/predict', methods=['POST', 'GET'])
def index():
    try:
        if request.method == 'POST':
            Age = float(request.json['Age'])
            TypeofContact = float(request.json['TypeofContact'])
            CityTier = float(request.json['CityTier'])
            DurationOfPitch = float(request.json['DurationOfPitch'])
            Occupation = float(request.json['Occupation'])
            Gender = float(request.json['Gender'])
            NumberOfPersonVisiting = float(request.json['NumberOfPersonVisiting'])
            NumberOfFollowups = request.json['NumberOfFollowups']
            ProductPitched = float(request.json['ProductPitched'])
            PreferredPropertyStar = float(request.json['PreferredPropertyStar'])
            MaritalStatus = float(request.json['MaritalStatus'])
            NumberOfTrips = float(request.json['NumberOfTrips'])
            Passport = float(request.json['Passport'])
            PitchSatisfactionScore = request.json['PitchSatisfactionScore']
            OwnCar = float(request.json['OwnCar'])
            NumberOfChildrenVisiting = float(request.json['NumberOfChildrenVisiting'])
            Designation = float(request.json['Designation'])
            MonthlyIncome = float(request.json['MonthlyIncome'])

            person_data = package_predictor.GetData(
                Age = Age,
                TypeofContact = TypeofContact,
                CityTier = CityTier,
                DurationOfPitch = DurationOfPitch,
                Occupation = Occupation,
                Gender = Gender,
                NumberOfPersonVisiting = NumberOfPersonVisiting,
                NumberOfFollowups = NumberOfFollowups,
                ProductPitched = ProductPitched,
                PreferredPropertyStar = PreferredPropertyStar,
                MaritalStatus = MaritalStatus, 
                NumberOfTrips = NumberOfTrips,
                Passport = Passport,
                PitchSatisfactionScore = PitchSatisfactionScore,
                OwnCar = OwnCar,
                NumberOfChildrenVisiting = NumberOfChildrenVisiting,
                Designation = Designation,
                MonthlyIncome = MonthlyIncome
            )
            
            X = person_data.get_dataframe()
            
            print(X.iloc[0].values)

            housing_predictor = package_predictor.PackagePredictor(model_dir=MODEL_DIR)
            result = housing_predictor.predict(X=X)

            
            if(result == 1):
                return "You will buy our package"
            else:
                return "You won't buy our package"

            return "Done"
    except Exception as e:
        raise PackageException(e, sys) from e

    return 'Done'

if __name__ == "__main__":
    app.run()