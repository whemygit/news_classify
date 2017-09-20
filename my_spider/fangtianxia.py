#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import HTMLParser
import json
import requests
from lxml import etree
from pandas import DataFrame
reload(sys)
sys.setdefaultencoding("utf-8")

url='http://newhouse.sy.fang.com/house/baojia.htm'


def price_spider(url):
    resp=requests.get(url)
    detail=etree.HTML(resp.content)
    data_all_area={}
    p_name=detail.xpath('//div[@class="pricearea"]/ul/li/span[1]/a/text()')

    p_price=detail.xpath('//div[@class="pricearea"]/ul/li/span[2]/text()')
    print len(p_name),len(p_price)
    p_info=zip(p_name,p_price)
    # for i in p_info:
    #     print i[0],i[1]


    data_all_area['prpname']=p_name
    data_all_area['prpprice']=p_price

    data_all_area_frame=DataFrame(data_all_area)

    data_all_area_frame['identify']= map(lambda x: '0' if x=='待定' else '1', data_all_area_frame['prpprice'])
    data_all_area_frame['int_price'] = map(lambda x: int(0) if x == '待定' else int(x.split('元')[0]),
                                          data_all_area_frame['prpprice'])
    data_mean=data_all_area_frame.groupby(['identify'])['int_price'].mean()
    print data_mean
    print data_all_area_frame

areas=['hunnanxinqu1','tiexi','shenbeixinqu','yuhong','huanggu','heping','dadong','shenhe','sujiatun',
       'xinmin','liaozhong','qita']

# areas=['hunnanxinqu1','tiexi','shenbeixinqu','yuhong','huanggu','heping']

urls=['http://newhouse.sy.fang.com/house/s/'+area +'/' for area in areas]
url_area='http://newhouse.sy.fang.com/house/s/hunnanxinqu1/'

def area_price_spider():
    df = DataFrame()
    for area in areas:
        area_url='http://newhouse.sy.fang.com/house/s/'+area +'/'
        resp=requests.get(area_url)
        detail=etree.HTML(resp.content)
        data_all_area={}
        p_name=[i.strip() for i in detail.xpath('//div[@class="nlcd_name"]/a/text()')]

        p_price=detail.xpath('//div[@class="nhouse_price"]/span/text()')
        # print len(p_name),len(p_price)
        # p_info=zip(p_name,p_price)
        # for i in p_info:
        #     print i[0],i[1]


        data_all_area['prpname']=p_name[0:len(p_price)]
        data_all_area['prpprice']=p_price
        data_all_area['area']=area
        data_all_area_frame=DataFrame(data_all_area)
        # print data_all_area_frame

        data_all_area_frame['identify']= map(lambda x: '0' if x=='价格待定' else '1', data_all_area_frame['prpprice'])
        data_all_area_frame['int_price'] = map(lambda x: int(0) if x == '价格待定' else int(x),
                                              data_all_area_frame['prpprice'])
        # data_mean=data_all_area_frame.groupby(['identify'])['int_price'].mean()
        # print data_mean
        # print data_all_area_frame
        df=df.append(data_all_area_frame)
    # df['int_price']=map(lambda x: int(x),df['prpprice'])
    # print df
    data_mean=df.groupby(['area','identify'])['int_price'].mean()
    print data_mean
    data_min=df.groupby(['area','identify'])['int_price'].min()
    print data_min
    data_max = df.groupby(['area', 'identify'])['int_price'].max()
    print data_max


if __name__ == '__main__':
    area_price_spider()