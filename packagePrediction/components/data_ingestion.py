from re import L
import sys
import mysql.connector as conn
import pandas as pd
import os
from sklearn.model_selection import StratifiedShuffleSplit

from packagePrediction.entity.config_entity import DataIngestionConfig
from packagePrediction.entity.artifact_entity import DataIngestionArtifact

from packagePrediction.logger import logging
from packagePrediction.exception import PackageException

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise PackageException(e,sys)

    def get_raw_data(self):

        mydb = conn.connect(
        host="localhost",
        user="root",
        password="password"
        )

        cursor = mydb.cursor()
        cursor.execute("select * from tourist_package.test_df1")
        df = pd.DataFrame(cursor.fetchall(), columns=['Age', 'TypeofContact', 'CityTier', 'DurationOfPitch', 'Occupation',
       'Gender', 'NumberOfPersonVisiting', 'NumberOfFollowups',
       'ProductPitched', 'PreferredPropertyStar', 'MaritalStatus',
       'NumberOfTrips', 'Passport', 'PitchSatisfactionScore', 'OwnCar',
       'NumberOfChildrenVisiting', 'Designation', 'MonthlyIncome',
       'ProdTaken'])    

        logging.info(f"Data frame is created with {df.columns}")
        raw_data_dir = self.data_ingestion_config.raw_data_dir
        logging.info(f"Raw directory is {raw_data_dir}")
        if os.path.exists(raw_data_dir):
            os.remove(raw_data_dir)

        os.makedirs(raw_data_dir,exist_ok=True)

        df.to_csv(os.path.join(raw_data_dir, 'data.csv'), index=False)

        logging.info(f"Data frame stored")
        return raw_data_dir

    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            file_name = os.listdir(raw_data_dir)[0]

            data_file_path = os.path.join(raw_data_dir, file_name)

            logging.info(f"Reading CSV file at [{data_file_path}]")
            df = pd.read_csv(data_file_path)

            logging.info(f"Splitting data into train and test")
            strat_train_set = None
            strat_test_set = None

            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

            for train_index,test_index in split.split(df, df["ProdTaken"]):
                strat_train_set = df.loc[train_index].drop(["ProdTaken"],axis=1)
                strat_test_set = df.loc[test_index].drop(["ProdTaken"],axis=1)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        file_name)

            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                logging.info(f"Exporting training datset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path,index=False)

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok= True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_csv(test_file_path,index=False)

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path,
                                is_ingested=True,
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")

            return data_ingestion_artifact
        
        except Exception as e:
            raise PackageException(e,sys)
            

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            self.get_raw_data()
            return self.split_data_as_train_test()
        except Exception as e:
            raise PackageException(e,sys) from e

    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")