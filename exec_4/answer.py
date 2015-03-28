#!/bin/python
#coding=utf-8
'''
1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。
'''
def get_num(num):
    l=[]
    for i in num:
        if not isinstance(i,int):
	    return "error!"
	else:
	    if i%2 == 0:
	        l.append(i)
    return l
num=[1,2,3,4,5,6,7,8,9]
print get_num(num)


'''
2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。
'''
import urllib2
def get_page(url):
    f=urllib2.urlopen(url)
    contens=f.read()
    return contens
url="http://www.baidu.com"
print get_page(url)

'''
3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
'''
def func(*keys):
    max_list=[]
    for i in keys:
        i.sort()
        max_list.append(i[-1])
    return max_list	    
print func([1,2,3],[4,5,6])


'''
4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。
'''
import os
def get_dir(f):
    dir_list=[]
    file_dir_list=os.listdir(f)
    for i in file_dir_list:
        full_path=f+"/"+i
        if os.path.isdir(full_path):
	    dir_list.append(i)
    return dir_list
path_dir="/Users/dongxiaobing/git"
print get_dir(path_dir)
