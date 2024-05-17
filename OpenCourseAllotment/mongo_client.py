from pymongo import MongoClient

def get_database(collection=None):
    """Return the MongoDB database object / collection"""
    
    client = MongoClient("mongodb://localhost:27017/")
    db = client["opencourse"]
    if not collection:
        return db
    return db[collection]