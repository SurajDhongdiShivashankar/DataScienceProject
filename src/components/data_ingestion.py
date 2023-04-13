import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    """
    Any inputs that's required will be through this class.

    This class includes the path that is used to save 
        a) raw data
        b) train data 
        c) test data

    Note: 
        Using @dataclass helps us to create a class having only defining the variables.

    """
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered Data Ingestion method or Component")

        try:
            # Read Data, can read data from multiple sources and must be replaced with respective functionality
            df = pd.read_csv("notebook\data\stud.csv")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            logging.info("Train test split initiated")
            train_data, test_data = train_test_split(self.ingestion_config.raw_data_path, train_size=0.2, random_state=42)

            df.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            train_data.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as ex:
            logging.info("Exception Exception")
            raise CustomException(ex, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
