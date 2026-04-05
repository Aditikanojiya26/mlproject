from setuptools import find_packages,setup
from typing import List

from typing import List

from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
name='mlproject',
version='0.0.1',
author='Aditi',
author_email='alpesh.food@gmail.com',
packages=find_packages(),#look for folder containing __init__.py file and consider it as package
install_requires=['pandas','numpy','seaborn']

)