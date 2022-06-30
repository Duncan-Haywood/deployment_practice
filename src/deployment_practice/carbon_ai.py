import boto3
import os
import sklearn
from joblib import Parallel, delayed


class CarbonAI:
    def __init__(self, input_folder_path: str):
        self.input_folder_path = input_folder_path
        self.bucket_name = os.get_environ("S3_BUCKET")
        self.s3 = boto3.resource("s3")
        self.bucket = self.s3.Bucket(self.bucket_name)
        self.s3_client = self.s3.client()
    def train(self):
        return NotImplementedError
    def predict(self):
        return NotImplementedError
    def download_data(self):
        """TODO - hopefully multipart isn't needed - if so, switch to bucket.download_fileobj"""
        #get keys of object in folder
        response = self.s3_client.list_objects(Bucket=self.bucket_name, prefix = self.input_folder_path)
        object_keys = [response["Contents"][i]["Key"] for i in len(response["Contents"])]
        #helper function for parallelization
        def _download_file(file_key:str):
            self.bucket.download_file(file_key, file_key)
        # downloads files in parallel cpu jobs    
        Parallel(n_jobs=-1)(delayed(_download_file)(file_key) for file_key in object_keys)
    def preprocess(self):
        return NotImplementedError

