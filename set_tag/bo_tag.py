#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import torndb
import mysql_connect

reload(sys)
sys.setdefaultencoding("utf-8")

#去重
def bo_Duplicate_rm():
    db=mysql_connect.mysql_connect()
    quchong='DELETE FROM business_opportunity_1 WHERE bid IN (SELECT m_bid FROM ' \
            '(SELECT max(bid) as m_bid,count(title) as count_t from business_opportunity_1 GROUP BY title HAVING count_t>1 ORDER BY bid ASC) as tab);'

    max_count='SELECT max(count_t) as max_count FROM (SELECT max(bid) ' \
              'as m_bid,count(title) as count_t from business_opportunity_1 GROUP BY title HAVING count_t>1) as tab;'
    select_max=db.query(max_count)
    mcount=select_max[0].values()
    mcount=mcount[0]
    print mcount

    if mcount>1:
        for i in range(mcount-1):
            db.execute(quchong)

    db.close()


#设置商机分类标签businessPid和businessId
def bo_tag_set():
    db=mysql_connect.mysql_connect()
    with open('set_pid_id','r') as fw:
        lines=fw.readlines()
        for line in lines:
            if line!='\n':
                update_sql=line.strip('\n')
                print update_sql
                db.execute(update_sql)
    db.close()

if __name__ == '__main__':
    bo_Duplicate_rm()
    bo_tag_set()