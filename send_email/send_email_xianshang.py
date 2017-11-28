#!/usr/bin/env python
# -- coding: utf-8 --
import time
import json
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import requests

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
    "host": "49.4.6.196",
    "port": "3306",
    "database": "cityparlor",
    "password": "123456",
    "user": "es",
    "charset": "utf8"
}

date_n = time.strftime("%Y-%m-%d", time.localtime(time.time()))
# date_n = yesterday

db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))
def get_data():
    news_data='''
            select * from (select b.title,
            a.counts
            from (
            SELECT
            type_id,
            count(0) counts
            FROM
             cityparlor.t_top_news
             where date(create_date) = date_sub(curdate(),interval 1 day)
             and type_id is not null and type_id  !=''
             and type_id  !='1708161038001960000'
             and  is_recommend ='0'
             and type_id !=0
             and type_id !='1709071235082790070'
             and type_id !='1709111209558500023'
             and type_id !='1711021243522870078'
             and type_id !='1711101216056640064'
             group by type_id) a
             left join
             (
             SELECT
             id,
             title
             FROM cityparlor.t_top_type) b
             on a.type_id =b.id) c
             union all
             SELECT  "首页推荐",
             count(0) counts
             FROM
             cityparlor.t_index_setting
             where
             date(create_date) = date_sub(curdate(),interval 1 day)
             union all
             SELECT
             '推荐' ,
             count(0) counts
             FROM
             cityparlor.t_top_news
             where date(create_date) = date_sub(curdate(),interval 1 day)
             and
             type_id is null and is_recommend ='1';'''

    res_sql = db.query(news_data)
    for r in res_sql:
        yield r


def get_city_news_data():
    city_news_data='''
        select b.city,a.language,counts  from
        (SELECT
        area ,

        case language_version
        when 'EN' then '英文'
        when 'ZH' then '中文'
         end as language
        ,
        count(0) counts
        FROM
        cityparlor.t_top_news
        where
        date (create_date) = date_sub(curdate(),interval 1 day)
        and area !=''
        and type_id ='1708161038001960000'
        and language_version!='None'
        and language_version!='CH'
        group by area ,language_version) a
         join
        (select
        code ,
        name city
        from cityparlor.t_area) b
        on a.area=b.code;'''

    res_sql = db.query(city_news_data)
    for r in res_sql:
        yield r




if __name__ == '__main__':
    res=''
    for r in get_data():
        # print r.get('title'),r.get('counts')
        res+=r.get('title')+':'+str(r.get('counts'))+'条'+'\n'
    # print res

    res+='\n'+'各城市新闻抓取情况如下：'+'\n'
    for r in get_city_news_data():
        # print r.get('city'),r.get('language'),str(r.get('counts'))
        res+= r.get('city') +r.get('language') + str(r.get('counts'))+'条'+'\n'
    print res


    from_addr = 'big-data@loongscity.com'
    password = '\u82CF\u742A'
    to_addr = ['jiabei5212006@126.com']
    #to_addr = ['wlw9649@163.com']
    smtp_server = 'smtp.mxhichina.com'
    # smtp_server = 'smtp.qq.com'
    msg = MIMEText(res, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'爬虫服务器 <%s>' % from_addr)
    msg['To'] = _format_addr(u'wanghemin <%s>' % to_addr[0])
    #msg['To'] = _format_addr(u'吴乐伟 <%s>' % to_addr[0])

    msg['Subject'] = Header(u'昨日数据统计结果信息……', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
