import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class SqlConnector:
    def __init__(self):
        self.__cnt = None

    def get_instance(self):
        if not self.__cnt:
            self.__cnt = mysql.connector.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                database='log_schema'
            )
        return self.__cnt