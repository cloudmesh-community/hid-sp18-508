from cassandra.cluster import Cluster
import time
cluster = Cluster()
session = cluster.connect()
session.set_keyspace('dev')

TimeTuple=time.localtime(time.time())
fmt='%Y-%m-%d %a %H:%M:%S'
test=time.strftime(fmt,TimeTuple)
print('time now:',test)
PER_INSERT = 10000
TIMES  = 1000
file = open('casandra_result.txt', 'a')
for i in range(TIMES):

    perLine = []
    for j in range(PER_INSERT):
        perLine.append(str(i)+str(j))
    time_pre = time.time()
    for uid in perLine:
        session.execute("INSERT INTO test (uid) VALUES (%s)", [uid])  # right
    time_after = time.time()
    print("insert time {0}: {1}".format(i, time_after - time_pre))
    insert_time = time_after - time_pre



    perLine = []
    for j in range(PER_INSERT):
        perLine.append(str(i) + str(j))
    time_pre = time.time()
    for uid in perLine:
        query = "SELECT * FROM test WHERE uid=%s"
        future = session.execute(query, [uid])
    time_after = time.time()
    print("search time {0}: {1}".format(i, time_after - time_pre))
    search_time = time_after - time_pre


    file.write("{0} {1} {2} {3}\n".format((i + 1) * PER_INSERT, insert_time, 0, search_time))


file.close()

TimeTuple=time.localtime(time.time())
fmt='%Y-%m-%d %a %H:%M:%S'
test=time.strftime(fmt,TimeTuple)
print('time end:',test)
