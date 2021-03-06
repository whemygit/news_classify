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
areas = ['北京', '天津', '上海', '广州', '深圳',
         '鞍山', '阜新', '锦州', '铁岭', '辽阳',
         '葫芦岛', '营口', '盘锦', '沈阳', '本溪',
         '朝阳', '抚顺', '大连', '丹东','哈尔滨',
         '龙岩', '呼和浩特', '阿坝藏族羌族自治州',
         '长春','南京','武汉','重庆',
         '成都','西安','石家庄','太原',
         '唐山','包头','吉林','齐齐哈尔',
         '徐州','杭州','福州','南昌',
         '济南','青岛','淄博','郑州',
         '长沙','贵阳','昆明','兰州',
         '乌鲁木齐','合肥','南宁','海口',
         '西宁','银川','宁波','厦门',
         '雄安新区', '肥城', '胶州',
         '即墨', '龙口', '平阴', '荣成',
         '新泰', '诸城', '邹城',
         '江西省', '张家口', '三亚', '抚州', '赣州',
         '贵溪', '吉安', '景德镇',
         '九江', '南昌县', '萍乡', '上饶',
         '新余', '宜春', '鹰潭', '樟树']
# areas = ['肥城', '胶州', '即墨', '龙口', '平阴', '荣成', '新泰', '诸城', '邹城']
# mysql = {
#     "host": "192.168.0.202",
#     "port": "3306",
#     "database": "spider",
#     "password": "123456",
#     "user": "suqi",
#     "charset": "utf8"
# }
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.8',
    'cookie': '_user_id=1708281259017703024; _user_account=suqi;',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}
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
#date_n = '2017-10-20'

def requests_post(data):
    resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data,headers=headers)  # 服务器
    # resp = requests.post('http://117.78.41.235:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data, headers=headers)         #本地
    return resp

def requests_post_shouye(data):
    resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/index/add', data=data,
                         headers=headers)
    return resp


def change_is_resp(newsid):
    change_sql = '''update _news_data set is_resp=1 where newsid=%s''' % newsid
    res = db.execute(change_sql)
    print res


def get_info(city):
    sql = '''select * from _news_data where area like "{city}%%" AND news_date="{date_n}" AND is_resp=0'''.format(
    city=city, date_n=date_n)
    # sql='''select * from _news_data where area area="北京"AND img_show is not NULL ORDER BY news_date DESC LIMIT 1;'''
    rec_newsid_sql = '''select newsid from _news_data where area like "{city}%%" AND news_date="{date_n}" AND is_resp=0 LIMIT 5;'''.format(
    city=city, date_n=date_n)
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
        d['area'] = get_area_code(city)
        d['content'] = text
        d['counts'] = '0'
        d['newsDesc'] = r.get('title')
        d['newsType'] = '1'
        img_show = r.get('img_show')
        if img_show == None:
            d['classify'] = 0
        else:
            img_show_len = len(img_show.split(','))
            if img_show_len <= 2:
                d['classify'] = 2
                d['pics'] = img_show.split(',')[0]
            else:
                d['classify'] = 1
                d['pics'] = img_show
        d['source'] = r.get('text_f')
        d['title'] = r.get('title')
        d['isTop'] = 0
        d['isEssential'] = 0
        d['typeId'] = '1708161038001960000'
        d['isRecommend'] = 0
        d['languageVersion'] = 'ZH'
        resp = requests_post(d)
        print r.get('area'), d.get('area'), resp.content

        # 推荐到首页
        if r.get('newsid') in newsid_rec_list:
            rec_data = {}
            rec_data['area'] = d.get('area')
            rec_data['title'] = d.get('title')
            rec_data['source'] = d.get('source')
            rec_data['isTop'] = 0
            rec_data['isEssential'] = 0
            rec_data['classify'] = d.get('classify')
            try:
                rec_data['objId'] = json.loads(resp.content).get('retObj')
            except ValueError:
                news_id = r.get('newsid')
                change_is_resp(news_id)
                continue
            rec_data['objType'] = 'news'
            rec_data['imageUrl'] = d.get('pics')
            rec_data['languageVersion'] = d.get('languageVersion')
            resp_shouye = requests_post_shouye(rec_data)
            print resp_shouye.content, d.get('title'), 'shouyetuijian',rec_data.get('languageVersion')
        news_id = r.get('newsid')
        change_is_resp(news_id)


def get_area_code(city):
    sql = """select name, code from t_area where IsEnabled=1;"""
    res = db.query(sql)
    for r in res:
        area = r.get('name')
        if city in area:
            return r.get('code')


if __name__ == '__main__':
    for _city in areas:
        get_info(_city)
