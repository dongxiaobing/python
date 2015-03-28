#!/bin/python
#coding=utf-8

'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''
def func1(name):
    if isinstance(name,str):
        return name.capitalize()
    else:
        return "error"
print func1("dxb")

"""
2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"

"""
import string
def func2(name,callback=None):
    if callback==None:
        return name
    else:
        return callback(name)
print func2("dxb")
print func2("dxb",string.upper)
print func2("DXB",string.lower)


"""
3.定义一个func(*kargs),效果如下。

l = func(1,2,3,4,5)
for i in l:
	print i,
	#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
	print i
	#输出 5 3 4 5 6
"""
def func3(*k):
    return k
l=func3(1,2,3,4,5)
for i in l:
    print i,
print ''
"""
4.定义一个func(*kargs)，该函数效果如下。
assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None
"""
def func4(*kargs):
    l=[]
    len_list=[]
    for i in kargs:
        if isinstance(i,str):
	    l.append(i)
    if l ==[]:
        return None
    for i in l:
        len_list.append(len(i))
    min_len=min(len_list)
    for i in l:
        if len(i)==min_len:
	    return "%s" % i
print func4(111,222,'xixi','hahahaha')
print func4(111,222)

"""
5.定义一个func(name=None,**kargs),该函数效果如下。
assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"
"""
def func5(name=None,**keys):
    l=["%s:%s" % (x,y) for x,y in keys.items()]
    l.insert(0,name)
    #return l
    return ','.join(l)
print func5("lilei",years=10,body_weight=20)
