from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@c4e29-cluster-lmdem.mongodb.net/test?retryWrites=true"
#mo uri
client = MongoClient(uri)

#tao ra mot tu
foods = client.foods_app

#tao ra 1 ngan tu (tuong tu khoi tao 1 dict)
Foods_data = foods["foods"]

#khoi tao du lieu trong ngan tu do 

# foods_data.insert_many(foods_coll)
