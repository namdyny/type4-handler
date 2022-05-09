from datetime import datetime
from dateutil.relativedelta import relativedelta
from pkgs.mongodb.mongodb import *
from bson.objectid import ObjectId


def get_by_id(mongo: Type4DB, id: str):
    record = mongo.collection.find_one({"_id": ObjectId(id)})
    record["id"] = id
    del record["_id"]
    mongo.client.close()
    return record