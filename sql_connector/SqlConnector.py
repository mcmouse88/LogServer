import mysql.connector

class SqlConnector:
    def __init__(self):
        self.__cnt = None

    def get_instance(self):
        if not self.__cnt:
            self.__cnt = mysql.connector.connect(
                user='root',
                password='****',
                host='127.0.0.1',
                database='log_schema'
            )
        return self.__cnt