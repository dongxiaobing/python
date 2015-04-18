import re

m=re.match("foo","fooo")
print m
print "@"
if m is not None:
    print m.group()
    print m.groups()
    
print re.search("foo","dxbfoofoo").group()


m=re.match('(\w\w\w)-(\d\d\d)',"abc-123")
print m.group()
print m.group(0)
print m.group(1)
print m.group(2)
print "!!"
print m.groups()
print m.groups()[0]
print m.groups()[1]




m=re.findall("dxb","123dxb123dxb")
print m


m=re.sub("dxb","DXB","dxb123dxb123")
print m

m=re.subn("dxb","DXB","dxb123dxb123")
print m

m=re.split(":","dxb:123:dxb:123")
print m