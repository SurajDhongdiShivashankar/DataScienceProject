from typing import List
from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This method will return the list of requirements
    '''
    with open(file_path) as f:
        requirements = f.read().splitlines()
        requirements = [r.replace('\n', '') for r in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    print('requirements: ', requirements)
    return requirements

setup(
    name="Data Science Project",
    version='0.0.1',
    author='Suraj D S',
    author_email='suraj.dhongadi.s@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)