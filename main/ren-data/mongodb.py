import pymongo

database_name = 'etl-data'
connection_url = 'mongodb://localhost:27017/'
connection = None

# To connect to the MongoDB server, we will use the MongoClient method
def db_connection():
    client = pymongo.MongoClient(connection_url)
    return client[database_name]

# save data
def save_data(collection_name, document):
    if connection is None:
        print(f"new connection open for transaction")
        collection = db_connection()[collection_name]
        print(f"data written to {collection}")
        collection.insert_one(document)
