#coding=utf-8
"""
习题：

有10个刷卡机，代表建立10个线程，每个刷卡机每次扣除用户一块钱进入总账中，每个刷卡机每天一共被刷100次。账户原有500块。所以当天最后的总账应该为1500

用多线程的方式来解决，提示需要用到这节课的内容
"""
import threading

num=500
mlock=threading.Lock()
def a():
    for i in range(100):
        global num
        mlock.acquire()
        num+=1
        mlock.release()
l=[]
for x in range(10):
    t=threading.Thread(target=a)
    t.start()
    l.append(t)
for y in l:
    y.join()
print "total nums %s" % num