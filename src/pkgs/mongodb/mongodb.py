from pymongo.mongo_client import MongoClient
from configs.globals import *

class Type4DB:
    def __init__(self, name: str=None) -> None:
        self.client = MongoClient(host=MONGO_HOST, port=MONGO_PORT, connect=False)
        self.db = self.client["type4_handler"]
        if name != None:
            self.collection = self.db[name]

    def set_collection(self, name):
        self.collection = self.db[name]

    # def