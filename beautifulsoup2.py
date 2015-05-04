#coding=utf-8
from bs4 import BeautifulSoup
import sys
import urllib2
reload (sys)
sys.setdefaultencoding("utf8")
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chardet
import urllib



"""
需求：输入一个搜索词，想得到所有的搜索结果，然后验证每个搜索结果中包含搜索关键字
步骤：
1.打开search.dangdang.com，输入搜索词，得到搜索之后的url,拼接url（search_url+&category_debug=1）
2.获得后台xml地址
3.查看关键字切词
4.后台一共返回了多少商品
5.返回一个商品名称
6.根据后台xml获得所有商品,验证所有商品中包含搜索关键字
"""


"""
1.取得后台xml地址
"""

dr = webdriver.Firefox()
base_url = "http://search.dangdang.com"
dr.get(base_url)
dr.find_element_by_id("key_S").send_keys(u"茵曼")
dr.find_element_by_id("key_S").send_keys(Keys.ENTER)
dr.implicitly_wait(10)
search_url=dr.current_url
dr.quit()
     
debug_url=search_url+"&category_debug=1"
print "debug url的地址是:%s " % debug_url

"""
2.根据debug_url的页面源码获得后台xml地址
"""


debug_url="http://search.dangdang.com/?key=%D2%F0%C2%FC&category_debug=1"
search_contents=urllib2.urlopen(debug_url).read()
#debug url源码的编码
print search_contents
    
print "debug url的源码是:%s" % search_contents
    
#发现debug url里面的内容有乱码，检查下该内容的编码是什么？
print chardet.detect(search_contents)
    
search_contents=search_contents.decode("gbk").encode("utf8")
print "#"*100
print search_contents
print chardet.detect(search_contents)
  
#因为后台xml地址所在的内容并不是真实的xml格式，所以现在还不能用beautifulsoup来解决  
result=re.search(r"mix:<a href='(.*)'",search_contents)
    
    
xml_url=result.groups(1)[0]
print "后台xml url的地址是:%s" % xml_url


 
"""
3.想看看搜索引擎的切词
"""

#如果使用正则表达式是这样实现的
xml_url="http://10.255.254.188:8390/?q=%D2%F0%C2%FC&pg=1&ps=60&ip=192.168.95.162&pid=20150330190649554825358648731959141&domain=search.dangdang.com&_url_token=5&vert=1&cate_type=0&platform=4&is_default_search=1&is_e_default=1&_new_tpl=1&session_id=49dad3ff31255cace1085299c79886bc&direct_brand=1&st=full&um=search_ranking&gp=cat_paths,label_id,clothes_size"
c=urllib2.urlopen(xml_url).read()
r_c=re.compile(r"<Term>(.*?)</Term>")
c_re=r_c.search(c).groups()
print "use re module,output segment"
print c_re[0].decode("gbk")


#如果使用beautifulsoup是这样实现的
xml_url="http://10.255.254.188:8390/?q=%D2%F0%C2%FC&pg=1&ps=60&ip=192.168.95.162&pid=20150330190649554825358648731959141&domain=search.dangdang.com&_url_token=5&vert=1&cate_type=0&platform=4&is_default_search=1&is_e_default=1&_new_tpl=1&session_id=49dad3ff31255cace1085299c79886bc&direct_brand=1&st=full&um=search_ranking&gp=cat_paths,label_id,clothes_size"
c=urllib2.urlopen(xml_url).read()


#使用beautifulsoup来解析xml内容
b=BeautifulSoup(c,"xml")
print b.is_xml
print b.prettify()
print b.Term

#虽然识别为xml，但是还是解析不了xml中的标签
#解决办法一：使用ElementTree
from xml.etree import ElementTree
from lxml import etree as ET
from io import BytesIO
format_c=ET.tostring(ET.parse(BytesIO(c)), encoding="utf-8")
root=ElementTree.fromstring(format_c)
seg_node = root.getiterator("Term")  
print seg_node[0].text

#解决办法二：使用re和beautifulsoup
contents=re.search(r"<result.*",c).group()
b=BeautifulSoup(contents,"xml",from_encoding="gb18030")
print "use beautifulsoup module,output segment"
print b.Term
print b.Term.string
print dir(b)

 
 
"""
4.后台一共返回了多少商品
"""
 
contents=re.search(r"<result.*",c).group()
b=BeautifulSoup(contents,"xml",from_encoding="gb18030")
print "total products"
print "一共会展示%s件商品 " % b.TotalCnt.string

 
"""
5.返回一个商品名称
"""

contents=re.search(r"<result.*",c).group()
b=BeautifulSoup(contents,"xml",from_encoding="gb18030")
print "used re"
print b.product_name.string
product_name=b.product_name.string
rrrr=re.search(r">(.*?)<.*>(.*)",product_name)
for i in rrrr.groups():
    print i,

   
contents=re.search(r"<result.*",c).group()
print contents
b=BeautifulSoup(contents,"xml",from_encoding="gb18030")
print "used beautifulsoup"
x=b.product_name.string
b2=BeautifulSoup(x,"xml")
print b2.font.string
print b2.get_text("font")
print b2.contents

 
"""
6.返回所有商品的名称
"""

print "66666666"
xml_url="http://10.255.254.188:8390/?q=%D2%F0%C2%FC&pg=1&ps=60&ip=192.168.95.162&pid=20150330190649554825358648731959141&domain=search.dangdang.com&_url_token=5&vert=1&cate_type=0&platform=4&is_default_search=1&is_e_default=1&_new_tpl=1&session_id=49dad3ff31255cace1085299c79886bc&direct_brand=1&st=full&um=search_ranking&gp=cat_paths,label_id,clothes_size"
c=urllib2.urlopen(xml_url).read()
contents=re.search(r"<result.*",c).group()

print "##"
# print contents

b=BeautifulSoup(contents,"xml",from_encoding="gb18030")
alls=b.findAll("product_name")
#print alls
all_prducts_list=[]
for i in alls:
    prduct_name_string=i.string
    rrrr=re.search(r">(.*?)<.*>(.*)",prduct_name_string)
    p_name=rrrr.group(1)+rrrr.group(2)
    all_prducts_list.append(p_name)
print "all products"
print all_prducts_list  #乱码



#查看编码
print chardet.detect(str(all_prducts_list))

tmp1=str(all_prducts_list).decode("unicode-escape")

#The Python-specific encoding unicode_escape is a dummy（傻瓜） encoding that converts all non-ASCII characters into their \uXXXX representations.


print type(tmp1)
print tmp1

    
for i in all_prducts_list:
    print i
    flag= u"茵曼" in i
    assert flag==True




