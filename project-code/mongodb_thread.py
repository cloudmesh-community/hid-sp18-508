import threading
import time
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

exitFlag = 0
PER_INSERT = 10000
file = open('mongo_thread.txt', 'a')
class myThread1(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        insert(self.name, self.counter, 1000)
        print("Exiting " + self.name)

class myThread2(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        search(self.name, self.counter, 1000)
        print("Exiting " + self.name)


def insert(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        perLine = []
        for j in range(PER_INSERT):
            perLine.append(str(counter) + str(j))
        time_pre = time.time()
        for uid in perLine:
            post_id = posts.insert_one({'uid': uid}).inserted_id
        time_after = time.time()
        print("insert time {0}: {1}".format(counter, time_after - time_pre))
        insert_time = time_after - time_pre
        print("%s: %s" % (threadName, time.ctime(time.time())))
        file.write("{0} {1} {2}\n".format("insert", (counter + 1) * PER_INSERT, insert_time))
        counter -= 1

def search(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        perLine = []
        for j in range(PER_INSERT):
            perLine.append(str(counter) + str(j))
        time_pre = time.time()
        for uid in perLine:
            post_id = posts.find({'uid': uid})
        time_after = time.time()
        print("search time {0}: {1}".format(counter, time_after - time_pre))
        search_time = time_after - time_pre
        print("%s: %s" % (threadName, time.ctime(time.time())))
        file.write("{0} {1} {2}\n".format("search",(counter + 1) * PER_INSERT, search_time))
        counter -= 1



thread1 = myThread1(1, "Thread-1", 1)
thread2 = myThread2(2, "Thread-2", 2)


thread1.start()
thread2.start()

print("Exiting Main Thread")

