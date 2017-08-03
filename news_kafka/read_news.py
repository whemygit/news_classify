#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import json
import time

reload(sys)
sys.setdefaultencoding("utf-8")

with open('news_17-07-31 (2)','r') as fr:
    for line in fr.readlines():
        print line
        print type(line)
        line_dict=json.loads(line)
        print line_dict
        print line_dict['title']
        break
# if __name__ == '__main__':
#     pass