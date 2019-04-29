from pymongo import MongoClient

from bson.objectid import ObjectId

uri = "mongodb+srv://admin:admin@c4e29-cluster-lmdem.mongodb.net/test?retryWrites=true"
#1. Create 1 connection
client = MongoClient(uri)

#2. Create / Get 
first_db = client.first_database

#3. Get/Create Collection
first_coll = first_db["first_collection"]

#4. Create a document

first_document = {
    "name":"pikachu",
    "description":"waste tme",
}

game_list = [
    {"name": "pubg",
    "description":"surival"

    },
    {
        "name":"fifa",
        "description":"sport"
    }
]
#5.CREATE : 
#5.1 Create one 

# first_coll.insert_one(first_document)

#5.2 CREATE many

# first_coll.insert_many(game_list)

#6.READ 
# 6.1 READ all:
all_games = first_coll.find()

#lazy loading

# for game in all_games:
#     print(game)

# 6.2 READ ONE:

# fifa = first_coll.find_one({"_id":ObjectId('5cc065d2afbfcb535ad15712')})
# print(fifa)

#7. UPDATE 

# fifa = first_coll.find_one({"_id":ObjectId('5cc065d2afbfcb535ad15712')})

# new_value = { "$set": { "name":"FO4" } }

# first_coll.update_one(fifa, new_value)

#8. DELETE

fifa = first_coll.find_one({"_id":ObjectId('5cc065d2afbfcb535ad15712')})
if fifa is not None :
    first_coll.delete_one(fifa )
else:
    print("not found")


