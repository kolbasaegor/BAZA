import datetime
from pymongo import MongoClient
from pymongo.collection import Collection

HOST = 'localhost'
PORT = 27017
DB_NAME = 'test'
COLLECTION_NAME = 'restaurants'
COLLECTION = MongoClient(f'mongodb://{HOST}:{PORT}')[DB_NAME][COLLECTION_NAME]

print('All Indian cuisines:')
for doc in COLLECTION.find({'cuisine': 'Indian'}):
    print(doc)

print('All Indian and Thai cuisines:')
for doc in COLLECTION.find({'$or': [{'cuisine': 'Indian'}, {'cuisine': 'Thai'}]}):
    print(doc)

print('Restaurant with the following address: 1115 Rogers Avenue, 11226')
for doc in COLLECTION.find({'address.building': '1115',
                            'address.street': 'Rogers Avenue',
                            'address.zipcode': '11226'}):
    print(doc)
