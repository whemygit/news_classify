#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import re
import time
import requests
from lxml import etree
import json

reload(sys)
sys.setdefaultencoding("utf-8")

headers={"Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cookie":"connect.sid=s%3AczMMktBdi_Mk81uG64V0KEsUijODtK1H.YgjRRJIFbvpG4pFsqtB2ktCmtLySDEnjZHYHSl8xH2g; cookie=zh",
    "Host":"media.yeesight.com",
    "Proxy-Connection":"keep-alive",
    "Referer":"http://media.yeesight.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"}

headers2={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cookie":"connect.sid=s%3AczMMktBdi_Mk81uG64V0KEsUijODtK1H.YgjRRJIFbvpG4pFsqtB2ktCmtLySDEnjZHYHSl8xH2g; cookie=zh",
    "Host":"media.yeesight.com",
    "Proxy-Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

category_dict={"1002":"shizheng",
        "1003":"shehui",
        "1004":"jingji",
        "1007":"keji",
        "1010":"chanye",
        "1015":"lvyou",
        "1020":"jiaoyu",
        "1021":"wenhua",
        "1032":"yule",
        "1038":"tiyu"}

# main_url='http://media.yeesight.com/news/news/industryCategory?isDefault=1&token=&categoryId=1002&mediaType=news&idList=&countryName=&mediaLevel=&mediaList=&pageNo=1&pageSize=15&fieldName=pubdate&order=&_='

def get_news_urllist(main_url):
    resp=requests.get(main_url,headers=headers)
    doc=etree.HTML(resp.text)
    news_uuid=doc.xpath('//div[@class="news2-item"]/@uuid')
    news_url=['http://media.yeesight.com/information_details/information_details2?informationId='+new_uuid for new_uuid in news_uuid]
    return news_url

def get_news_detail(main_url):
    for new_url in get_news_urllist(main_url):
        resp=requests.get(new_url,headers=headers2)
        detail=etree.HTML(resp.text)
        try:
            new_title=detail.xpath('//*[@id="item_1"]/div[1]/text()')[0]
            # print new_title
            # print new_title[0]
            new_text=detail.xpath('//*[@id="item_1"]/div[3]/p/text()')[0]
            # print new_text[0]
        except IndexError:
            print 'failed'
            continue
        yield new_url,new_title,new_text

def main():
    for item in category_dict:
        with open('corpus/'+category_dict.get(item),'w') as fw:
            for page in range(1,16):
                main_url='''http://media.yeesight.com/news/news/industryCategory?isDefault=1&token=&categoryId=%s&mediaType=news&idList=&countryName=&mediaLevel=&mediaList=&pageNo=%s&pageSize=15&fieldName=pubdate&order=&_='''%(item,page)
                info = get_news_detail(main_url)
                for url,title,content in info:
                    news_info = dict()
                    news_info['url']=url
                    news_info['title'] = title
                    news_info['content'] = content
                    news_info=json.dumps(news_info)
                    fw.write(news_info+'\n')
                    print url, title

if __name__ == '__main__':
    main()
    # info=get_news_detail(main_url)
    # for url,title,text in info:
    #     print url,title
