import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.mongodb.mongodb import Type4DB


def test_mongo_api_connection():
    db = Type4DB()
    res = db.client["type4"]["connection_test"].find()
    assert res[0]["dummy"] == "dummy"
