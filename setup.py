from setuptools import find_packages, setup
from typing import List
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="ML_Eng",
    version="0.0.1",
    author="Miguel Betances",
    author_email="miguelbetances17@gmail.com",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=get_requirements("requirements.txt")
)