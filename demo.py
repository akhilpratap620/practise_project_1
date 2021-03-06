from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.constant import *



def main():
    try:
        #data_validation_config_01 = Configuartion().get_data_validation_config()
        #print(data_validation_config_01)
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #pipeline.start()
        logging.info("main function execution completed.")
        data_validation_config = Configuartion().get_model_trainer_config()
        print( data_validation_config)
        # schema_file_path=r"D:\Project\machine_learning_project\config\schema.yaml"
        # file_path=r"D:\Project\machine_learning_project\housing\artifact\data_ingestion\2022-06-27-19-13-17\ingested_data\train\housing.csv"

        # df= DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)
     



if __name__=="__main__":
    main()
