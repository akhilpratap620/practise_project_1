from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys
app = Flask(__name__)

@app.route("/", methods= ['GET','POST'])
def index():
    try:
        raise Exception("we are testing exception class")
    except Exception as e:
        housing = HousingException(e, sys)   
        logging.info(housing.error_message) 
        logging.info("we are testing logging module")
    return "starting machine learning code first update"

if __name__=="__main__":
    app.run(debug=True)    