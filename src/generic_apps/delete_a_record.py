from pkgs.mongodb.mongodb import *
from bson.objectid import ObjectId


def remove_by_id(mongo: Type4DB, id: str):
    record = mongo.collection.delete_one({"_id": ObjectId(id)})
    mongo.client.close()
    return True