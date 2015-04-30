import os
import time
p = os.pipe()
p1 = os.pipe()
pid = os.fork()

if(pid == 0):
	os.close(p[1])
	while True:
		msg = os.read(p[0], 1024)
		print 'child process get msg:', msg
		if(msg == 'q'):
			os.close(p[0])
			break
else:
	os.close(p[0])
	while True:
		str1 = raw_input("enter:")
		os.write(p[1], str1)
		if(str1 == 'q'):
			os.close(p[1])
			os.wait()
			break
		time.sleep(1)

	 

