import os
from multiprocessing import Queue, Process, Lock
import time

Qmsg = Queue()

lock = Lock()
def clild_func(name):
	print "clild=%d acquire lock" % name
	lock.acquire()
	print "clild=%d acquired lock" % name
	Qmsg.put('clild_' + str(name) + '_msg_'  + '_1:pid=' + str(os.getpid()))
	time.sleep(1)
	Qmsg.put('clild_' + str(name) + '_msg_'  + '_2:pid=' + str(os.getpid()))
	lock.release()
	print "clild=%d release lock" % name


listp = []

for i in range(10):
	p = Process(target=clild_func, args=(i,))
	p.start()
	listp.append(p)

while(True):
	msg = Qmsg.get()
	print msg

for i in range(10):
	listp[i].join()

