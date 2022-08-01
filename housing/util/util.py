import yaml
from housing.exception import HousingException
import os , sys
import dill
import numpy as np
import pandas as pd
from housing.constant import * 

def read_yaml_file(file_path:str):
    """we are reading yaml file through this function we just need to provide file path"""
    try:

        with open(file_path , "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e, sys) from e

def write_yaml_file(file_path:str , data:dict=None):
    try:
        """
        we will take input as a file_path and we will also take a dict as input 
        and we will create output
        """
        os.makedirs(file_path , exist_ok = True)
        with open(file_path , 'w') as yaml_file :
            if data is not None:


                yaml.dump(data, yaml_file)

    except Exception as e:
        raise HousingException(e, sys) from e


def load_numpy_array_data(file_path:str)->np.array:
    try:
        """we will take input as file path and will read the data in 
        numpy array formate
        """
        with open(file_path , 'rb') as file_obj:
            return np.load(file_obj)
    
    except Exception as e:
        raise HousingException(e, sys) from e


def save_object(file_path:str,obj):
    """
    file_path: str
    obj: Any sort of object
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise HousingException(e,sys) from e


def load_object(file_path:str):
    try:
        with open(file_path , 'rb') as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise HousingException(e, sys) from e

def load_data(file_path: str, schema_file_path: str) -> pd.DataFrame:
    try:
        datatset_schema = read_yaml_file(schema_file_path)

        schema = datatset_schema[DATASET_SCHEMA_COLUMNS_KEY]

        dataframe = pd.read_csv(file_path)

        error_messgae = ""


        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])
            else:
                error_messgae = f"{error_messgae} \nColumn: [{column}] is not in the schema."
        if len(error_messgae) > 0:
            raise Exception(error_messgae)
        return dataframe

    except Exception as e:
        raise HousingException(e,sys) from e
    



        
        

def  save_numpy_array_data(file_path:str , array:np.array):
        try:
            dir_path = os.path.dirname(file_path)
            os.makedirs(dir_path ,  exist_ok=True)

            with open(file_path ,  'wb') as file_obj:
                np.save(file_obj , array)

            

        except Exception as e:
            raise HousingException(e, sys) from e
        
