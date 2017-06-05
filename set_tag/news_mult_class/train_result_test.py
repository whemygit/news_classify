#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

with open("pVect_array","r") as fr1:
    lines=fr1.readlines()
    for line in lines:
        aa=line.split('\x01')
        print aa
        print len(aa)

with open("vocablist", "r") as fr2:
    lines = fr2.readlines()
    for line in lines:
        ss = line.split('\x01')
        print ss
        print len(ss)

# if __name__ == '__main__':
#     pass