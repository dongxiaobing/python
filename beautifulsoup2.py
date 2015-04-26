#coding=utf-8
from bs4 import BeautifulSoup
import sys
reload (sys)
sys.setdefaultencoding("utf8")
import re


f=open("xml.txt")
fc=f.read()
f.close()

"""
1.想看看搜索引擎的切词，如果使用正则表达式是这样实现的
"""
r_c=re.compile(r"<Term>(.*?)</Term>")
c=r_c.search(fc).groups()
print "use re module,output segment"
print c[0].decode("gbk")

"""
2.如果使用beautifulsoup是这样实现的
"""
b=BeautifulSoup(fc,"xml")
#print dir(b)
print "use beautifulsoup module,output segment"
print b.Term.string

"""
3.后台一共返回了多少商品
"""
print "total products"
print b.Count.string

"""
4.返回一个商品
"""
print b.product_name.string
x=b.product_name.string
b2=BeautifulSoup(x,"xml")
print b2.font.string
# print b.product_name.contents[0]

"""
5.返回所有的商品
"""
print "555"
b=BeautifulSoup(fc,"xml")
alls=b.findAll("product_name")
#rint alls
for i in alls:
    print i
    b3=BeautifulSoup(i,"xml")
    print "!!!"
    print b3.product_name.string
# print b.cost
#print b.findAll("Score")