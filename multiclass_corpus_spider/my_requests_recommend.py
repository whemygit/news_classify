#!/usr/bin/env python
# -- coding: utf-8 --
import requests
import torndb
import time
import re

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
areas = ['北京市', '天津市', '上海市', '广州市', '深圳市',
         '鞍山市', '阜新市', '锦州市', '铁岭市', '辽阳市',
         '葫芦岛市', '营口市', '盘锦市', '沈阳市', '本溪市',
         '朝阳市', '抚顺市', '大连市', '丹东市','哈尔滨市','呼和浩特市', '龙岩市', '阿坝藏族羌族自治州']
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

db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))

date_n = time.strftime("%Y-%m-%d", time.localtime(time.time()))


def requests_post(data):
    # resp = requests.post('http://192.168.0.225:8080/cityparlor-web/cityparlor/cityparlor/index/save', data=data)
    resp = requests.post('https://cms.loongscity.com/cityparlor-web/cityparlor/cityparlor/index/save', data=data)
    return resp


def requests_post_1(data):
    resp = requests.post('http://cms.loongscity.com/cityparlor-web/cityparlor/cityparlor/top/news/add', data=data)
    return resp


def change_is_resp(newsid):
    change_sql = '''update _news_data set is_resp=1 where newsid=%s''' % newsid
    res = db.execute(change_sql)
    print res


def get_info(city):
    sql = '''select * from _news_data where area="%s" AND news_date="%s" AND img_show is not NULL AND is_resp=0 ORDER BY news_date DESC''' % (
    city, date_n)
    # sql='''select * from _news_data where area area="北京市"AND img_show is not NULL ORDER BY news_date DESC LIMIT 1;'''
    rec_newsid_sql = '''select newsid from _news_data where area="%s" AND news_date="%s" AND img_show is not NULL AND is_resp=0 ORDER BY news_date DESC LIMIT 2;''' % (
    city, date_n)
    res = db.query(sql)
    res_rec=db.query(rec_newsid_sql)
    newsid_rec_list=[]
    for i in res_rec:
        newsid_rec_list.append(i.get('newsid'))
    for r in res:
        d = dict()
        text = str(r.get('text')).replace(r'\n', '').replace('\\', '').replace('http', 'https').replace(
            '<style>.*?</style>', '')
        imgs = re.findall(r'<img.+?src="(.*?)"', text)
        if imgs:
            for img in imgs:
                _img = '<img src="' + img + '">'
                reg = '<img src="%s".*?/>' % img
                text = re.sub(reg, _img, text)
        d['area'] = get_area_code(r.get('area'))
        d['content'] = text
        d['counts'] = '0'
        # d['createDate'] = str(r.get('news_date'))
        d['newsDesc'] = ''
        d['newsType'] = '1'
        d['pics'] = ','.join([img for img in imgs])
        d['source'] = r.get('text_f')
        d['title'] = r.get('title')
        d['isTop'] = 0
        d['isEssential'] = 0
        d['typeId'] = '1708161038001960000'
        d['isRecommend'] = 0
        if r.get('newsid') in newsid_rec_list:
            d['isRecommend'] = 1
        # for recid in res_rec:
        #     if r.get('newsid')==recid.get('newsid'):
        #         d['isRecommend'] = 1
            # else:
            #     d['isRecommend'] = 0
        resp = requests_post_1(d)
        print r.get('area'), resp.content
        news_id = r.get('newsid')
        change_is_resp(news_id)


def get_area_code(city):
    sql = """select name, code from t_area"""
    res = db.query(sql)
    for r in res:
        area = r.get('name')
        if city in area:
            return r.get('code')


if __name__ == '__main__':
    for _city in areas:
        get_info(_city)
        # change_is_resp()
        # requests_post(data)
        # get_area_code(_city)
