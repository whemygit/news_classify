#!/usr/bin/env python
# -- coding: utf-8 --
import requests
import torndb
import re

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

mysql = {
    "host": "192.168.0.202",
    "port": "3306",
    "database": "spider",
    "password": "123456",
    "user": "suqi",
    "charset": "utf8"
}
areas = ['贵阳', '南昌', '大连', '合肥', '郑州', '沈阳', '唐山', '三亚', '长春', '温州', '佛山', '济南', '宁波', '武汉', '南宁', '青岛', '东莞', '兰州',
         '无锡', '昆明', '成都', '西安', '石家庄', '苏州', '淄博', '太原', '长沙', '福州', '烟台']
db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))


def requests_post_1(data):
    resp = requests.post('http://cms.loongscity.com/cityparlor-web/cityparlor/cityparlor/town/news/add', data=data)
    return resp


def get_title_area(title):
    for area in areas:
        if area in title:
            return area


def filter_tags(htmlstr):
    """
    清洗和过滤标签
    :param htmlstr: 页面筛选后的html代码块
    :return: 返回处理后的带标签内容
    """
    # 替换p标签
    s = re.sub(r'<p.*?>', '<p>', htmlstr)
    # 去掉h和style标签
    s = re.sub(r'<style>[\s.\S]*?</style>', '', s)
    # 替换div
    s = re.sub(r'<div.*?>', '<div>', s)
    # 处理script标签
    s = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', '', s)
    s = re.sub(r'<\s*script[^>]*>', '', s)
    # 去掉a标签
    s = re.sub(r'<a.*?>', '', s)
    s = re.sub(r'</a>', '', s)
    # 去掉input标签
    s = re.sub(r'<input.*?>', '', s)
    return s


def get_info():
    sql = '''select * from town_data_1'''
    res = db.query(sql)
    for r in res:
        info_d = dict()
        area = r.get('area')
        if not area:
            continue
        if area == 'area':
            area = get_title_area(r.get('title'))
        try:
            code = get_area_code(area)
        except TypeError:
            print area, code
            continue
        info_d['title'] = r.get('title')
        info_d['categoryId'] = r.get('category_pid')
        info_d['categoryPid'] = r.get('category_id')
        info_d['area'] = code
        info_d['releaseUnit'] = r.get('text_f')
        info_d['releaseDate'] = r.get('news_date')
        info_d["isEssential"] = "0"
        info_d['isCtop'] = "0"
        info_d['classify'] = "0"
        info_d['newsDetails'] = filter_tags(r.get('text'))
        resp = requests_post_1(info_d)
        print resp.content, area



def get_area_code(city):
    sql = """select name, code from t_area"""
    res = db.query(sql)
    for r in res:
        area = r.get('name')
        if city in area:
            return r.get('code')


if __name__ == '__main__':
    get_info()
