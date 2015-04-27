#coding=utf-8
from bs4 import BeautifulSoup
import sys
import urllib2
reload (sys)
sys.setdefaultencoding("utf8")
import re

"""
f=open("xml.txt")
fc=f.read()
f.close()
"""
xml_url="http://10.255.254.188:8390/?q=%D2%F0%C2%FC&pg=1&ps=60&ip=192.168.95.162&pid=20150330190649554825358648731959141&domain=search.dangdang.com&_url_token=5&vert=1&cate_type=0&platform=4&is_default_search=1&is_e_default=1&_new_tpl=1&session_id=49dad3ff31255cace1085299c79886bc&direct_brand=1&st=full&um=search_ranking&gp=cat_paths,label_id,clothes_size"

c=urllib2.urlopen(xml_url).read()

"""
1.想看看搜索引擎的切词，如果使用正则表达式是这样实现的
"""
r_c=re.compile(r"<Term>(.*?)</Term>")
c_re=r_c.search(c).groups()
print "use re module,output segment"
print c_re[0].decode("gbk")

"""
2.如果使用beautifulsoup是这样实现的
"""
contents=re.search(r"<result.*",c).group()
# print contents
# print type(contents)
b=BeautifulSoup(contents,"xml",from_encoding="gb18030")
print "use beautifulsoup module,output segment"
print b.Term.string

"""
3.后台一共返回了多少商品
"""
print "total products"
print b.TotalCnt.string

"""
4.返回一个商品名称
"""
print "used re"
print b.product_name.string
product_name=b.product_name.string
rrrr=re.search(r">(.*?)<.*>(.*)",product_name)
for i in rrrr.groups():
    print i,
    
"""
print "used beautifulsoup"
x=b.product_name.string
b2=BeautifulSoup(x,"xml")
print b2.font.string
print b2.get_text("font")
print b2.contents
"""

"""
5.返回所有商品的名称
"""
b=BeautifulSoup(contents,"xml",from_encoding="gb18030")
alls=b.findAll("product_name")
print alls
for i in alls:
    print type(i)
    print dir(i)
    print i.strings
    prduct_name_string=i.string
    rrrr=re.search(r">(.*?)<.*>(.*)",prduct_name_string)
    for y in rrrr.groups():
        print y,
    print "\n"
    
    





