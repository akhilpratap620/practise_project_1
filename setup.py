from setuptools import setup
from typing import List


#declaring variable for setup function
PROJECT_NAME="housing-predict"
VERSION="0.0.1" 
AUTHOR="Akhil pratap singh"
DSCRIPTION="this is first fsds batch project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
"""txt
this function is going to return requirment.return 
list of librraries required for package

"""
    
    

setup(
    name=PROJECT_NAME,
    version =VERSION, 
    author=AUTHOR,
    discription=DSCRIPTION,
    packages=["housing"] ,
    install_requires=get_requirements_list()

)
