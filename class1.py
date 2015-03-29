#!/bin/python
#coding=utf-8
'''
定义一个列表的操作类：Listinfo

包括的方法: 

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key() 

list_info = Listinfo([44,222,111,333,454,'sss','333'])
'''
class ListInfo():
    def __init__(self,l):
        self.list=l
    def add_key(self,keyname):
        if isinstance(keyname,str) or isinstance(keyname,int):
            self.list.append(keyname)
	    return self.list
    def get_key(self,num):
        if isinstance(num,int):
            return self.list[num]
    def update_list(self,list2):
        #if type(list2)==list:
        if isinstance(list2,list):
	    self.list.extend(list2)
	    #return self.list
    def del_key(self):
        del self.list[-1]
list_info=ListInfo([44,222,111,333,454,'sss','333'])	   
print list_info.add_key("dxb")
print list_info.add_key(123)
print list_info.list

print list_info.get_key(4)

list_info.update_list([1,2,3])
print list_info.list

list_info.del_key()
print list_info.list


'''
定义一个集合的操作类：Setinfo

包括的方法: 

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)
'''
class SetInfo():
    def __init__(self,my_set):
        self.my_set=my_set
    def add_setinfo(self,keyname):
        if isinstance(keyname,str) or isinstance(keyname,int):
	    self.my_set.add(keyname)
    def get_intersection(self,unioninfo):
        if isinstance(unioninfo,set):
	    return self.my_set & unioninfo
    def get_union(self,unioninfo):
        if isinstance(unioninfo,set):
	    return self.my_set | unioninfo
    def del_difference(self,unioninfo):
        if isinstance(unioninfo,set):
	    return self.my_set - unioninfo
s=set([1,2,3,4,5])
set_info=SetInfo(s)
set_info.add_setinfo(6)
print set_info.my_set

print set_info.get_intersection(set([1,2,7]))
print set_info.get_union(set([1,2,7]))
print set_info.del_difference(set([1,2,7]))

