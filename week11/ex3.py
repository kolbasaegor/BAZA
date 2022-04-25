import datetime
from pymongo import MongoClient
from pymongo.collection import Collection

HOST = 'localhost'
PORT = 27017
DB_NAME = 'test'
COLLECTION_NAME = 'restaurants'
COLLECTION = MongoClient(f'mongodb://{HOST}:{PORT}')[DB_NAME][COLLECTION_NAME]

print('Amount of deleted Manhattan located restaurant:',
      COLLECTION.delete_one({'borough': 'Manhattan'}).deleted_count)

print('Amount of deleted all Thai cuisines:',
      COLLECTION.delete_many({'cuisine': 'Thai'}).deleted_count)
