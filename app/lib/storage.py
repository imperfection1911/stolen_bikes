from pymongo import MongoClient

from config import Configuration


class Storage:

    def __init__(self):
        self.config = Configuration()
        self.connection = MongoClient(self.config.mongo_host, 27017)
        self.db = self.connection.stolen_bikes
        self.collection = self.db.bikes

    def insert(self, bike):
        id = self.collection.insert_one(bike).inserted_id
        if id:
            return True
        return False

    def insert_many(self, bikes):
        result = self.collection.insert_many(bikes)
        if result:
            return True
        return False

    def find(self, query):
        return self.collection.find(query)

    def clear(self):
        self.collection.remove()






