from housing.config.configuration import Configuartion
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataValidationConfig
from housing.entity.config_entity import DataIngestionConfig
import os,sys



class DataValidation:
    
    def __init__(self ,data_validation_config:DataValidationConfig ,data_ingestion_artifact:DataIngestionArtifact):
        self.data_validation_config=data_validation_config
        self.data_ingestion_artifact = data_ingestion_artifact



        try:
            pass
        except Exception as e :
            raise HousingException(e, sys) from e


    def is_train_test_file_exists(self)->bool:
        try:
            logging.info("cheking if train and test file exists or not")    
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist =os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_exist = is_train_file_exist and is_test_file_exist
            logging.info("is train test file exists?->{is_exist}")
            return is_exist

            if not is_exist:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                message = f"Training file :{training_file} , testing_file path:{testing_file}" \
                    "is not present"
                logging.info(message)    
                raise Exception(message)

        except Exception as e:
            raise HousingException( e, sys) from e

    def validate_dataset_schema(self)->bool:
        try:
            validation_status = False


            


            validation_status = True 
            return validation_status
        except Exception  as  e:
            raise HousingException(e, sys) form e 



    def intiate_data_validation(self):
        try:
            self.is_train_test_file_exists()

            

            self.validate_dataset_schema()    

        except Exception as e:
            raise HousingException(e, sys) from e
    

    





