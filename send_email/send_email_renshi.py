#!/usr/bin/env python
# -- coding: utf-8 --
import time
import json
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import requests
from prettytable import PrettyTable

import MySQLdb
import torndb

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
yesterday = str(yesterday)

mysql = {
    "host": "117.78.60.108",
    "port": "3306",
    "database": "cityparlor",
    "password": "123456",
    "user": "es",
    "charset": "utf8"
}

# mysql = {
#     "host": "localhost",
#     "port": "3306",
#     "database": "cityparlor",
#     "password": "123456",
#     "user": "root",
#     "charset": "utf8"
# }

date_n = time.strftime("%Y-%m-%d", time.localtime(time.time()))
# date_n = yesterday

db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def get_data():
    news_data='''
        SELECT
        CASE
        WHEN b.name IS NULL THEN '未找到匹配的城市'
        ELSE b.name
        END AS city,
        a.source,
        a.title FROM
        (SELECT title,
        source,
        area FROM cityparlor.t_all_news WHERE DATE(create_date) >= DATE_SUB(CURDATE(),interval 1 day)
        AND p_type_id ='1709301224421460294') a
        LEFT OUTER JOIN
        (SELECT
        code,
        name FROM cityparlor.t_area) b
        ON a.area=b.code
        ORDER BY city;'''

    res_sql = db.query(news_data)
    for r in res_sql:
        yield r


if __name__ == '__main__':
    pt=PrettyTable(field_names=['地区','信息来源','标题'])
    for r in get_data():
        r_list=[r.get('city'),r.get('source'),r.get('title')]
        pt.add_row(r_list)
    pt.align='l'
    res=str(pt)
    print res
    # res='\n'+'人事任免数据抓取明细如下：'+'\n'
    # res +=  '地区     信息来源      标题' + '\n'
    # sums=0
    # for r in get_data():
    #     try:
    #         # print r,r.keys()
    #         res+=r.get('city')+'     '+r.get('source')+'     ' +r.get('title')+'\n'
    #     except:
    #         continue
    # print res


    # from_addr = 'big-data@loongscity.com'
    # password = '\u82CF\u742A'
    # # to_addr = ['luxingdong2008@126.com','sage4571@163.com','1339296847@qq.com','whemy25@163.com']
    # to_addr = ['lyh1269@qq.com']
    # smtp_server = 'smtp.mxhichina.com'
    # msg = MIMEText(res, 'plain', 'utf-8')
    # msg['From'] = _format_addr(u'爬虫服务器 <%s>' % from_addr)
    # # msg['To'] = _format_addr(u'陆总 <%s>' % to_addr[0])+',' +_format_addr(u'suqi <%s>' % to_addr[1])+',' +_format_addr(u'zhujialiang <%s>' % to_addr[2])+',' +_format_addr(u'wanghemin <%s>' % to_addr[3])
    # msg['To'] = _format_addr(u'lyh <%s>' % to_addr[0])
    #
    # msg['Subject'] = Header(yesterday+u' 人事任免数据更新信息', 'utf-8').encode()
    #
    # server = smtplib.SMTP(smtp_server, 25)
    # server.set_debuglevel(1)
    # server.login(from_addr, password)
    # server.sendmail(from_addr, to_addr, msg.as_string())
    # server.quit()
