#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import torndb
import mysql_connect
import json
reload(sys)
sys.setdefaultencoding("utf-8")

#去重
def prod_Duplicate_rm():
    db=mysql_connect.mysql_connect()
    quchong='DELETE FROM product WHERE prodId IN (SELECT m_prodId FROM ' \
            '(SELECT max(prodId) as m_prodId,count(title) as count_t from product GROUP BY title HAVING count_t>1 ORDER BY prodId ASC) as tab);'

    max_count='SELECT max(count_t) as max_count FROM (SELECT max(prodId) ' \
              'as m_prodId,count(title) as count_t from product GROUP BY title HAVING count_t>1) as tab;'
    select_max=db.query(max_count)
    mcount=select_max[0].values()
    mcount=mcount[0]
    print mcount

    if mcount>1:
        for i in range(mcount-1):
            db.execute(quchong)

    db.close()


#获取商品参数
def get_prod_params():
    db=mysql_connect.mysql_connect()
    select_sql='SELECT prodId,SuperParams FROM product limit 10;'
    select_res=db.query(select_sql)
    for item in select_res:
        item_params=item.get('SuperParams')
        item_params=item_params[1:-1]
        params_list=item_params.split(',')
        for param in params_list:
            params_dict=eval(param)                                #字符串转换为字典
            for k,v in params_dict.items():
                print k+':'+v
        print '\n'                                                #每个商品之间有一个空行

    db.close()

if __name__ == '__main__':
    # prod_Duplicate_rm()                                      #去重
    get_prod_params()                                        #获取商品参数