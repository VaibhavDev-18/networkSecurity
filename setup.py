from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    fn returns list of requirements.
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt.', 'r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirement.txt not found")


setup(
    name="NetworkSecurity",
    version="0.0.1",
    packages=find_packages(),
    install_requirements=get_requirements()
)