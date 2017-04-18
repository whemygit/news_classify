#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb
reload(sys)
sys.setdefaultencoding("utf-8")

#连接数据库
def mysql_connect():
    mysql_par={'ip':"192.168.0.202",
               'port':'3306',
               'database':'spider',
               'user':'root',
               'password':'neiwang-zhongguangzhangshi'}

    db=torndb.Connection(host=mysql_par['ip'],
                         database=mysql_par['database'],
                         user=mysql_par['user'],
                         password=mysql_par['password'])
    return db

# 297个城市列表
def define_city_list():
    with open('city_list', 'r') as fr:
        city_list = fr.readlines()
        print 'len(city_list):' + str(len(city_list))
    return city_list

def rec_newsid_select(city):
    db=mysql_connect()
    pos_news_select='SELECT * FROM news_data WHERE area LIKE \'%%{s}%%\' AND em_teg=0 ORDER BY news_date DESC LIMIT 7;'.format(s=city)
    # pos_news_select=pos_news_select.replace('%','%%')
    pos_news_res=db.query(pos_news_select)
    pos_newsid_list=[]
    for news_select in pos_news_res:
        newsid_select=news_select.get('newsid')
        pos_newsid_list.append(newsid_select)
    print pos_newsid_list
    return pos_newsid_list
    db.close()

def rec_news_select(city):
    db=mysql_connect()
    pos_news_list=[]
    for newsid in rec_newsid_select(city):
        print newsid
        pos_news_select='SELECT * FROM news_data WHERE newsid={n};'.format(n=newsid)
        pos_news_res=db.query(pos_news_select)                                                     #按照newsID查找到的包含该条新闻字典的列表
        pos_news_list.append(pos_news_res)
    return pos_news_list
    db.close()

pos_newsid_list=rec_news_select()
db=mysql_connect()
sql='SELECT * FROM news_data WHERE newsid not in ', pos_newsid_list

if __name__ == '__main__':
    # define_city_list()
    # rec_newsid_select('北京')
    rec_news_select('北京')
    # rec_news_select(3394)