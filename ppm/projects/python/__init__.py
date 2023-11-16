import os
import subprocess
from pyfiglet import Figlet

from ppm.settings import RUN_PATH, RUN_FOLDER

def py_config():
    f = Figlet(font='puffy')
    print(f.renderText('moorfo.uz'))

    project_name = input(f'Project name ({RUN_FOLDER}): ')

    if project_name:
        path = RUN_PATH.joinpath(project_name)
        os.mkdir(path)
        open(path.joinpath('main.py'), 'w')
        subprocess.run(['python3', '-m', 'venv', 'venv'])
    else:
        open(RUN_PATH.joinpath('main.py'), 'w')