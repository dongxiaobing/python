#coding=utf-8
"""
习题一：已知列表 info = [1,2,3,4,55,233]

生成6个线程对象,每次线程输出一个值，最后输出："the end"。
"""
import threading
info=[1,2,3,4,55,233]

def test(i):
    print i
t_list=[]
for i in info:
    th=threading.Thread(target=test,args=[i])
    #th.start()
    t_list.append(th)
    th.start()
for i in t_list:
    i.join()
print "the end"
    
    
"""
习题二：已知列表 urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 用多线程的方式分别打开列表里的URL，并且输出对应的网页标题和内容,输出网页的http状态码。。
"""    
import urllib2
urlinfo=['http://www.sohu.com','http://www.163.com','http://www.sina.com']

def run(i):
    u=urllib2.urlopen(i)
    contents=u.read()
    u.close()
    print "title ",i
    print "contents ",contents
    print u.code
for i in urlinfo:
    th=threading.Thread(target=run,args=[i])
    th.start()