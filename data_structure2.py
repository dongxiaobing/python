#!/bin/python
#coding=utf-8

import time
import linecache
#因为有些内容可能是空的，如果你想顺序取文本中的值，可能取不到，所以将内容作为键，将序列作为键值
data_keys=["mid","uid","username","date","source","url","content"]
keys={}
for k in range(len(data_keys)):
    key=data_keys[k]
    keys[key]=k
#print keys


f=linecache.getlines("data_structure2.txt")
#print f
#将每一行信息生成一个列表，并且添加到列表lines中
lines=[]
for x in f:
    lines.append(x.split('","'))
#print lines

#######################################1 输出用户总数
#遍历lines列表，取出每一项中的username
username_list=[]
for line in lines:
    #print line
    username_list.append(line[keys['username']])
#print username_list

#因为username_list中的值可能会重复，所以要去除重复之后，通过集合来实现，集中的值都是唯一的，就可以得到一共有多少用户了
username_list_set=set(username_list)
total_user_nums=len(username_list_set)
print "第一题一共有%d个用户"% total_user_nums

#######################################2 每一个用户的名字，生成一个列表
username_list=list(set(username_list))
print "第二题用户名字的列表为%s" %  username_list

#######################################3 有多少个在2012年11月份发布的消息
#print lines
#将发布时间生成一个列表，然后遍历这个列表，找出包含“2012-11”有多少
date_list=[]
for line in lines:
    #print line
    date_list.append(line[keys['date']])
#print date_list
def cmp_date(date):
    if "2012-11" in date:
        return True
count=0
for date in date_list:
    if cmp_date(date):
        count+=1
print "第三题一共有%d个在2012-11发出的消息" % count

#######################################4 有哪几天，将每一天按照从小到大的顺利排列
#print date_list
#需要分割日期和时间，将日期取出来
created_at=[]
for i in date_list:
    created_at.append(i.split(" ")[0])
created_at=set(created_at)
created_at=list(created_at)
created_at.sort()
print "第四题一共有这些天%s" % created_at


#######################################5 在哪个小时发布的数据最多
#需要分割日期和时间，将日期取出来
date_hour_list=[]
for h in date_list:
    date_hour_list.append(h.split(":")[0])
hour_list=[]
for h in date_hour_list:
    hour_list.append(h.split(" ")[1])
#print hour_list
total_by_hour = [(h,hour_list.count(str(h))) for h in xrange(0,24) ]
#print total_by_hour
total_by_hour.sort(key=lambda k:k[1],reverse=True)
#print total_by_hour
print "第五题 在第%s个小时，发的数据最多，一共发了%s个" % (total_by_hour[0][0],total_by_hour[0][1])


#######################################6 统计来源和次数
source_list=[]
for line in lines:
    #print line
    source_list.append(line[keys['source']])
#print source_list
set_source_list=set(source_list)
list_source_list=list(set_source_list)
list_tuple_source=[(s,source_list.count(s)) for s in list_source_list]
list_tuple_source.sort(key=lambda k:k[1],reverse=True )
print "第六题来源是%s的次数最多，为%s" % (list_tuple_source[0][0],list_tuple_source[0][1])


#######################################7 统计url中以“https://twitter.com/umiushi_no_uta”的有多少
url="https://twitter.com/umiushi_no_uta"
url_count=0
for line in lines:
    if line[keys["url"]].startswith(url):
        count+=1
print "第气题包含特定url的一共有",count

#######################################8 统计uid为573638104的用户一共发了多少微博
uid="573638104"
uid_list=[]
for line in lines:
    uid_list.append(line[keys['uid']])
uid_count=uid_list.count(uid)
print "第八题统计uid为573638104的用户一共发了%d微博" % uid_count

