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

    @classmethod
    def predict(self, X):
        try:
            model_path = r'./packagePrediction/model_dir/model.pkl'
            model = load_object(file_path=model_path)

            logging.info(f"Model at {model_path} is successfully loaded")
            package_prediction = model.predict(X)
            logging.info(f"{model_path} exists is {package_prediction}")
            return package_prediction
        except Exception as e:
            raise PackageException(e, sys) from e
