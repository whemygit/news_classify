#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb

mysql = {
    "host": "117.78.60.108",
    "port": "3306",
    "database": "cityparlor",
    "password": "123456",
    "user": "es",
    "charset": "utf8"
}

db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))


query_sql='''SELECT title,source,content FROM t_top_news WHERE create_date LIKE '%%{date}%%' AND language_version='ZH';'''.format(date='2017-12-27')
res_sql=db.query(query_sql)
for i in res_sql:
    print(i)
    break