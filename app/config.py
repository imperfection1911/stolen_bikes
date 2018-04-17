import os
import configparser


class Configuration:

    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(os.path.dirname(os.path.abspath(__file__)) + '/config.ini')
        self.bikepost_url = self.config.get('bikepost', 'url')
        self.user_agent = self.config.get('http', 'user_agent')
        self.token = self.config.get('telegram', 'token')
        self.mongo_host = self.config.get('mongo', 'host')
        self.interval = self.config.get('interval', 'time')