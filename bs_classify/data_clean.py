#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb
import json
import datetime

reload(sys)
sys.setdefaultencoding("utf-8")

def mysql_connect():
    mysql_par={'ip':"192.168.0.202",
               'port':'3306',
               'database':'spider',
               'user':'root',
               'password':'neiwang-zhongguangzhangshi'}

    # mysql_par = {'ip': "192.168.1.8",
    #              'port': '3306',
    #              'database': 'cityparlor',
    #              'user': 'bigdata',
    #              'password': 'zhongguangzhangshi'}


    db=torndb.Connection(host=mysql_par['ip'],
                         database=mysql_par['database'],
                         user=mysql_par['user'],
                         password=mysql_par['password'])
    return db


def extract_title_text(tab_name):
    db=mysql_connect()
    select_sql='''select bid,title,text from %s limit 1000''' %tab_name
    res=db.query(select_sql)
    with open('business_opportunity_testdata','w') as fw:
        for r in res:
            fw.write(str(r.get('bid'))+'\x01'+r.get('title')+'\x01'+r.get('text')+'\n')
            print r.get('bid')
    db.close()
ss='city_outer'
def area_code_get():
    db = mysql_connect()
    select_sql = '''select id,name from t_area where signs like \'%city_outer%\''''
    res = db.query(select_sql)
    for i in res:
        print i
    # with open('business_opportunity_testdata', 'w') as fw:
    #     for r in res:
    #         fw.write(str(r.get('bid')) + '\x01' + r.get('title') + '\x01' + r.get('text') + '\n')
    #         print r.get('bid')
    # db.close()



if __name__ == '__main__':
    area_code_get()