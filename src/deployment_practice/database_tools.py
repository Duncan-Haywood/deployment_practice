import os
import mysql.connector
from mysql.connector import errorcode
import logging
import pandas as pd

class DB:
    def __init__(self):
        # database setup
        self.host = os.get_environ("DB_HOST")
        self.password = os.get_environ("DB_PASSWORD")
        self.user = os.get_environ("DB_USER")
        self.db_name = os.get_environ("DB_NAME")
        self.db_connection = None
        self.db_cursor = self.db_connection.cursor()
        self.connect_to_database()

    def connect_to_database(self):
        def _connect():
            self.db_connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host, db_name=self.db_name)
        try:
            _connect()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.exception("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.exception("Database does not exist")
                self.create_database()
                _connect()
            else:
                logging.exception()            

    def create_database(self):
        try:
            self.cursor.execute(f"CREATE DATABASE {self.db_name} DEFAULT CHARACTER SET 'utf8'")
        except mysql.connector.Error:
            logging.exception("failed to create database")

    def db_upload_data(self, df: pd.DataFrame, table_name: str):
        df.to_sql(con=self.db_connection, if_exists='replace', name=table_name, flavor='mysql')

    def db_download_data(self, table_name: str) -> pd.DataFrame:
        db_df = pd.read_sql(table_name, con=self.db_connection)
        return db_df


