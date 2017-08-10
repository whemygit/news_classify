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
    "Connection":"keep-alive",
    "Cookie":"UM_distinctid=15daaea044060e-0600ce68bf14bd-4e47052e-1fa400-15daaea044162f; cnsuuid=9693639a-403e-81ef-8301-4b5c2d45c55e1330.582074663635_1501827142507; JSESSIONID=aaaVQbty0dQOxdzVq4R2v; __jsluid=1a98acfe2bf27aaf8100ea2933c5e301",
    "Host":"channel.chinanews.com",
    "Referer":"http://www.chinanews.com/society/",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

main_url='http://channel.chinanews.com/cns/s/channel:sh.shtml?pager=1&pagenum=20&_='
def get_news_urllist(main_url):
    resp=requests.get(main_url,headers=headers)
    s=resp.text
    s = re.sub(r'var specialcnsdata = ', '', s)
    s=re.sub(r'\;','',s)
    s=s.strip()
    s_dict=json.loads(s.strip())
    for i in s_dict.values()[0]:
        new_url=i.get('url')
        new_title=i.get('title')
        yield new_url,new_title


def get_news_detail(new_url):
    resp=requests.get(new_url)
    detail=etree.HTML(resp.content)
    new_text=detail.xpath('//*[@id="cont_1_1_2"]/div[6]/p/text()')
    new_text=''.join(i for i in detail.xpath('//*[@id="cont_1_1_2"]/div[6]/p/text()'))
    return new_text

category_dict={"cj":"caijing",
    "cul":"wenhua",
    "yl":"yule",
    "life":"shenghuo",
    "gn":"shizheng",
    "auto":"qiche",
    "ty":"tiyu",
    "sh":"shehui"}


def main():
    for item in category_dict:
        with open('corpus'+category_dict.get(item),'w') as fw:
            for page in range(1,41):
                main_url='''http://channel.chinanews.com/cns/s/channel:%s.shtml?pager=%s&pagenum=20&_='''%(item,page)
                for url, title in get_news_urllist(main_url):
                    content=get_news_detail(url)
                    news_info = dict()
                    news_info['url']=url
                    news_info['title'] = title
                    news_info['content'] = content
                    news_info=json.dumps(news_info)
                    fw.write(news_info+'\n')
                    print url, title

def read():
    with open('corpus/shehui','r') as fr:
        lines=fr.readlines()
        for line in lines:
            print json.loads(line).get("content")
            break

if __name__ == '__main__':
    # read()
    main()
    # get_news_detail()
    # for new_url,new_title in get_news_urllist(main_url):
    #     print new_title
    # new_url="http://www.chinanews.com/sh/2017/08-04/8295772.shtml"
    # get_news_detail(new_url)
