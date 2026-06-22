import os
from google.cloud import storage
from dotenv import load_dotenv

load_dotenv()

def upload_csv(bucket_name, source_file, dest_blob):
    """Uploads a local file to GCS."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(dest_blob)
    blob.upload_from_filename(source_file, content_type='text/csv')
    print(f"Uploaded {source_file} to gs://{bucket_name}/{dest_blob}")


BUCKET_NAME = os.environ.get("GCP_BUCKET_NAME")

if BUCKET_NAME:
    upload_csv(
        bucket_name=BUCKET_NAME,
        source_file="data/user_data_processed.csv",
        dest_blob="gold/user_data_processed.csv"       
    )
else:
    print("Error: No se encontró la variable GCP_BUCKET_NAME")
