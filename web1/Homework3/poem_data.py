from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
all_poem = client.c4e

all_data = all_poem.posts
# data = [{"title":"Long Dep TRai",
#         "author":"LongPTIT",
#         "content":"Co 1 su that la Long hoc lop VT08 PTIT rat dep trai =)). "
# },
# {"title":"Tóc giống anh Bảnh",
# "author":" SƠn tùng MTP ",
# "content":"Anh Bảnh ơi em cắt tóc giống anh bố em đấm em không trượt phát làooo ...."

# }
# ]

# all_data.insert_many(data)


