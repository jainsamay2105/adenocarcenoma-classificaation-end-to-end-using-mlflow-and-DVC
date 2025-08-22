## Generic template for any CNN classifier 
## Author : Samay Jain, https://github.com/jainsamay2105

import os
from pathlib import Path #path is a class
import logging # The logging library in Python is the built-in way to record messages from your program — very useful for debugging, monitoring, and production ML pipelines.

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


project_name = "cnn_classifier"


list_of_files = [
    ".github/workflows/.gitkeep", #.gitkeep is placeholder  #This folder is usually used for GitHub Actions workflows (CI/CD pipelines like testing, linting, or deployment)
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

# all the paths are according to linux paths '/' not '\' 
# use Path() : automatically converts strings to path according to os
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = filepath.parent , filepath.name

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory -> {filedir} for the file {filename}' )
    
    if (not os.path.exists(filepath)) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating an empty file -> {filename}')
    
    else:
        logging.info(f"{filename} already exist")