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

