from pymongo import MongoClient
from config import DATABASES

def get_mongo():
    conf = next(db for db in DATABASES if db["type"] == "mongodb" and db["enabled"])
    client = MongoClient(conf["uri"])
    db = client[conf["db_name"]]
    return db