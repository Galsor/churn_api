from google.cloud import storage
from churn_api.settings import BUCKET_NAME, MODEL_NAME
from joblib import load
import os

def load_model(bucket_name=BUCKET_NAME, source_blob_name=MODEL_NAME):
    """Import pickle model already trained form bucket.

    Arguments
    ---------
    bucket_name: str
        Bucket name.
    source_blob_name: str
        Path to the file trained model in bucket.

    Return
    ------
    model: scikit-learn Pipeline
        Fitted pipeline.
    """
    # Google Storage Client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    #download that file and name it 'local.joblib'
    model_local='local.joblib'
    blob.download_to_filename(model_local)
    #load that file from local file
    model=load(model_local)
    os.remove(model_local)
    return model

if __name__ == "__main__":
    model = load_model()
    
    print(model)