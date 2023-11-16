import os
from pathlib import Path

RUN_PATH = Path(os.getcwd()).resolve()

RUN_PATH_STR = str(RUN_PATH)

RUN_FOLDER = RUN_PATH_STR.split('/')[-1]