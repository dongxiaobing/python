#!/bin/python
#coding=utf-8
'''
1.定义一个func(url,folder_path)，获取url地址的内容，保存到folder_path的文件目录下，并随机生成一个文件名
'''
import urllib2
import random
import time
import os
def func1(url,folder_path):
    #if not url.startswith("http://") and not url.stardswith("https://"):
    if not (url.startswith("http://") or url.startswith("https://")):
        return u"网页类型错误"
    #file_name="dxb_%s" % random.randrange(1000)
    file_name="dxb_%s" % time.time()
    file_path=os.path.join(folder_path,file_name)
    try:
        f=urllib2.urlopen(url)
	content=f.read()
    except Exception,e:
        print e
    else:
        f2=open(file_path,'w')
	f2.write(content)
	f2.close()
    return file_path
print func1("http://126.com","/tmp")

'''
2.定义一个func(folder_path)，合并该目录下的所有文件，生成一个all.txt
'''
def marge(folder_path):
    if os.path.isfile(folder_path):
        return u"不是目录，请输入一个目录"
    #print os.listdir(folder_path)
    for i in os.listdir(folder_path):
	file_path=os.path.join(folder_path,i)
	if os.path.isdir(file_path):
	    marge(file_path)
       	else:
	    f1=open(file_path,"rb")
	    content=f1.read()
	    f1.close()
	    f2=open("all.txt","ab+")
	    f2.write(content)
	    f2.close()
print marge("/tmp/test")

'''
3.定义一个func(url),分析该url内容有多少个链接
'''
def func3(url):
    content=urllib2.urlopen(url).read()
    return len(content.split("<a href"))-1
print func3("http://www.baidu.com")

'''
4.定义一个func(url),获取？后的参数，并返回一个dict
assert('http://url/api?param=2&param2=4') == {"param1":"2","param2":"4"}
'''
import urlparse
def func4(url):
    result=urlparse.urlparse(url)
    first_dict=urlparse.parse_qs(result.query)
    list=[(x,y[0]) for x,y in first_dict.items()]
    return dict(list)
print func4('http://url/api?param=2&param2=4')

'''
5.定义一个func(folder)，删除该folder下的所有文件
'''
def delete_file(folder):
    if not os.path.exists(folder):
        return u"该目录不存在"
    for i in os.listdir(folder):
        file_path=os.path.join(folder,i)
	if os.path.isdir(file_path):
	    delete_file(file_path)
	else:
	    os.remove(file_path)
delete_file("/tmp/test")
