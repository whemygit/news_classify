#!/usr/bin/env python
# -- coding: utf-8 --
import requests
import torndb
import time
import re
import json
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

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
    # resp = requests.post('http://cms.loongscity.com/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data, headers=headers)
    resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data,headers=headers)  # 服务器
    # resp = requests.post('http://117.78.41.235:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data, headers=headers)         #本地
    return resp


def requests_post_shouye(data):
    # resp = requests.post('https://cms.loongscity.com/cityparlor-web/cityparlor/cityparlor/index/add', data=data,headers=headers)
    resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/index/add', data=data,
                         headers=headers)
    return resp


def change_is_resp(newsid):
    change_sql = '''update rec_news_data set is_resp=1 where newsid=%s''' % newsid
    res = db.execute(change_sql)
    print res


def get_info():
    sql = '''select * from rec_news_data where is_resp=0;'''
    res = db.query(sql)
    for r in res:
        d=dict()
        d['title']=r.get('title')
        d['newsDesc'] = r.get('title')
        d['source'] = r.get('text_f')
        d['content'] = r.get('text')
        d['newsType'] = '1'
        d['counts'] = '0'
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
        d['isTop'] = 0
        d['isEssential'] = 0
        resp = requests_post(d)
        print resp.content,r.get('title')

        #推荐到首页
        rec_data={}
        rec_data['area'] = 0
        rec_data['title'] = d.get('title')
        rec_data['source'] = d.get('source')
        rec_data['isTop'] = 0
        rec_data['isEssential'] = 0
        rec_data['classify'] = d.get('classify')
        rec_data['objId'] = json.loads(resp.content).get('retObj')
        rec_data['objType'] = 'news'
        rec_data['imageUrl'] = d.get('pics')
        resp_shouye = requests_post_shouye(rec_data)
        print resp_shouye.content,d.get('title'),'shouyetuijian',rec_data.get('source')

        news_id = r.get('newsid')
        change_is_resp(news_id)

if __name__ == '__main__':
    get_info()

