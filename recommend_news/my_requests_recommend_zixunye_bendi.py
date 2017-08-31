#!/usr/bin/env python
# -- coding: utf-8 --
import requests
import torndb
import time
import re
import json

import sys

reload(sys)


# mysql = {
#     "host": "192.168.0.202",
#     "port": "3306",
#     "database": "spider",
#     "password": "123456",
#     "user": "suqi",
#     "charset": "utf8"
# }

mysql = {
    "host": "119.57.93.42",
    "port": "3306",
    "database": "spider",
    "password": "zhongguangzhangshi",
    "user": "bigdata",
    "charset": "utf8"
}

headers = {
    'accept': 'textml,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.8',
    'cookie': '_user_id=1708281259017703024; _user_account=suqi;',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))

date_n = time.strftime("%Y-%m-%d", time.localtime(time.time()))


def requests_post(data):
    # resp = requests.post('http://192.168.0.249:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data)
    # resp = requests.post('http://cms.loongscity.com/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data, headers=headers)
    # resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data,headers=headers)  # 服务器
    resp = requests.post('http://117.78.41.235:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data, headers=headers)         #本地
    return resp


def requests_post_shouye(data):
    # resp = requests.post('http://192.168.0.225:8080/cityparlor-web/cityparlor/cityparlor/index/save', data=data)
    # resp = requests.post('https://cms.loongscity.com/cityparlor-web/cityparlor/cityparlor/index/add', data=data,headers=headers)
    resp = requests.post('https://117.78.41.235:8080/cityparlor-web/cityparlor/cityparlor/index/add', data=data,
                         headers=headers)
    return resp


def change_is_resp(newsid):
    change_sql = '''update rec_news_data set is_resp=1 where newsid=%s''' % newsid
    res = db.execute(change_sql)
    print res


def get_info():
    sql = '''select * from rec_news_data where news_date="%s" AND is_resp=0;''' % date_n
    # sql = '''select * from rec_news_data where newsid=395583;'''
    res = db.query(sql)
    for r in res:
        # print r
        d=dict()
        d['title']=r.get('title')
        d['newsDesc'] = r.get('title')
        d['source'] = r.get('text_f')
        # text = str(r.get('text')).replace(r'\n', '').replace('\\', '').replace('http', 'https').replace(
        #     '<style>.*?</style>', '')
        d['content'] = r.get('text')
        d['newsType'] = '1'
        # d['typeId'] = '1708161037396400000'
        d['isRecommend'] = 1
        img_show=r.get('img_show')
        if img_show==None:
            d['classify']=0
        else:
            img_show_len=len(img_show.split(','))
            if img_show_len<=2:
                d['classify']=2
                d['pics']=img_show.split(',')[0]
            else:
                d['classify']=1
                d['pics']=img_show
        resp = requests_post(d)
        print resp.content,r.get('title')
        post_result=resp.content
        news_id = r.get('newsid')
        change_is_resp(news_id)
        # yield post_result,d

def rec_shouye():
    post_result,d=get_info()
    rec_data={}
    rec_data['area'] = 0
    rec_data['title']=d.get('title')
    rec_data['classify']=d.get('classify')
    rec_data['objId']=json.loads(post_result).get('retObj')
    rec_data['objType']='news'
    rec_data['imageUrl']=d.get('pics')
    resp=requests_post_shouye(rec_data)
    print resp.content




if __name__ == '__main__':
    get_info()

