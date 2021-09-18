import bson
from bson.raw_bson import RawBSONDocument
from dateutil import parser
from pandas import DataFrame

expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
def get_database():
    from pymongo import MongoClient
    import pymongo
    CONNECTION_STRING = 'mongodb://localhost:27017/myFirstDatabase'
    client = MongoClient(CONNECTION_STRING)
    return client['user_shopping_list']



def save_to_collection(collection_name, tweets):
    try:
        dbname = get_database()
        collection = dbname[collection_name]
        print(collection_name)
        rawDocs = []
        for x in tweets:
            rawDocs.append((RawBSONDocument(bson.BSON.encode(x.__dict__))))
        collection.insert_many(rawDocs)
    except Exception as e:
        print(e)
