from operator import mod
import os
import sys
from packagePrediction.logger import logging
from packagePrediction.exception import PackageException
from packagePrediction.util.util import load_object

import pandas as pd


class GetData:

    def __init__(self,
                 Age: float,
                 TypeofContact: float,
                 CityTier: float,
                 DurationOfPitch: float,
                 Occupation: float,
                 Gender: float,
                 NumberOfPersonVisiting: float,
                 NumberOfFollowups: float,
                 ProductPitched: float,
                 PreferredPropertyStar: float,
                 MaritalStatus: float,
                 NumberOfTrips: float,
                 Passport: float,
                 PitchSatisfactionScore: float,
                 OwnCar: float,
                 NumberOfChildrenVisiting: float,
                 Designation: float,
                 MonthlyIncome: float
                 ):
        try:
            self.Age = Age
            self.TypeofContact = TypeofContact
            self.CityTier = CityTier
            self.DurationOfPitch = DurationOfPitch
            self.Occupation = Occupation
            self.Gender = Gender
            self.NumberOfPersonVisiting = NumberOfPersonVisiting
            self.NumberOfFollowups = NumberOfFollowups
            self.ProductPitched = ProductPitched
            self.PreferredPropertyStar = PreferredPropertyStar
            self.MaritalStatus = MaritalStatus
            self.NumberOfTrips = NumberOfTrips
            self.NumberOfTrips = NumberOfTrips
            self.Passport = Passport
            self.PitchSatisfactionScore = PitchSatisfactionScore
            self.OwnCar = OwnCar
            self.NumberOfChildrenVisiting = NumberOfChildrenVisiting
            self.Designation = Designation
            self.MonthlyIncome = MonthlyIncome
        except Exception as e:
            raise PackageException(e, sys) from e

    def get_dataframe(self):

        try:
            housing_input_dict = self.get_data_as_dict()
            df =  pd.DataFrame(housing_input_dict)
            logging.info("Dataframe is Created from dictonary")
            return df
        except Exception as e:
            raise PackageException(e, sys) from e

    def get_data_as_dict(self):
        try:
            input_data = {
                "Age": [self.Age],
                "TypeofContact": [self.TypeofContact],
                "CityTier": [self.CityTier],
                "DurationOfPitch": [self.DurationOfPitch],
                "Occupation": [self.Occupation],
                "Gender": [self.Gender],
                "NumberOfPersonVisiting": [self.NumberOfPersonVisiting],
                "NumberOfFollowups": [self.NumberOfFollowups],
                "ProductPitched": [self.ProductPitched],
                "PreferredPropertyStar": [self.PreferredPropertyStar],
                "MaritalStatus": [self.MaritalStatus],
                "NumberOfTrips": [self.NumberOfTrips],
                "Passport": [self.Passport],
                "PitchSatisfactionScore": [self.PitchSatisfactionScore],
                "OwnCar": [self.OwnCar],
                "NumberOfChildrenVisiting": [self.NumberOfChildrenVisiting],
                "Designation": [self.Designation],
                "MonthlyIncome": [self.MonthlyIncome]
                }

            print((list(input_data.keys())))
            logging.info(f"Dictonary with {(list(input_data.keys()))} keys is constructed")
            return input_data
        except Exception as e:
            raise PackageException(e, sys)


class PackagePredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise PackageException(e, sys) from e

    def get_latest_model_path(self):
        try:
            file_name ="model.pkl"
            latest_model_path = os.path.join(self.model_dir, file_name)
            print(latest_model_path)
            return latest_model_path
        except Exception as e:
            raise PackageException(e, sys) from e
    
    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            print(model_path)
            model = load_object(file_path=model_path)
            median_house_value = model.predict(X)
            return median_house_value
        except Exception as e:
            raise PackageException(e, sys) from e
