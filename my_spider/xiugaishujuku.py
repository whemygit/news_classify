#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import requests
from lxml import etree
import jieba
import time
import re
import torndb
import traceback

reload(sys)
sys.setdefaultencoding("utf-8")

today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
yesterday=time.strftime('%Y-%m-%d',time.localtime(time.time()-86400))

# mysql = {
#     "host": "119.57.93.42",
#     "port": "3306",
#     "database": "spider",
#     "password": "zhongguangzhangshi",
#     "user": "bigdata",
#     "charset":"utf8"
# }

mysql = {
    "host": "192.168.0.202",
    "port": "3306",
    "database": "spider",
    "password": "123456",
    "user": "suqi",
    "charset": "utf8"
}

db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                           user=mysql.get('user'),
                           password=mysql.get('password'),charset=mysql.get('charset'))

select_sql='SELECT * FROM rec_news_data WHERE text LIKE "%%相关报道见%%";'
print select_sql

res=db.query(select_sql)
print res

# if __name__ == '__main__':
#     pass