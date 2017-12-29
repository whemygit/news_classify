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
        SELECT * FROM (SELECT
        b.title,
        a.language,
        a.counts
        FROM (
        SELECT
        type_id,
        CASE
        WHEN language_version='EN' THEN '英文'
        WHEN language_version='ZH' THEN '中文'
        ELSE  concat('语种未匹配到:',language_version)
        END AS language,
        COUNT(0) counts
        FROM
        cityparlor.t_top_news
        WHERE DATE(create_date) >= DATE_SUB(curdate(),INTERVAL 1 DAY)
        AND type_id IS NOT NULL AND type_id  !=''
        AND type_id  !='1708161038001960000'
        AND  IS_recommend ='0'
        AND type_id !=0
        AND type_id !='1709071235082790070'
        AND type_id !='1709111209558500023'
        AND type_id !='1711021243522870078'
        AND type_id !='1711101216056640064'
        GROUP BY language_version ,type_id ) a
        LEFT JOIN
        (
        SELECT
        id,
        title
        FROM cityparlor.t_top_type) b
        ON a.type_id =b.id) c
        UNION ALL
        SELECT
        '推荐' ,
        CASE language_version
        WHEN 'EN' THEN '英文'
        WHEN 'ZH' THEN '中文'
        END AS language,
        COUNT(0) counts
        FROM
        cityparlor.t_top_news
        WHERE DATE(create_date) >= DATE_SUB(curdate(),INTERVAL 1 DAY)
        AND type_id IS null AND IS_recommend ='1';'''

    res_sql = db.query(news_data)
    for r in res_sql:
        yield r


def get_city_news_data():
    city_news_data='''
        select c.city,
        case
         when d.language_name is null then concat('语种未匹配到:',c.language)
         else d.language_name
         end AS language
         ,c.counts from (select b.city,
        a.area,
        a.language,
        counts  from (SELECT area ,
        language_version language,
        count(0) counts
        FROM
        cityparlor.t_top_news
        where
        date (create_date) >= date_sub(curdate(),interval 1 day) and
        area !=''
        and type_id ='1708161038001960000'
        group by area ,language_version) a
         left join
        (select
        code ,
        name city
        from cityparlor.t_area) b
        on a.area=b.code) c
         left join
        (SELECT language_name,
        language_code FROM cityparlor.t_language_code) d
        on c.language=d.language_code
         ;'''

    res_sql = db.query(city_news_data)
    for r in res_sql:
        yield r


def get_sdyd_news_data():
    sdyd_news_data='''
            SELECT
            CASE fun
            WHEN 'entertainment_news' THEN '娱道'
            WHEN 'washington' THEN '商道'
            END AS fun,
            CASE language_version
            WHEN 'EN' THEN '英文'
            WHEN 'ZH' THEN '中文'
            END AS language,
            count(0)
            FROM `t_channel_news`
            WHERE date(create_date) >= date_sub(curdate(),interval 1 day)
            GROUP BY fun ,language_version;'''

    res_sql = db.query(sdyd_news_data)
    for r in res_sql:
        yield r


def get_wenzh_news_data():
    wenzh_news_data='''
            SELECT *
            FROM
            (SELECT
            c.name,
            d.title,
            c.language,
            c.counts
            FROM
            (SELECT
            a.p_type_id id ,
            b.name,
            a.language,
            a.counts
            FROM
            (SELECT
             p_type_id,
            area,
            case language_version
            when 'EN' then '英文'
            when 'ZH' then '中文'
            end as language
            ,
            count(0) counts
            FROM `t_all_news`
            WHERE
            date(create_date) >= date_sub(curdate(),interval 1 day)
            AND fun ='town_news'
            AND p_type_id is not null
            GROUP BY p_type_id, area,language_version ) a
            JOIN
            (
            SELECT
            code,
            name
            FROM `t_area` )b
            ON a.area=b.code ) c
            JOIN (SELECT id,title  FROM t_all_type) d
            ON c.id =d.id) e
            WHERE language is not Null;'''

    res_sql = db.query(wenzh_news_data)
    for r in res_sql:
        yield r

def get_shzzx_data():
    shzzx_data='''
            SELECT
            d.city_name,
            c.name,
            c.language,
            c.counts FROM
            (SELECT
            b.name,
            b.area,
            a.language,
            a.counts FROM
            (SELECT
            personage_id,
            CASE
            WHEN language_version='EN' THEN '英文'
            WHEN language_version='ZH' THEN '中文'
            ELSE language_version
            END AS language,
            count(0) counts
            FROM cityparlor.t_all_news
            WHERE DATE(create_date) >= DATE_SUB(CURRENT_TIMESTAMP(),INTERVAL 1 DAY)
            AND del_flag=0
            AND fun ='town_mayor_dynamic'
            GROUP BY personage_id )  a LEFT JOIN
            (SELECT
            id,
            name,
            area
            FROM cityparlor.t_town_mayor
            WHERE del_flag=0)b
            ON a.personage_id=b.id )c
            LEFT OUTER JOIN
            (SELECT
            code,
            name city_name
            FROM t_area
            WHERE del_flag=0) d
            ON c.area=d.code
            ORDER BY city_name DESC;'''

    res_sql = db.query(shzzx_data)
    for r in res_sql:
        yield r



def get_sjxm_data():
    sjxm_data='''
            SELECT * FROM
            (SELECT
            b.name,
            a.counts
            FROM (SELECT
            city_code,
            count(0) counts
            FROM cityparlor.t_opportunity_project
            WHERE date(create_date) >= date_sub(curdate(),interval 1 day)
            AND city_code is not Null
            GROUP BY city_code) a
            LEFT JOIN (SELECT
            code,
            name
            FROM cityparlor.t_area) b
            on a.city_code =b.code) c WHERE name is not Null;'''

    res_sql = db.query(sjxm_data)
    for r in res_sql:
        yield r


def get_sjzx_data():
    sjzx_data='''
            SELECT
            CASE language_version
            WHEN 'EN' THEN '英文'
            WHEN 'ZH' THEN '中文'
            END AS language,
            COUNT(0) counts
            FROM `t_all_news`
            WHERE
            DATE(create_date) >= DATE_SUB(curdate(),INTERVAL 1 DAY)
            AND fun ='opportunity_news';'''

    res_sql = db.query(sjzx_data)
    for r in res_sql:
        yield r

def get_gongyi_data():
    gongyi_data='''
            SELECT
            c.name,
            c.language,
            c.counts
            FROM
            (SELECT
            a.p_type_id id ,
            b.name,
            a.language,
            a.counts
            FROM
            (SELECT
             p_type_id,
            area,
            case language_version
            when 'EN' then '英文'
            when 'ZH' then '中文'
             end as language,
            count(0) counts
            FROM cityparlor.t_all_news
            WHERE
            date(create_date) >= DATE_SUB(CURRENT_TIMESTAMP(),INTERVAL 1 DAY)
            AND fun ='commonweal_news'
            AND del_flag=0
            GROUP BY p_type_id, area,language_version ) a
            JOIN
            (
            SELECT
            code,
            name
            FROM cityparlor.t_area )b
            ON a.area=b.code ) c;'''

    res_sql = db.query(gongyi_data)
    for r in res_sql:
        yield r


if __name__ == '__main__':
    table_list=[]
    header='数据更新汇总情况如下：'+ '\n'
    paragraph_fen='\n'+'\n'+'****************************************************************************************************************'+'\n'
    pt_huizong=PrettyTable(field_names=['模块','数据更新量'])

    sums=0
    pt=PrettyTable(field_names=['新闻类别','语种','数据更新量'])
    for r in get_data():
        try:
            sums+=r.get('counts')
            row=[r.get('title'),r.get('language'),str(r.get('counts'))+'条']
            pt.add_row(row)
        except:
            continue
    pt.align='l'
    res_1=str(pt)
    res_0=paragraph_fen+'分类新闻当日更新总量' + str(sums) + '条,'+ '明细如下：'+'\n'
    table_list.append([res_0,res_1])
    pt_huizong.add_row(['分类新闻更新量',str(sums)+ '条'])

    sums = 0
    pt = PrettyTable(field_names=['地区', '语种', '数据更新量'])
    for r in get_city_news_data():
        try:
            sums += r.get('counts')
            row = [r.get('city'), r.get('language'), str(r.get('counts')) + '条']
            pt.add_row(row)
        except:
            continue
    pt.align = 'l'
    res_1 = str(pt)
    res_0 = paragraph_fen + '本地新闻当日更新总量' + str(sums) + '条,' + '明细如下：' + '\n'
    table_list.append([res_0, res_1])
    pt_huizong.add_row(['本地新闻更新量', str(sums)+ '条'])

    sums = 0
    pt = PrettyTable(field_names=[' 模块', '语种', '数据更新量'])
    for r in get_sdyd_news_data():
        try:
            sums += r.get('count(0)')
            row = [r.get('fun'), r.get('language'), str(r.get('count(0)')) + '条']
            pt.add_row(row)
        except:
            continue
    pt.align = 'l'
    res_1 = str(pt)
    res_0 = paragraph_fen + '商道娱道资讯当日更新总量' + str(sums) + '条,' + '明细如下：' + '\n'
    table_list.append([res_0, res_1])
    pt_huizong.add_row(['商道娱道资讯更新量', str(sums)+ '条'])

    sums = 0
    pt = PrettyTable(field_names=['地区', '问政分类', '语种', '数据更新量'])
    for r in get_wenzh_news_data():
        try:
            sums += r.get('counts')
            row = [r.get('name'), r.get('title'), r.get('language'), str(r.get('counts')) + '条']
            pt.add_row(row)
        except:
            continue
    pt.align = 'l'
    res_1 = str(pt)
    res_0 = paragraph_fen + '问政资讯当日更新总量' + str(sums) + '条,' + '明细如下：' + '\n'
    table_list.append([res_0, res_1])
    pt_huizong.add_row(['问政资讯更新量', str(sums)+ '条'])

    sums = 0
    pt = PrettyTable(field_names=['地区', '书记/市长姓名', '语种', '数据更新量'])
    for r in get_shzzx_data():
        try:
            sums += r.get('counts')
            row = [r.get('city_name'), r.get('name'), r.get('language'), str(r.get('counts')) + '条']
            pt.add_row(row)
        except:
            continue
    pt.align = 'l'
    res_1 = str(pt)
    res_0 = paragraph_fen + '市长在线当日更新总量' + str(sums) + '条,' + '明细如下：' + '\n'
    table_list.append([res_0, res_1])
    pt_huizong.add_row(['市长在线更新量', str(sums)+ '条'])

    sums = 0
    pt = PrettyTable(field_names=['地区', '数据更新量'])
    for r in get_sjxm_data():
        try:
            sums += r.get('counts')
            row = [r.get('name'), str(r.get('counts')) + '条']
            pt.add_row(row)
        except:
            continue
    pt.align = 'l'
    res_1 = str(pt)
    res_0 = paragraph_fen + '商机项目当日更新总量' + str(sums) + '条,' + '明细如下：' + '\n'
    table_list.append([res_0, res_1])
    pt_huizong.add_row(['商机项目更新量', str(sums)+ '条'])

    sums = 0
    pt = PrettyTable(field_names=['语种', '数据更新量'])
    for r in get_sjzx_data():
        try:
            sums += r.get('counts')
            row = [r.get('language'), str(r.get('counts')) + '条']
            pt.add_row(row)
        except:
            continue
    pt.align = 'l'
    res_1 = str(pt)
    res_0 = paragraph_fen + '商机资讯当日更新总量' + str(sums) + '条,' + '明细如下：' + '\n'
    table_list.append([res_0, res_1])
    pt_huizong.add_row(['商机资讯更新量', str(sums)+ '条'])

    sums = 0
    pt = PrettyTable(field_names=['地区','语种', '数据更新量'])
    for r in get_gongyi_data():
        try:
            sums += r.get('counts')
            row = [r.get('name'), r.get('language'), str(r.get('counts')) + '条']
            pt.add_row(row)
        except:
            continue
    pt.align = 'l'
    res_1 = str(pt)
    res_0 = paragraph_fen + '公益资讯当日更新总量' + str(sums) + '条,' + '明细如下：' + '\n'
    table_list.append([res_0, res_1])
    pt_huizong.add_row(['公益资讯更新量', str(sums)+ '条'])



    pt_huizong.align='l'
    res=header+str(pt_huizong)
    for i in table_list:
        res+=i[0]+i[1]
    print res


    # from_addr = 'big-data@loongscity.com'
    # password = '\u82CF\u742A'
    # to_addr = ['luxingdong2008@126.com',
    #            'zengyi@loongs.cc',
    #            'sage4571@163.com',
    #            '1339296847@qq.com',
    #            'whemy25@163.com',
    #            '1789981094@qq.com',
    #            '2286635023@qq.com',
    #            '2129219453@qq.com',
    #            '1354867306@qq.com']
    #
    # smtp_server = 'smtp.mxhichina.com'
    # msg = MIMEText(res, 'plain', 'utf-8')
    # msg['From'] = _format_addr(u'爬虫服务器 <%s>' % from_addr)
    # msg['To'] = _format_addr(u'陆总 <%s>' % to_addr[0])\
    #             +',' +_format_addr(u'zengyi <%s>' % to_addr[1])\
    #             +',' +_format_addr(u'suqi <%s>' % to_addr[2])\
    #             +',' +_format_addr(u'zhujialiang <%s>' % to_addr[3])\
    #             +',' +_format_addr(u'wanghemin <%s>' % to_addr[4])\
    #             +',' +_format_addr(u'duwanqiu <%s>' % to_addr[5])\
    #             +',' +_format_addr(u'wangqiuyang <%s>' % to_addr[6])\
    #             +',' +_format_addr(u'sunyan <%s>' % to_addr[7])\
    #             +',' +_format_addr(u'wangxuelan <%s>' % to_addr[8])
    #
    #
    # msg['Subject'] = Header(yesterday+u' 数据更新信息', 'utf-8').encode()
    #
    # server = smtplib.SMTP(smtp_server, 25)
    # server.set_debuglevel(1)
    # server.login(from_addr, password)
    # server.sendmail(from_addr, to_addr, msg.as_string())
    # server.quit()
