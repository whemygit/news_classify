#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import torndb
import time

reload(sys)
sys.setdefaultencoding("utf-8")

#连接数据库
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

now=time.strftime('%Y-%m-%d',time.localtime(time.time()))

#去重
def bo_Duplicate_rm():
    db=mysql_connect()
    quchong='DELETE FROM _news_data WHERE newsid IN (SELECT m_newsid FROM ' \
            '(SELECT max(newsid) as m_newsid,count(title) as count_t from _news_data GROUP BY title HAVING count_t>1 ORDER BY newsid ASC) as tab);'

    # quchong='DELETE FROM _news_data WHERE newsid IN (SELECT m_newsid FROM ' \
    #         '(SELECT max(newsid) as m_newsid,count(title) as count_t from _news_data where news_date=%s GROUP BY title HAVING count_t>1 ORDER BY newsid ASC) as tab);' %now

    max_count='SELECT max(count_t) as max_count FROM (SELECT max(newsid) ' \
              'as m_newsid,count(title) as count_t from _news_data GROUP BY title HAVING count_t>1) as tab;'
    select_max=db.query(max_count)
    mcount=select_max[0].values()
    mcount=mcount[0]
    print mcount

    if mcount>1:
        for i in range(mcount-1):
            db.execute(quchong)
    db.close()


if __name__ == '__main__':
    bo_Duplicate_rm()