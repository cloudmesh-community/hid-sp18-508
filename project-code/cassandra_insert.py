from cassandra.cluster import Cluster
import time
cluster = Cluster()
session = cluster.connect()
session.set_keyspace('dev')
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
        session.execute(
            """
            INSERT INTO train (uid, mid, rate)
            VALUES (%s, %s, %s)
            """,
            (row[0], row[1], row[2])
        )

t = time.time()
print(t)
TimeTuple=time.localtime(time.time())
fmt='%Y-%m-%d %a %H:%M:%S'
test=time.strftime(fmt,TimeTuple)
print('time end:',test)
