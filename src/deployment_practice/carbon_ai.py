import boto3
import os
from .database_tools import DB
from sklearn.linear_model import LinearRegression


class CarbonAI:
    def __init__(self):
        # get environment variables
        self.model_output_path = os.get_environ("MODEL_PATH")
        # set up aws resources
        self.bucket_name = os.get_environ("S3_BUCKET")
        self.s3 = boto3.resource("s3")
        self.bucket = self.s3.Bucket(self.bucket_name)
        self.s3_client = self.s3.client()
        self.db = DB()
        self.input_df = self.db.db_download_data('input_data')
        self.train_df = None
        self.time_steps = 5
        self.model = None
        self.set_model()
    def set_model(self):
        # TODO - lots
        self.model = LinearRegression(n_jobs=-1)

    def preprocess(self, df: pd.DataFrame):
        self.train_df = self.input_df.drop(axis='columns', labels=["start_time", "end_time", "intensity_index"])
        return NotImplementedError

    def train(self):
        self.preprocess()
        #split into time series 'x_data' and next step labels
        x_data = [self.train_df.iloc[[i-self.time_steps:i]].values for i in range(self.time_steps, train_df.shape[0]-1)]
        labels = [self.train_df["actual"].iloc[[i]].values for i in range(self.time_steps, self.train_df.shape[0])]
        # train model
        self.model = self.model.fit(X=x_data,y=labels)
        self.save_model()
    def save_model():
        return NotImplementedError
    def predict(self):
        self.preprocess()
        return NotImplementedError
