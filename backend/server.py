import json
from flask import Flask, request, jsonify
from dao import log_dao
from sql_connector.SqlConnector import SqlConnector


class LogServer:
    def __init__(self, connection):
        self.app = Flask(__name__)
        self.connection = connection
        self.port = 5555

    def init_routes(self):
        @self.app.route('/')
        def home():
            return "Hello, This is the Log Server"

        @self.app.route('/get_all_logs', methods=['GET'])
        def get_all_logs():
            logs = log_dao.get_all_logs(self.connection)
            response = jsonify(logs)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        @self.app.route('/insert_log', methods=['POST'])
        def insert_log():
            request_payload = json.loads(request.form['data'])
            status = log_dao.insert_new_log(self.connection, request_payload)
            response = jsonify({'status': status})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

    def start(self):
        self.init_routes()
        self.app.run(port=self.port)

if __name__ == '__main__':
    sql_connector = SqlConnector().get_instance()
    server = LogServer(sql_connector)
    print("Server started on port: " + str(server.port))
    server.start()

