from pathlib import Path
import os
import sys

ROOT_PATH = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(ROOT_PATH)

SUB_PACKAGE_PATH = os.path.join(ROOT_PATH,'src')

LOG_FOLDER_PATH = os.path.join(SUB_PACKAGE_PATH,"Logs")

ARTIFACTS_PATH = os.path.join(SUB_PACKAGE_PATH,'artifacts')

TRAIN_RAW_DATASET_PATH = os.path.join(SUB_PACKAGE_PATH,'dataset','RawDataset','drugsComTrain_raw.csv')
TEST_RAW_DATASET_PATH = os.path.join(SUB_PACKAGE_PATH,'dataset','RawDataset','drugsComTest_raw.csv')

DATA_ARTIFACTS = os.path.join(SUB_PACKAGE_PATH,'datasets',"PreProcessed")

COLUMNS_TO_MERGE = ['drugName','condition','review']
