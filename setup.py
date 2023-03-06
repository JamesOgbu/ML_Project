import os
from setuptools import find_packages, setup
from typing import List

# create a function to read and install all packages from "requirements.txt"
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    the function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

# setup
setup(
    name='ml_project',
    version='0.0.1',
    author='james',
    author_email='ogbujameschizoba@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt')),
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown'
)
