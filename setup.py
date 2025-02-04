from setuptools import find_packages,setup
from typing import List

x='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]
    
        if x in requirements:
            requirements.remove(x)
    return requirements
setup(
    name='MLproject',
    version='0.0.1',
    author='Shyvalya',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)