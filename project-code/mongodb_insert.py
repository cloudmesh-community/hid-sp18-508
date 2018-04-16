import pymongo
from pymongo import MongoClient
import pprint
import numpy
import time
client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection
posts = db.posts
t = time.time()
print(t)
TimeTuple=time.localtime(time.time())
fmt='%Y-%m-%d %a %H:%M:%S'
test=time.strftime(fmt,TimeTuple)
print('time now:',test)
with open('test_0.txt', 'r') as f:
    data = f.readlines()

    for line in data:
        row = line.split()
        post = {"uid": row[0],
                "mid": row[1],
                "rate": row[2]}

        post_id = posts.insert_one(post).inserted_id
t = time.time()
print(t)
TimeTuple=time.localtime(time.time())
fmt='%Y-%m-%d %a %H:%M:%S'
test=time.strftime(fmt,TimeTuple)
print('time end:',test)

