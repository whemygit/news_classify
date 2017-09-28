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
areas = ['北京市', '天津市', '上海市', '广州市', '深圳市',
         '鞍山市', '阜新市', '锦州市', '铁岭市', '辽阳市',
         '葫芦岛市', '营口市', '盘锦市', '沈阳市', '本溪市',
         '朝阳市', '抚顺市', '大连市', '丹东市','哈尔滨市',
         '龙岩市', '呼和浩特市', '阿坝藏族羌族自治州',
         '长春市','南京市','武汉市','重庆市',
         '成都市','西安市','石家庄市','太原市',
         '唐山市','包头市','吉林市','齐齐哈尔市',
         '徐州市','杭州市','福州市','南昌市',
         '济南市','青岛市','淄博市','郑州市',
         '长沙市','贵阳市','昆明市','兰州市',
         '乌鲁木齐市','合肥市','南宁市','海口市',
         '西宁市','银川','宁波市','厦门市','雄安新区']
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
    sql = '''select * from _news_data where area="%s" AND news_date="%s" AND is_resp=0''' % (
    city, date_n)
    # sql='''select * from _news_data where area area="北京市"AND img_show is not NULL ORDER BY news_date DESC LIMIT 1;'''
    rec_newsid_sql = '''select newsid from _news_data where area="%s" AND news_date="%s" AND is_resp=0 LIMIT 5;''' % (
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
        print r.get('area'), resp.content

        # 推荐到首页
        if r.get('newsid') in newsid_rec_list:
            rec_data = {}
            rec_data['area'] = d.get('area')
            rec_data['title'] = d.get('title')
            rec_data['source'] = d.get('source')
            rec_data['isTop'] = 0
            rec_data['isEssential'] = 0
            rec_data['classify'] = d.get('classify')
            rec_data['objId'] = json.loads(resp.content).get('retObj')
            rec_data['objType'] = 'news'
            rec_data['imageUrl'] = d.get('pics')
            rec_data['languageVersion'] = d.get('languageVersion')
            resp_shouye = requests_post_shouye(rec_data)
            print resp_shouye.content, d.get('title'), 'shouyetuijian',rec_data.get('languageVersion')
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
