#!/bin/python
#coding=utf-8
'''
1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。

2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。

3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。

例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。

4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。

5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
'''

###################1
def func(*nums):
    #return nums
    for i in nums:
        if isinstance(i,int):
	    pass
	else:
	    return "error!"

    length=len(nums)
    nums=list(nums)
    nums.sort()
    return nums[0],nums[-1]
print func(1,2,3,9,10)

###################2
def funcString(*s):
    l=[]
    for i in s:
        if isinstance(i,str):
	   
	   l.append(len(i))
	   pass
	else:
	    return "error!"
    l.sort()
    return l[-1]
print funcString("dsdsad","dsadsadewrewrew","dxb")



###################3
import re
def get_doc(module):
    return help(module)
dir_list=dir()
print get_doc(dir_list[-1])
###################4


import os
file_path=os.path.abspath("answer.py")
def get_text(f):
    ff=open(f,"r")
    lines=ff.readlines()
    ff.close()
    return lines
print get_text(file_path)


###################5
import os
cmd=os.getcwd()
def get_dir(floder):
    return os.listdir(floder)
print get_dir(cmd)

