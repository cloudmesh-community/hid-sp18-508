import pymongo
from pymongo import MongoClient
import pprint
import numpy
import time
client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection
collection.create_index([('uid', pymongo.DESCENDING)])
posts = db.posts

TimeTuple=time.localtime(time.time())
fmt='%Y-%m-%d %a %H:%M:%S'
test=time.strftime(fmt,TimeTuple)
print('time now:',test)
PER_INSERT = 10000
TIMES  = 1000
file = open('mongo_result.txt', 'a')
for i in range(TIMES):
   
    perLine = []
    for j in range(PER_INSERT):
        perLine.append(str(i)+str(j))
    time_pre = time.time()
    for uid in perLine:
        post_id = posts.insert_one({'uid': uid}).inserted_id
    time_after = time.time()
    print("insert time {0}: {1}".format(i, time_after - time_pre))
    insert_time = time_after - time_pre



    time_pre = time.time()
    res = posts.find().sort('uid', pymongo.DESCENDING).limit(10)
    time_after = time.time()
    print("sort time: {0}".format(time_after - time_pre))
    sort_time = time_after - time_pre


    perLine = []
    for j in range(PER_INSERT):
        perLine.append(str(i) + str(j))
    time_pre = time.time()
    for uid in perLine:
        post_id = posts.find({'uid': uid})
    time_after = time.time()
    print("search time {0}: {1}".format(i, time_after - time_pre))
    search_time = time_after - time_pre

  
    file.write("{0} {1} {2} {3}\n".format((i + 1) * PER_INSERT, insert_time, sort_time, search_time))


file.close()

TimeTuple=time.localtime(time.time())
fmt='%Y-%m-%d %a %H:%M:%S'
test=time.strftime(fmt,TimeTuple)
print('time end:',test)



