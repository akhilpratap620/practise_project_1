import yaml
from housing.exception import HousingException

def read_yaml_file(file_path:str):
    """we are reading yaml file through this function we just need to provide file path"""
    try:

        with open(file_path , "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e, sys) from e