from setuptools import find_packages,setup   # find_packages within root folder (here its sensor folder). Setup will help on publishing and setting up the package
from typing import List
import os

requirements_file_path=os.path.join(os.getcwd(),"requirements.txt")

def get_requirements()->List[str]:

    requirement_list:List[str] = []
    with open(requirements_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            # let's also ignore empty lines and comments
            if not line or line.startswith('#'):
                continue
            requirement_list.append(line)
    
    return requirement_list

setup(
    name="cancer",
    version="0.0.1",
    author="Bonny",
    author_email="philipbonny18@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)

#get_requirements()

# Run the command "python setup.py install"