#!/bin/python
#coding=utf-8
'''
1 用lambda和filter完成下面功能：输出一个列表，列表里面包括：1-100内的所有偶数。（提示：可以用filter,lambda）
'''
print filter(lambda x:x%2==0,range(1,101))

'''
2 用位置匹配，关键字匹配，收集匹配(元组收集,字典收集)分别写4个函数，完成功能；

传递3个列表参数：

[1,2,3],[1,5,65],[33,445,22]

返回这3个列表中元素最大的那个，结果是：445
'''
def locate_func(l1,l2,l3):
    l1.sort()
    l2.sort()
    l3.sort()
    max_list=[]
    max_list.append((l1[-1],l2[-1],l3[-1]))
    return max_list[0][2]
print locate_func([1,2,3],[1,5,65],[33,445,22])

        
def guanjianzi_func(l1=[1,2,3],l2=[1,5,65],l3=[33,445,22]):
    l1.sort()
    l2.sort()
    l3.sort()
    max_list=[]
    max_list.append((l1[-1],l2[-1],l3[-1]))
    return max_list[0][2]
print guanjianzi_func()

def kargs_func(*kargs):
    l1=kargs[0]
    l2=kargs[1]
    l3=kargs[2]
    l1.sort()
    l2.sort()
    l3.sort()
    max_list=[]
    max_list.append((l1[-1],l2[-1],l3[-1]))
    return max_list[0][2]
print kargs_func([1,2,3],[1,5,65],[33,445,22])

def keys_func(**keys):
    l=[]
    for i in keys.values():
        l.append(i)
    l1=l[0]
    l2=l[1]
    l3=l[2]
    l1.sort()
    l2.sort()
    l3.sort()
    max_list=[]
    max_list.append((l1[-1],l2[-1],l3[-1]))
    max_list=list(max_list[0])
    max_list.sort()
    return max_list[-1]
print keys_func(key1=[1,2,3],key2=[1,5,65],key3=[33,445,22])

'''
3 递归函数解释，用自己的话说明这个递归函数的工作流程。

def func1(i):
        if i<100:
                        return i + func1(i+1)
                                return i
                                print func1(0)
'''
