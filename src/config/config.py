from pathlib import Path
import os
import sys

ROOT_PATH = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(ROOT_PATH)

SUB_PACKAGE_PATH = os.path.join(ROOT_PATH,'src')

LOG_FOLDER_PATH = os.path.join(SUB_PACKAGE_PATH,"Logs")