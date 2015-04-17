#coding=utf-8
import sys   
import ConfigParser
reload(sys)  
sys.setdefaultencoding('utf8')  

def get_search_data(data):
    conf = ConfigParser.ConfigParser()
    conf.read("coding.conf")
    test_data=conf.items(data)
    return test_data
test_data=get_search_data("English")
for i in test_data:
    print type(i[1]) #str
    i1=i[1].decode()#unicode
    print type(i1)
    print i1       #输出中文
    


#写入中文
import os
z1="我"
z2="是"
z3="董小兵"

f=open("coding2.conf","w")
f.write("%s%s" % (z1,os.linesep))
f.write("%s%s" % (z2,os.linesep))
f.write("%s%s" % (z3,os.linesep))
f.close()

f=open("coding2.conf","r")
for i in f.readlines():
    print i