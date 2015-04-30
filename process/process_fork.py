import os
import time
print "pid =", os.getpid()

tmp = 10
ret = os.fork()
if(ret == 0):
	print 'C pid=', os.getpid()
	time.sleep(1)
else:
	tmp = 0
	print 'P pid=', os.getpid(), 'C pid=', ret
#os.wait()

print 'pid = ', os.getpid(), 'tmp=', tmp
