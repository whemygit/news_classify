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

# main_url='http://sports.cri.cn/focus/index-2.html'
def get_news_urllist(main_url):
    resp=requests.get(main_url)
    print resp.text
    doc=etree.HTML(resp.text)
    news_uuid=doc.xpath('//h4/a/@href')
    news_url=['http://sports.cri.cn'+new_uuid for new_uuid in news_uuid]
    return news_url


def get_news_detail(main_url):
    for new_url in get_news_urllist(main_url):
        resp=requests.get(new_url)
        detail=etree.HTML(resp.text)
        new_title=detail.xpath('//*[@id="goTop"]/text()')[0]
        # print new_title
        new_text=''.join(i for i in detail.xpath('//*[@id="abody"]/p/text()'))
        # print new_text
        yield new_url,new_title,new_text


def main():
    with open('corpus/tiyu','w') as fw:
        for page in range(2,22):
            main_url='''http://sports.cri.cn/focus/index-%s.html'''%page
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
    # get_news_detail()
    # get_news_urllist(main_url)
