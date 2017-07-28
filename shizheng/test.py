#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import urllib
import time

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    a=['a','b','c']
    for x in a:
        if x=='b':
            pass
        else:
            print x

    q={}
    q[1]='a'
    print q
    print time.time()
    print time.strftime('%y-%m-%d',time.localtime(time.time()-24*60*60))

    d=[1,2,3]
    print sum(d)