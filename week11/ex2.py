import datetime
from pymongo import MongoClient
from pymongo.collection import Collection

HOST = 'localhost'
PORT = 27017
DB_NAME = 'test'
COLLECTION_NAME = 'restaurants'
COLLECTION = MongoClient(f'mongodb://{HOST}:{PORT}')[DB_NAME][COLLECTION_NAME]

print
(
    COLLECTION.insert_one({
            'address': {
                'building': '1480',
                'coord': [-73.9557413, 40.7720266],
                'street': '2 Avenue',
                'zipcode': '10075'
            },
            'borough': 'Manhattan',
            'cuisine': 'Italian',
            'grades': [{'date': datetime.datetime(2014, 10, 1, 0, 0), 'grade': 'A', 'score': 11}],
            'name': 'Vella',
            'restaurant_id': '41704620'
        }
    ).inserted_id
)
