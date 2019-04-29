from pymongo import MongoClient
from bson.objectid import ObjectId

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(uri)

data = client.c4e

river = data.river

# all_river = river.find({'continent':'Africa'})

# for item in all_river:
#     print(item['name']) 

all_river_s_america = river.find({'continent':'S. America'})

for item in all_river_s_america:
    if (item['length'] > 1000):
        print(item['name'])



