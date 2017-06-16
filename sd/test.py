#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb

reload(sys)
sys.setdefaultencoding("utf-8")

# c='https://img.huxiucdn.com/article/content/201512/08/1208338475.jpg'
#
# a='http://img-proxy.huxiu.com/http://mmbiz.qpic.cn/mmbiz_jpg/l4sfibEYR5pWMia1ib0DILOicp1vj3cyBalia3QZxITGvD0Gia8yFeq0g474EbXrqPicdAChtkiaxNtwI50rO9jibdWmibwQ/0'
# print  a.startswith('http://img-proxy')
# print 'http://img-proxy' in c

def mysql_connect():
    mysql_par={'ip':"192.168.0.202",
               'port':'3306',
               'database':'spider',
               'user':'root',
               'password':'neiwang-zhongguangzhangshi'}

    # mysql_par={'ip':"119.57.93.42",
    #            'port':'3306',
    #            'database':'spider',
    #            'user':'bigdata',
    #            'password':'zhongguangzhangshi'}


    db=torndb.Connection(host=mysql_par['ip'],
                         database=mysql_par['database'],
                         user=mysql_par['user'],
                         password=mysql_par['password'])
    return db



if __name__ == '__main__':
    db = mysql_connect()
    select_sql = 'SELECT title FROM sd_hxw;'