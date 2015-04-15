#!/bin/python

import getopt

import sys

try:

    options,args=getopt.getopt(sys.argv[1:],"hp:i:",["help","ip=","port="])

except getopt.GetoptError:

    exit(1)



print options


print "@"
print args


for name,value in options:

    if name in ("-i","--ip"):

        print "ip is %s " % value

    if name in ("-p","--port"):

        print "port is %s " % value
