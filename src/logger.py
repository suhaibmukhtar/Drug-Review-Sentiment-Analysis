import logging
from datetime import datetime
from pathlib import Path
import os
import sys

ROOT_PATH = Path(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(str(ROOT_PATH))

from src.config.config import LOG_FOLDER_PATH

if not os.path.exists(LOG_FOLDER_PATH):
    os.makedirs(LOG_FOLDER_PATH)

LOG_FILE_NAME = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"  # Replace colons with underscores

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s-%(funcName)s-%(lineno)d-%(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_FOLDER_PATH, LOG_FILE_NAME)),
        logging.StreamHandler()
    ]

)
if __name__=="__main__":
    logging.info("Logging Has Been Started")