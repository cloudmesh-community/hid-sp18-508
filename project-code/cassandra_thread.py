import threading
from cassandra.cluster import Cluster
import time
cluster = Cluster()
session = cluster.connect()
session.set_keyspace('dev')


exitFlag = 0
PER_INSERT = 10000
TIMES  = 1000
file = open('casandra_thread.txt', 'a')
class myThread1(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        insert(self.name, self.counter, TIMES)
        print("Exiting " + self.name)

class myThread2(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        search(self.name, self.counter, TIMES)
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
            session.execute("INSERT INTO test (uid) VALUES (%s)", [uid])  # right

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
            future = session.execute("SELECT * FROM test WHERE uid=%s", [uid])
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

