from multiprocessing import Process,Value,Array, Manager
import time
import os

def clild_func(g_value, g_ay, g_d, ar):
	g_value.value = ar
	g_ay[ar] = ar*ar
	g_d[ar] = ar+ar
	print 'g_value.value=', g_value.value

listp = []

g_va = Value('i', 0)

g_ay = Array('i', range(10))

ma = Manager()

g_dict = ma.dict()

print "init g_va=%d\ng_ay=%s" % (g_va.value, g_ay[:])
print 'g_dict=', g_dict

for i in range(10):
	p = Process(target=clild_func,args=(g_va,g_ay, g_dict,i))
	p.start()
	listp.append(p)

for i in range(10):
	listp[i].join()
print g_va.value
print g_ay[:]
print g_dict



