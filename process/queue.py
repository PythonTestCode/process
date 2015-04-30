import os
from multiprocessing import Queue, Process
import time

Qmsg = Queue()

def clild_func(name):
	while(True):
		msg = Qmsg.get()
		print "get msg =", msg
		if(msg == 'q'):
			break
#		print msg, 'finish'

p = Process(target=clild_func, args=(1,))
p.start()

while(True):
	msg = raw_input('enter:')
	Qmsg.put(msg)
	if(msg == 'q'):
		break
	time.sleep(1)

p.join()

