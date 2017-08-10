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
    s=resp.content
    s = s.replace(r'jQuery17105182322770872603_1502343424783({ "status": 0,"data": ', '')
    s=s.replace(r', "totalnum":4081})','')
    s_dict=json.loads(s)
    for i in s_dict.values()[0]:
        new_url=i.get('LinkUrl')
        new_title=i.get('Title')
        new_time=i.get('PubTime')
        new_img_url=i.get('allPics')[0]
        # print new_title,new_img
        yield new_url,new_title,new_time,new_img_url

def get_news_detail(new_url):
    resp=requests.get(new_url)
    # print resp.content
    detail=etree.HTML(resp.content)
    new_source=detail.xpath('//*[@id="source"]/text()')[0]
    # print new_source
    new_text=etree.tostring(detail.xpath('//*[@id="p-detail"]')[0], xml_declaration=True,
                   encoding='utf-8').decode()
    new_text=re.sub(r'<div class="zan-wap"[\s.\S]*?iv>', '', new_text)
    new_text = re.sub(r'<div class="p-tags"[\s.\S]*?iv>', '', new_text)
    new_text= re.sub(r'<iframe src=" "[\s.\S]*?/>&#13;', '', new_text)
    new_text = re.sub(r'<span class="tj"[\s.\S]*?>&#13;', '', new_text)
    # print new_text
    return new_text,new_source

def main():
    main_url = 'http://qc.wa.news.cn/nodeart/list?nid=11147664&pgnum=1&cnt=16&tp=1&orderby=1?callback=jQuery17105182322770872603_1502343424783&_=1502343425088'
    for new_url,new_title,new_time,new_img_url in get_news_urllist(main_url):
        new_text, new_source = get_news_detail(new_url)
        news_info = dict()
        news_info['url'] = new_url
        news_info['title'] = new_title
        news_info['news_date'] = new_time
        news_info['source'] = new_source
        news_info['content'] = new_text
        news_info['img_show'] = 'https://cityparlor.oss-cn-beijing.aliyuncs.com/sd_yd_img/img/'+new_img_url.split('/')[-1]
        news_info = json.dumps(news_info)
        # fw.write(news_info + '\n')
        print new_url, new_title,new_img_url
        break

if __name__ == '__main__':
    # main_url='http://qc.wa.news.cn/nodeart/list?nid=11147664&pgnum=1&cnt=16&tp=1&orderby=1?callback=jQuery17105182322770872603_1502343424783&_=1502343425088'
    # # get_news_urllist(main_url)
    # new_url='http://news.xinhuanet.com/fortune/2017-08/10/c_1121460024.htm'
    # get_news_detail(new_url)
    main()
