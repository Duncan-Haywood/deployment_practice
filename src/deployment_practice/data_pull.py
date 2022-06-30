import boto3
import os
class DataPull:
    def __init__(self):
        self.data_url = 'https://carbonintensity.org.uk/'
        self.s3 = boto3.resource('s3')
        self.bucket_name = os.get_environ('S3_BUCKET')
        self.bucket = self.s3.Bucket(self.bucket_name)
    def pull_data(self):
        
    def s3_upload_data(self):
        
