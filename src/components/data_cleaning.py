import numpy as np
import pandas as pd
from pathlib import Path
import os
import sys

ROOT_PATH = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(ROOT_PATH)

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.config.config import DATA_ARTIFACTS

@dataclass
class DataCleaningConfig:
    train_clean_path = os.path.join(DATA_ARTIFACTS,"cleaned_train.csv")
    test_clean_path = os.path.join(DATA_ARTIFACTS,'test_clean.csv')
    
    
class DataCleaning:
    def __init__(self):
        self.data_clean_config = DataCleaningConfig()
    