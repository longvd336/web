from pymongo import MongoClient
from bson.objectid import ObjectId
import matplotlib.pyplot as plt

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(uri)
all_poem = client.c4e

all_data = all_poem.customers

x = all_data.count({'ref':'events'})
y = all_data.count({'ref':'ads'})
z = all_data.count({'ref':'wom'}) 


        
labels = ['events', 'Advertisements', 'Word of Mouth']

sizes = [x, y, z]

colors = ['yellowgreen', 'gold', 'lightskyblue']

patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)

plt.legend(patches, labels, loc="best")

plt.axis('equal')

plt.tight_layout()
plt.show()