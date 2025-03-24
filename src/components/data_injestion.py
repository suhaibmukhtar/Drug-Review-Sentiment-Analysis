import numpy as np
import pandas as pd
from pathlib import Path
import os
import sys

ROOT_PATH = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(ROOT_PATH)

from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.config.config import DATA_ARTIFACTS, TEST_RAW_DATASET_PATH, TRAIN_RAW_DATASET_PATH
#dataclass is a decorator with help of which we are able to directly define class-variables
#datainjestionconfig will contain all paths where we want to save our output
#Note: Only possible when we have to define variables only, nor the method, should contain variables only
@dataclass
class DataInjestionConfig:
    train_dataset_path=os.path.join(DATA_ARTIFACTS,'train.csv')
    test_dataset_path=os.path.join(DATA_ARTIFACTS,'test.csv')
    
class DataInjestion:
    def __init__(self):
        self.injestion_config = DataInjestionConfig()
    
    def initiate_data_injestion(self):
        """
        This function will initiate data-injestion
        """
        logging.info("Started Data-Injestion-initiation")
        try:
            train_data = pd.read_csv(TRAIN_RAW_DATASET_PATH)
            test_data = pd.read_csv(TEST_RAW_DATASET_PATH)
            logging.info("Datasets Loaded Successfully")
            #dirname is used to read the directory-name
            os.makedirs(os.path.dirname(self.injestion_config.train_dataset_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.injestion_config.test_dataset_path),exist_ok=True)
            #after creation of directory saving the csv files
            logging.info("Train-test-split-initiated")
            train_data.to_csv(self.injestion_config.train_dataset_path,index=False,header=True)
            test_data.to_csv(self.injestion_config.test_dataset_path, index=False, header=True)
            logging.info("Train-test-split performed successfully")
            logging.info(f"Train-dataset shape:{train_data.shape}")
            logging.info(f"Test-dataset shape:{test_data.shape}")
            logging.info(f"Columns Present in Dataset:{train_data.columns}")
            logging.info(f"No. of Missing records:{train_data.isna().sum()}")
            logging.info(f"No. of Duplicates:{train_data.duplicated().sum()}")
            return(
                self.injestion_config.train_dataset_path,
                self.injestion_config.test_dataset_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj1 = DataInjestion()
    train_path, test_path= obj1.initiate_data_injestion()






