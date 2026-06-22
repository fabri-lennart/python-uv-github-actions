# lets import the etl modules to run the data extraction and transformation
from etl.extract import extract_data
from etl.transformm import transform_data
from etl.load import upload_csv

def run_pipeline():
    extract_data()
    transform_data()
    upload_csv()

if __name__ == "__main__":
    run_pipeline()
