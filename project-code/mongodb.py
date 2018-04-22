import pymongo
from pymongo import MongoClient
import sys, getopt
import time
client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection
collection.create_index([('uid', pymongo.DESCENDING)])
posts = db.posts


#PER_INSERT = 10000
#TIMES  = 1000
def main(argv):
    per_insert = 0
    times = 1000
    try:
        opts, args = getopt.getopt(argv, "hp:")
    except getopt.GetoptError:
        print('mogodb.py -p <per_insert>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('mogodb.py -p <per_insert>')
            sys.exit()
        elif opt == '-p':
            per_insert = arg


    file = open('mongo_result_'+ per_insert+'.txt', 'a')
    per_insert = int(per_insert)
    for i in range(times):

        perLine = []
        for j in range(per_insert):
            perLine.append(str(i)+str(j))
        time_pre = time.time()
        for uid in perLine:
            post_id = posts.insert_one({'uid': uid}).inserted_id
        time_after = time.time()
        print("insert time {0}: {1}".format(i, time_after - time_pre))
        insert_time = time_after - time_pre


        perLine = []
        for j in range(per_insert):
            perLine.append(str(i) + str(j))
        time_pre = time.time()
        for uid in perLine:
            post_id = posts.find({'uid': uid})
        time_after = time.time()
        print("search time {0}: {1}".format(i, time_after - time_pre))
        search_time = time_after - time_pre


        file.write("{0} {1} {2}\n".format((i + 1) * per_insert, insert_time, search_time))


    file.close()



if __name__ == "__main__":
   main(sys.argv[1:])


