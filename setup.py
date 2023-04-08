from setuptools import find_packages ,setup
from typing import List

def get_requirements(file_path:str)-> List(str):
    """
    This function will reurn the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace ("\n", " ") for req in requirements]

setup(
name = 'MLProjects',
version = '0.0.1',
author = 'Sunil',
author_email = 'sunildubeym1306@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')


)