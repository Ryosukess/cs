#-*-coding:UTF-8-*-

'''
import thread
from time import sleep
lk = thread.allocate_lock()
g_FinishCount = 0
def loop(id):
	lk.acquire()
 	for i in range(0,4):
		print"Thread",id,"working"
		sleep(1)
	lk.release()
 	global g_FinishCount
	g_FinishCount = g_FinishCount + 1

thread.start_new_thread(loop,(1,))
thread.start_new_thread(loop,(2,))
thread.start_new_thread(loop,(3,))
while g_FinishCount < 3:
	sleep(1)
'''


'''
class Person(object):

	def __init__(self,name,sex):
		self.name = name
		self.sex = sex
	def get_name(name):
		return self.name
	pass

p1=Person("yuhang","male")
print(p1.get_name())
'''

class Number:
	def __init__(self,base):
		self.base = base
	def double(self):
		return self.base * 2
	def triple(self):
		return self.base * 3

x = Number(2)
print x.double()




