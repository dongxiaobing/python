#!/bin/python
#coding=utf-8
'''
题目一： 写一个网页数据操作类。完成下面的功能：

提示：需要用到urllib模块

get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int 

get_htmlcontent() 获取网页的内容。返回类型:str

get_linknum()计算网页的链接数目。
'''
import urllib2
class Page():
    def __init__(self,url):
        self.url=url
        self.handle=urllib2.urlopen(self.url)
    def get_httpcode(self):
	return self.handle.code
    def get_htmlcontent(self):
        return self.handle.read()
    def get_linknum(self):
        content=self.get_htmlcontent()
	self.link_num=len(content.split("<a href"))-1
	return self.link_num
url="http://www.baidu.com"
p=Page(url)
print p.get_httpcode()
print p.get_htmlcontent()
print p.get_linknum()
