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

main_url='http://minsheng.haiwainet.cn/455828/'
main_url_page='http://minsheng.haiwainet.cn/455828/2.html'
def get_news_urllist(main_url):
    resp=requests.get(main_url)
    # print resp.content
    doc = etree.HTML(resp.content)
    news_url = doc.xpath('//div[@class="w650 show_list fl"]/ul/li/a/@href')
    return news_url


def get_news_detail(main_url):
    for new_url in get_news_urllist(main_url):
        resp=requests.get(new_url)
        detail=etree.HTML(resp.content)
        # print resp.content
        try:
            try:
                new_title=detail.xpath('//h1[@class="show_wholetitle"]/text()')[0]
                # print new_title
                # break
            except:
                new_title=detail.xpath('//h1[@class="H01 tp05"]/text()')[0]

            try:
                new_date=detail.xpath('//div[@class="contentExtra"]/span[1]/text()')
                new_date=new_date[0].split(" ")[0]
                # print new_date
                # break
            except:
                new_date = detail.xpath('//*[@id="pubtime_baidu"]/text()')
                new_date = new_date[0].split(" ")[0]
                # print new_date
                # break
            try:
                try:
                    new_source=detail.xpath('//div[@class="contentExtra"]/span[2]/a/text()')[0]
                    # print new_source
                    # break
                except:
                    new_source = detail.xpath('//*[@id="source_baidu"]/a/text()')[0]
                    # print new_source
                    # break
            except IndexError as err:
                new_source = detail.xpath('//div[@class="contentExtra"]/span[2]/text()')
                new_source=new_date[0].split("：")[0]
                print "changed"
                # break
            try:
                new_text=detail.xpath('//div[@class="contentMain"]/p/text()')
                new_text=''.join(s for s in new_text)
                # print new_text
                # break
            except:
                new_text = detail.xpath('//*[@id="con"]/p/text()')
                new_text = ''.join(s for s in new_text)
                # print new_text
                # break
        except:
            continue
        yield new_url,new_title,new_text,new_date,new_source


def main():
    with open('corpus/'+'haiwaiwang_fangchan','w') as fw:
        for page in range(1,22):
            if page==1:
                main_url='http://minsheng.haiwainet.cn/455828/'
            else:
                main_url='http://minsheng.haiwainet.cn/455828/'+str(page)+'.html'
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
    # get_news_detail('http://minsheng.haiwainet.cn/n/2016/0715/c455828-30098172.html')
    main()