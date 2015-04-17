#coding=utf-8
from bs4 import BeautifulSoup
import urllib2
url_address="http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#xml"
u=urllib2.urlopen(url_address).read()
b=BeautifulSoup(u)
print b.title
print b.title.name
print b.title.string
print b.title.parent.name
print b.p
print b.p.get("class")
print b.a
all_a=b.findAll("a")
for i in all_a:
    print i.get("href") 
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
print tag
print type(tag)
print tag.name
tag.name="dxb"
print tag
print tag["class"]


xml_soup = BeautifulSoup('<p class="body strikeout"></p>','xml')
print xml_soup.p['class']

xml_soup = BeautifulSoup('<p class="body strikeout"></p>')
#print xml_soup.p['class']
tag=xml_soup.p
print tag
print tag.string
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
type(comment)
print comment
print soup.b.prettify()

