import os

P_Name = './pipe'
if(os.access(P_Name, os.F_OK) == False):
	os.mkfifo(P_Name)

print "befor open rpipe"
fp_r = os.open(P_Name, os.O_RDONLY)
print "end open rpipe"

while(True):
	msg = os.read(fp_r, 1024)

	if(msg == ''):
		break
	print "get msg:", msg
	if(msg == 'q'):
		print 'quit'
		break
os.close(fp_r)

