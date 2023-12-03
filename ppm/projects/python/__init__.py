import os
import subprocess
import requests
import datetime

from ppm.settings import RUN_PATH, RUN_FOLDER
from ppm.templates import license


def py_config():

    print('This will walk you through creating a new Python project.')
    print('It only covers the most common items, and tries to guess sensible defaults.')
    print('Press ^C at any time to quit.', end='\n\n')

    project_name = input(f'\n\nProject name: ({RUN_FOLDER}) ')

    if project_name is None:
        project_name = RUN_FOLDER

    project_script = input(f'Project script: (main.py) ')

    if project_script is None:
        project_script = 'main.py'

    python_venv = input(f'Python vertual environment creation: (y/n) ')

    if python_venv == 'y':
        python_venv = True
    else:
        python_venv = False

    project_license = input(f'Project license: (MIT) ')

    if project_license is None:
        project_license = 'MIT'

    project_description = input(f'Project description: ')

    if project_description is None:
        project_description = ''

    project_author = input(f'Project author: ({os.getlogin()}) ')

    if project_author is None:
        project_author = os.getlogin()

    create_py_project(
        project_name=project_name,
        project_script=project_script,
        python_venv=python_venv,
        project_license=project_license,
        project_description=project_description,
        project_author=project_author
    )


def create_py_project(**kwargs):
    print('\n\nCreating project...')
    project_name = kwargs['project_name']
    project_script = kwargs['project_script']
    python_venv = kwargs['python_venv']
    project_license = kwargs['project_license']
    project_description = kwargs['project_description']
    project_author = kwargs['project_author']

    if not os.path.exists(f'{RUN_PATH}/{project_name}'):
        os.makedirs(f'{RUN_PATH}/{project_name}')
        print(f'\n\nCreated project folder: {project_name}', end='\n\n')

    if python_venv:
        create_py_virtualenv(project_name=project_name)

    create_gitignore(project_name=project_name)
    create_py_requirements(project_name=project_name, project_script=project_script)
    create_license(project_name=project_name, project_author=project_author, project_license=project_license)
    create_readme(project_name=project_name, project_script=project_script, project_license=project_license,
                  project_description=project_description, project_author=project_author)

    print('\n\nProject successfully created.', end='\n\n')


def create_py_virtualenv(**kwargs):
    project_name = kwargs['project_name']

    subprocess.run(
        ['python3', '-m', 'venv', f'{RUN_PATH}/{project_name}/venv'])
    print('Created Python virtual environment.', end='\n\n')
    print('\n\nTo activate virtual environment, run:', end='\n\n')
    print(f'\n\ncd {RUN_PATH}/{project_name}')
    print('source venv/bin/activate', end='\n\n')
    print('\n\nTo deactivate virtual environment, run:', end='\n\n')
    print('deactivate')


def create_gitignore(**kwargs):
    project_name = kwargs['project_name']

    gitignore = requests.get(
        'https://www.toptal.com/developers/gitignore/api/python').text

    with open(f'{RUN_PATH}/{project_name}/.gitignore', 'w') as f:
        f.write(gitignore)

    print('\n\nCreated .gitignore file.', end='\n\n')


def create_py_requirements(**kwargs):
    project_name = kwargs['project_name']
    project_script = kwargs['project_script']

    pipreqs = subprocess.run([f'{RUN_PATH}/{project_name}/venv/bin/pip', 'freeze'], shell=True, capture_output=True)
    
    with open(f'{RUN_PATH}/{project_name}/requirements.txt', 'w') as f:
        f.write('requests')
    
    print('\n\nCreated requirements.txt file.', end='\n\n')


def create_license(**kwargs):
    project_name = kwargs['project_name']
    project_license = kwargs['project_license']
    project_author = kwargs['project_author']

    if project_license == 'MIT':
        license_content = license.create_mit_license_template(year=2023, author=project_author)
    else:
        license_content = project_license

    with open(f'{RUN_PATH}/{project_name}/LICENSE', 'w') as f:
        f.write(license_content)


def create_readme(**kwargs):
    project_name = kwargs['project_name']
    project_script = kwargs['project_script']
    project_license = kwargs['project_license']
    project_description = kwargs['project_description']
    project_author = kwargs['project_author']

    with open(f'{RUN_PATH}/{project_name}/README.md', 'w') as f:
        f.write(f'# {project_name}\n')
        f.write(f'{project_description}\n')
        f.write(f'## License\n')
        f.write(f'{project_license}\n')
        f.write(f'## Author\n')
        f.write(f'{project_author}\n')

    print('\n\nCreated README.md file.', end='\n\n')
