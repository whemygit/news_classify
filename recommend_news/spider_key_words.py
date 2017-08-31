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
    # yaowen_title_list=detail.xpath('//div[@class="news"]/p/a/text()')      搜狐要闻，单独抓，政治
    # yaowen_title_list=detail.xpath('//div[@class="list16"]/ul/li/a/strong/text()')  #搜狐strong，可单独抓
    yaowen_title_list = detail.xpath('//div[@class="list16"]/ul/li/a/text()')
    return yaowen_title_list

def wangyi_yaowen_titlelist():
    main_url = 'http://www.163.com/'
    _title_list = spider_yaowen_title(main_url)
    title_list = []
    for i in _title_list:
        if i not in title_list and i != ' 温度 |':
            title_list.append(i)
    return title_list

def key_wordsdict_generate():
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
    print key_words_dict
    sorted_dict = sorted(key_words_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_dict

def keywords_set_generate():
    title_list=wangyi_yaowen_titlelist()
    key_words_list=[]
    for i in title_list:
        for t in news_cut_outstop(i):
            if len(t)>=2:
                key_words_list.append(t)
    # return key_words_list
    keywords_set = set(key_words_list)
    return keywords_set

def wangyi_title_segset():
    main_url='http://www.163.com/'
    title_xpath_rules='//div[@class="yaowen_news"]/div/ul/li/a/text()'
    resp=requests.get(main_url)
    detail=etree.HTML(resp.text)
    yaowen_title_list=detail.xpath(title_xpath_rules)
    for i in yaowen_title_list:
        print i
    key_words_list = []
    for title in yaowen_title_list:
        for t in news_cut_outstop(title):
            if len(t) >= 2:
                key_words_list.append(t)
    keywords_set = set(key_words_list)
    return keywords_set

def souhu_title_segset():
    main_url='http://www.sohu.com/'
    title_xpath_rules=['//div[@class="news"]/p/a/text()','//div[@class="list16"]/ul/li/a/strong/text()','//div[@class="list16"]/ul/li/a/text()']
    resp=requests.get(main_url)
    detail=etree.HTML(resp.text)
    title_list = []
    for rule in title_xpath_rules:
        yaowen_title_list=detail.xpath(rule)
        for i in yaowen_title_list:
            title_list.append(i.strip())
    key_words_list = []
    for title in title_list:
        for t in news_cut_outstop(title):
            if len(t) >= 2:
                key_words_list.append(t)
    keywords_set = set(key_words_list)
    return keywords_set

now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
print now
print time.time()
print time.strftime('%Y-%m-%d',time.localtime(time.time()-86400))
print type(time.strftime('%Y-%m-%d',time.localtime(time.time()-86400)))

if __name__ == '__main__':
    a={'a':1,'b':2,'c':3}
    # print a
    # for i in a:
    #     print i
    # for i in a.itervalues():
    #     print i





