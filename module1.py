#!/bin/python
#coding=utf-8
'''
习题一：
 1.1 用time模块获取当前的时间戳.
 1.2 用datetime获取当前的日期，例如：2013-03-29
 1.3 用datetime返回一个月前的日期：比如今天是2013-3-29 一个月前的话：2013-02-27
'''
import time
import datetime
#1.1
print time.time()

#1.2
print datetime.date.today()

#
now_date=datetime.date.today()
before_month_date=datetime.timedelta(days=30)
print now_date-before_month_date

'''
 习题二:
 1 用os模块的方法完成ping www.baidu.com 操作。
 2 定义一个函数kouzhang(dirpwd)，用os模块的相关方法，返回一个列表，列表包括：dirpwd路径下所有文件不重复的扩展名，如果有2个".py"的扩展名，则返回一个".py"。
'''
import os
#1
#os.system("ping -c 5 www.baidu.com")

#2

'''
 习题三：
 定义一个函数xulie(dirname,info) 参数：dirname:路径名，info:需要序列化的数据，功能：将info数据序列化存储到dirname路径下随机的文件里。  
'''
import pickle
import time
import random
def xulie(dirname,info):
    if not os.path.exists(dirname):
        return u"dirname不存在"
    file_name="dxb_%s" % random.randrange(1000)
    file_path=os.path.join(dirname,file_name)
    xulie_date=pickle.dumps(info)
    f=open(file_path,"w")
    f.write(xulie_date)
    f.close()

    f2=open(file_path,"r")
    content=f2.read()
    f2.close()
    return pickle.loads(content)
    #return file_path
print xulie("/tmp","[1,2,3]")
