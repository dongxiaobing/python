#coding=utf-8
import json
import sys
import time
reload(sys) 
sys.setdefaultencoding('utf-8')
import urllib2
from bs4 import BeautifulSoup
import re

xml_url="http://10.255.254.188:8390/?q=%D2%F0%C2%FC&pg=1&ps=60&ip=192.168.95.162&pid=20150330190649554825358648731959141&domain=search.dangdang.com&_url_token=5&vert=1&cate_type=0&platform=4&is_default_search=1&is_e_default=1&_new_tpl=1&session_id=49dad3ff31255cace1085299c79886bc&direct_brand=1&st=full&um=search_ranking&gp=cat_paths,label_id,clothes_size"

c=urllib2.urlopen(xml_url).read()
#print c
b=BeautifulSoup(c,"xml")
print b
"""
1.想看看搜索的切词是什么，如果是用正则表达式实现是这样的
"""
print type(c)
com=re.compile(r"<Term>(.*?)</Term>")
segment=com.search(c).groups()
print segment[0].decode("gbk")

"""
2.如果是想用beautifulsoup实现是这样的
"""




