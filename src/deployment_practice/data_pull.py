import requests
from joblib import Parallel, delayed
import pandas as pd
import datetime
from .database_tools import DB



class DataPull:
    def __init__(self, datetime_range: pd.date_range = None):
        #set up variables for data pull and processing
        self.data_url = f'https://api.carbonintensity.org.uk/intensity/date/' # to add {from} Datetime in in ISO8601 format
        self.responses = None
        self.df = None
        self.table_name = 'input_data'
        # creates pandas satetime range for timesteps to query
        self.datetime_range = self.set_datetime_range() if datetime_range is None else datetime_range # ISO8601 format
        self.db = DB()


    def main(self):
        """Downloads data uploads it to mysql database as os.environ("DB_HOST"). Needs __init__ to be run first"""
        self.download_data()
        self.process_responses()
        self.db.db_upload_data(df=self.df, table_name=self.table_name)

    def set_datetime_range(self):
        self.datetime_range = pd.date_range(end=datetime.now(), periods=500, freq="30min")

    def download_data(self):
        datetimes = self.date_time_range.dt.strfrmt("%Y-%m-%dT%H:%minZ").values
        headers = {
            'Accept': 'application/json'
            }
        # requests the intensity data from datetimes in parallel
        self.responses = Parallel(n_jobs=-1)(delayed(requests.get)(f'{self.data_url}{datetime}', headers=headers)  for datetime in datetimes)

    def process_responses(self):
        self._data = list()
        def _process_response(response):
            # if response["error"] exists:
            #     raise Exception(f'{response["error"]}')
            #pull data from responses
            data_dict = {}
            response_data = response["data"]
            data_dict["start_time"] = response_data["from"] 
            data_dict["end_time"] = response_data["to"]
            data_dict["intensity_forecast"] = response_data["intensity"]["forecast"]
            data_dict["intensity_actual"] = response_data["intensity"]["actual"]
            data_dict["intensity_index"] = response_data["intensity"]["index"]
            # add dictionary of response data to data list for df use
            self._data.append(data_dict)
        # process responses in parallel
        Parallel(n_jobs=-1)(delayed(_process_response)(response) for response in self.responses)
        #create dataframe out of data
        self.df = pd.df(self._data)

if __name__ == "__main__":
    data_pull = DataPull()
    data_pull.main()
        
