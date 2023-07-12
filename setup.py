# Package our application and deploy it on pypy

from setuptools import find_packages, setup         # find_packages - find all the packages used in the application
from typing import List

HYPEN_E_DOT = '-e .'                                           
'''
1. auto_trigger -  added in requirments file, which will automatically trigger setup.py file.
2. get_requirements function - This function will get the requirements(libraries) from the path(requirements.txt) and 
return it in the form of list        
3. Use of replace function - Every time when a file is read/written from one line to the next line \n will be recoreded/written to avoid 
that we can replace it with the blank sapce in the list
4. If statement is used to avoid '-e .' from the final requirment list
'''
def get_requirements(file_path:str)->List[str]:                
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()                                 
        requirements = [req.replace("\n","") for req in requirements]   
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name = 'End-End-ML-Project',
version = '0.0.1',
author = 'Gowtham',
author_email = 'gowtham12591@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')         
# Whatever the libraries that are available in the requirments file will be installed automatically
)
