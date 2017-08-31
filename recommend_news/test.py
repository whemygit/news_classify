#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import requests
from lxml import etree
import jieba
import time
import re
import chardet

reload(sys)
sys.setdefaultencoding("utf-8")

today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
yesterday=time.strftime('%Y-%m-%d',time.localtime(time.time()-86400))


def news_cut_outstop(news_text):
    stopwd=[line.strip().decode('utf-8') for line in open('D:/gitcode/mypython/R+python/my_news_classify/stopw.txt','r').readlines()]
    news_text=news_text.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
    seg_list=jieba.cut(news_text,cut_all=False)
    seg_list_outstop=[w for w in seg_list if w not in stopwd]
    return seg_list_outstop

def wangyi_title_segset():
    main_url='http://www.163.com/'
    title_xpath_rules='//div[@class="yaowen_news"]/div/ul/li/a/text()'
    resp=requests.get(main_url)
    detail=etree.HTML(resp.text)
    yaowen_title_list=detail.xpath(title_xpath_rules)
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

def intersect_keywd_set():
    wangyi_keywd_set=wangyi_title_segset()
    souhu_keywd_set=souhu_title_segset()
    keywd_set=wangyi_keywd_set&souhu_keywd_set
    return keywd_set

def title_url_list():
    main_url='http://news.sina.com.cn/hotnews/#2'
    resp=requests.get(main_url)
    # print resp.content
    detail=etree.HTML(resp.content)
    title_list=detail.xpath('//td[@class="ConsTi"]/a/text()')
    url_list=detail.xpath('//td[@class="ConsTi"]/a/@href')
    title_url_dict={}
    for i,title in enumerate(title_list):
        title_url_dict.update({title:url_list[i]})
    return title_url_dict

def recomend_news():
    keywd_set=intersect_keywd_set()
    keywd_list=list(keywd_set)
    title_url_dict=title_url_list()
    rec_news_dict={}
    for keywd in keywd_list:
        # print keywd
        for title in title_url_dict:
            if keywd in title:
                rec_news_dict.update({title_url_dict.get(title):title})
        keywd_list.remove(keywd)
    return rec_news_dict

def news_spider():
    rec_news_dict=recomend_news()
    for url in rec_news_dict:
        # print url
        if url.startswith('http://slide') or url.startswith('http://video') or url.startswith('http://news') or url.startswith('http://sports'):
            # print url
            continue
        url_split=url.split('/')
        if today in url_split or yesterday in url_split:
            # print url
            if today in url_split:
                new_date=today
            else:
                new_date=yesterday
            new_content=news_detail_spider(url)
            new_title=rec_news_dict.get(url)
            print url,new_title,new_date,new_content



def news_detail_spider(new_url):
    # new_url='http://news.sina.com.cn/s/wh/2017-08-21/doc-ifykcypq1380073.shtml'
    resp=requests.get(new_url)
    # print resp.content
    detail=etree.HTML(resp.content)
    print chardet.detect(resp.content)
    # new_title=detail.xpath('//*[@id="main_title"]/text()')[0]
    # print new_title
    new_content = etree.tostring(detail.xpath('//*[@id="artibody"]')[0], xml_declaration=True,
                              encoding='utf-8').encode()

    # new_content = detail.xpath('//*[@id="artibody"]/text()')[0]
    # print new_content
    # new_source=detail.xpath('//*[@id="page-tools"]/span/span[2]/a/text()')[0]
    # print new_source
    # new_date=detail.xpath('//*[@id="page-tools"]/span/span[1]/text()')[0].split(' ')[0]
    # new_date=re.findall('\d+',new_date)
    # new_date='-'.join(new_date)
    return new_content

# def main():
#     url_list=news_spider()
#     for new_url in url_list:
#         try:
#             new_title, new_date, new_source, new_content=news_detail_spider(new_url)
#             print new_title,new_date,new_source,new_url
#         except Exception as e:
#             print e

if __name__ == '__main__':
    keywd_set=intersect_keywd_set()
    for i in keywd_set:
        print i
