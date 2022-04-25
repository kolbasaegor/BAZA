import datetime
from pymongo import MongoClient
from pymongo.collection import Collection

HOST = 'localhost'
PORT = 27017
DB_NAME = 'test'
COLLECTION_NAME = 'restaurants'
COLLECTION = MongoClient(f'mongodb://{HOST}:{PORT}')[DB_NAME][COLLECTION_NAME]

cursor = COLLECTION.find({'address.street': 'Rogers Avenue'})

for_deleting_ids = []
for_updating_ids = []

for doc in cursor:
    count = 0

    for grade in doc['grades']:
        if grade['grade'] == 'C':
            count += 1

    if count > 1:
        for_deleting_ids.append(doc['_id'])
    else:
        for_updating_ids.append(doc['_id'])

COLLECTION.delete_many({'_id': {'$in': for_deleting_ids}})
COLLECTION.update_many(
    {'_id': {'$in': for_updating_ids}},
    {'$push': {'grades': {'date': datetime.datetime.now(), 'grade': 'C', 'score': 0}}}
)
