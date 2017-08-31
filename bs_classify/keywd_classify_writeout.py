#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import requests
import torndb
import time
import re
import json

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

# mysql = {
#     "host": "119.57.93.42",
#     "port": "3306",
#     "database": "spider",
#     "password": "zhongguangzhangshi",
#     "user": "bigdata",
#     "charset": "utf8"
# }


db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))


category_dict={
    "其他":"0",
    "市政建设":"1",
    "土地开发":"2",
    "医疗康养":"3",
    "能源矿产":"4",
    "知识产权":"5",
    "文化创意":"6",
    "金融投资":"7",
    "交通运输":"8",
    "农林牧渔":"9",
    "网络科技":"10",
    "先进制造":"11",
    "建筑建材":"12",
    "旅游开发":"13"
}

def category_writeout():
    for key in category_dict:
        sql = '''select title,text from business_opportunity_copy WHERE category_id_2="%s";'''%category_dict.get(key)
        res=db.query(sql)
        with open(category_dict.get(key)+key.decode('utf-8'),'w') as fw:
            for i in res:
                fw.write(i.get('title')+'\n'+i.get('text')+'\n')

if __name__ == '__main__':
    category_writeout()

