#!/usr/bin/env python
# -- coding: utf-8 --
import sys
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
    news_url=doc.xpath('//div[@class="dd_bt"]/a/@href')
    news_url=['http://www.chinanews.com'+new_url for new_url in news_url]
    return news_url

def get_news_detail(main_url):
    for new_url in get_news_urllist(main_url):
        resp=requests.get(new_url)
        detail=etree.HTML(resp.content)
        new_title=detail.xpath('//*[@id="cont_1_1_2"]/h1/text()')[0].strip()
        # print new_title
        # break
        new_date=detail.xpath('//*[@id="cont_1_1_2"]/div[4]/div[2]/text()')[0]
        new_date=new_date.split('　')[0].split(' ')[1]
        new_date=re.findall('\d+',new_date)
        new_date='-'.join(s for s in new_date)
        # print new_date
        # break
        new_source =detail.xpath('//*[@id="cont_1_1_2"]/div[4]/div[2]/text()')[0]
        new_source = new_source.split('　')[1].split('：')[1]
        # print new_source
        # break
        new_text=detail.xpath('//div[@class="left_zw"]/p/text()')
        new_text=''.join(s for s in new_text)
        # print new_text
        # break
        yield new_url,new_title,new_text,new_date,new_source

def main():
    with open('corpus'+'chinanes_fangchan','w') as fw:
            main_url='http://www.chinanews.com/house/gd.shtml'
            info = get_news_detail(main_url)
            for new_url,new_title,new_text,new_date,new_source in info:
                content=get_news_detail(new_url)
                news_info = dict()
                news_info['url'] = new_url
                news_info['title'] = new_title
                news_info['content'] = new_text
                news_info['date'] = new_date
                news_info['source'] = new_source
                news_info = json.dumps(news_info)
                fw.write(news_info + '\n')
                print new_url, new_title, new_source


if __name__ == '__main__':
    main()
