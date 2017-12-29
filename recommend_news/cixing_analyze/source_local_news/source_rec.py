#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb
from snownlp import SnowNLP

reload(sys)
sys.setdefaultencoding("utf-8")

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

def ns_source_rec():
    query_sql='''SELECT source FROM t_source_local_news;'''
    res_sql=db.query(query_sql)

    for i in res_sql:
        tags=SnowNLP(i.get('source').decode()).tags
        tag_list = []
        for j in tags:
            tag_list.append(j[1])
        print i.get('source'),SnowNLP(i.get('source').decode()).tags
        if u'nz' in tag_list or u'ns' in tag_list:
            print i.get('source')
            update_sql='''UPDATE t_source_local_news SET rec_flag='1' WHERE source = '{}';'''.format(i.get('source'))
            db.execute(update_sql)


if __name__ == '__main__':
    ns_source_rec()