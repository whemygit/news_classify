#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

#使用朴素贝叶斯来发现地域相关的用词
import feedparser
ny=feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
ny['entries']
print len(ny['entries'])