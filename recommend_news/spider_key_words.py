#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import re
import time
import requests
from lxml import etree
import json
import torndb
import jieba
import operator

reload(sys)
sys.setdefaultencoding("utf-8")

def news_cut_outstop(news_text):
    stopwd=[line.strip().decode('utf-8') for line in open('D:/gitcode/mypython/R+python/my_news_classify/stopw.txt','r').readlines()]
    news_text=news_text.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
    seg_list=jieba.cut(news_text,cut_all=False)
    seg_list_outstop=[w for w in seg_list if w not in stopwd]
    return seg_list_outstop

def spider_yaowen_title(main_url):
    resp=requests.get(main_url)
    # print resp.text
    detail=etree.HTML(resp.text)
    yaowen_title_list=detail.xpath('//div[@class="yaowen_news"]/div/ul/li/a/text()')
    return yaowen_title_list

def wangyi_yaowen_titlelist():
    main_url = 'http://www.163.com/'
    _title_list = spider_yaowen_title(main_url)
    title_list = []
    for i in _title_list:
        if i not in title_list and i != ' 温度 |':
            title_list.append(i)
    return title_list

def key_words_generate():
    title_list=wangyi_yaowen_titlelist()
    key_words_dict={}
    for i in title_list:
        print i
        for t in news_cut_outstop(i):
            # print t,len(t)
            if len(t)>=2:
                if t not in key_words_dict:
                    key_words_dict.update({t:1})
                else:
                    key_words_dict[t]+=1
    return key_words_dict


if __name__ == '__main__':
   a= key_words_generate()
   print a
   for k,v in a.items():
       print k,v

   sorted_dict = sorted(a.iteritems(), key=operator.itemgetter(1), reverse=True)
   print sorted_dict
   for i in sorted_dict:
       print i[0],i[1]

   # ss=[u'\u4e2d\u56fd\u5171\u4ea7\u515a']
   # print ss[0]