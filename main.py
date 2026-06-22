# lets import the etl modules to run the data extraction and transformation
import os
from etl.extract import fetch_data
from etl.transformm import transform_data
from etl.load import upload_csv

def run_pipeline():
    fetch_data()
    transform_data()
    # Obtenemos la variable de entorno
    bucket_name = os.environ.get("GCP_BUCKET_NAME")
    
    if bucket_name:
        # Le pasamos los 3 argumentos que la función de etl/load.py exige
        upload_csv(
            bucket_name=bucket_name,
            source_file="data/user_data_processed.csv",
            dest_blob="gold/user_data_processed.csv"
        )
    else:
        print("Error: No se encontró la variable GCP_BUCKET_NAME")

if __name__ == "__main__":
    run_pipeline()
