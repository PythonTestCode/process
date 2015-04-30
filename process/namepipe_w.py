import os

P_Name = './pipe'
if(os.access(P_Name, os.F_OK) == False):
	os.mkfifo(P_Name)

print "befor open wpipe"
fp_w = os.open(P_Name, os.O_WRONLY)
print "end open wpipe"

msg = ''

while(True):
	msg1 = raw_input('>')
	os.write(fp_w, msg1)
	if(msg1 == 'q'):
		break

os.close(fp_w)

