#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import requests
import pymysql


def get_report_id(keywd):
    # mysql_params = {
    #     "host": "117.78.60.108",
    #     "port": 3306,
    #     "database": "cityparlor",
    #     "password": "123456",
    #     "user": "es",
    #     "charset": "utf8"}

    mysql_params = {
        "host": "192.168.1.26",
        "port": 3306,
        "database": "cityparlor",
        "password": "123456",
        "user": "es",
        "charset": "utf8"}


    mysql = mysql_params
    conn = pymysql.connect(host=mysql.get('host'), port=mysql.get('port'), user=mysql.get('user'),
                           passwd=mysql.get('password'), db=mysql.get('database'), charset=mysql.get('charset'))
    cur = conn.cursor()
    cur.execute('''SELECT id,title,area FROM t_top_report WHERE title LIKE '%%{s}%%' AND area='110100';'''.format(s=keywd))
    res_sql = cur.fetchall()
    cur.close()
    conn.close()
    for i in res_sql:
        report_id=i[0]
        report_title=i[1]
        report_area=i[2]
        print(report_id)
        print(report_title)
    return report_id,report_area

def requests_post(data):
    resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/top/news/edit', data=data)  # 服务器
    # resp = requests.post('http://117.78.41.235:8080/cityparlor-web/cityparlor/cityparlor/top/news/edit', data=data)         #本地
    return resp



def report_news_post(news_id,report_id):
    d = dict()
    d['id'] = news_id
    d['reportId'] = report_id
    resp = requests_post(d)
    print(resp.content,d['id'], d['reportId'])


