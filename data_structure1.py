#!/bin/python
#coding=utf-8

#1.1
a="aAsmr3idd4bgs7Dlsf9eAF"
print a.swapcase()

#1.2
l=[]
for x in a:
    if x.isdigit():
        l.append(x)
print ''.join(l)

#1.3
b=a.lower()
print b
print set(b)

print dict([(x,b.count(x)) for x in set(b)])

#1.4
a_list=list(a)
print set(a_list)
set_list=list(set(a_list))
print set_list
set_list.sort(key=a_list.index)
print ''.join(set_list)

#1.5
print a[::-1]


#1.6
l=sorted(a)
#print l

a_upper_list=[]
a_lower_list=[]

for x in l:
    if x.isupper():
        a_upper_list.append(x)
    if x.islower():
        a_lower_list.append(x)
print a_upper_list
print a_lower_list
for x in a_upper_list:
    print "#####,",x.lower()
    if x.lower() in a_lower_list:
        a_lower_list.insert(a_lower_list.index(x.lower()),x)
print a_lower_list


#1.7
search='bgs7D'
for x in search:
   if x not in a:
       break
   else:
       pass
else:
    print "True"

#1.8
l=['boy','girl','bird','dirty']
l_str=''.join(l)
print l_str
#search='bgs7D'
for x in l_str:
   if x not in a:
       break
   else:
       pass
else:
    print "True"



#2
import os
this_str=os.popen("python -m this").read()
this_str2=this_str.replace("\n",'').replace(" ",'')
print this_str2

be_count=this_str2.count("be")
print be_count

#3.
size=102324123499123
print size/1024
print size>>10 #2**10=1024

print size/1024/1024
print size>>20 #2**20


#4
#b=['1','2','3']
b=[1,2,3,6,8,9,10,14,17]
print str(b)[1:-1].replace(", ",'')
