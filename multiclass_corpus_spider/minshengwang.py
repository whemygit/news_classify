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

def get_news_urllist(main_url):
    resp=requests.get(main_url)
    doc=etree.HTML(resp.text)
    news_url=doc.xpath('//div[@class="pagmainL1"]/ul/li/a/@href')
    news_url=['http://www.mszsx.com'+new_url for new_url in news_url]
    return news_url

def get_news_detail(main_url):
    for new_url in get_news_urllist(main_url):
        resp=requests.get(new_url)
        detail=etree.HTML(resp.content)
        new_title=detail.xpath('//div[@class="news_title"]/text()')[0]
        # print new_title
        # break
        new_date=detail.xpath('//div[@class="news_time"]/text()')[0]
        new_date=new_date.split('  ')[0].split('：')[1].split(' ')[0]
        # print new_date
        # break
        new_source = '民生网'
        new_text=detail.xpath('//*[@id="zoom"]/p/text()')
        new_text=''.join(s for s in new_text)
        # print new_text
        # break
        yield new_url,new_title,new_text,new_date,new_source

def main():
    with open('corpus/'+'minshengwang_minsheng','w') as fw:
        for page in range(1,51):
            if page==1:
                main_url='http://www.mszsx.com/news/'
            else:
                main_url='http://www.mszsx.com/news/index_'+str(page)+'.html'
            print main_url
            info = get_news_detail(main_url)
            for new_url,new_title,new_text,new_date,new_source in info:
                news_info = dict()
                news_info['url']=new_url
                news_info['title'] = new_title
                news_info['content'] = new_text
                news_info['date'] = new_date
                news_info['source'] = new_source
                news_info=json.dumps(news_info)
                fw.write(news_info+'\n')
                print new_url, new_title,new_source

if __name__ == '__main__':
    main_url='http://www.mszsx.com/news/'
    main_url_page='http://www.mszsx.com/news/index_2.html'
    main()