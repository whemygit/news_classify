#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb
import numpy as np
from numpy import *
import random
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



# 297个城市列表
def define_city_list():
    with open('city_list', 'r') as fr:
        city_list_1 = fr.readlines()
        city_list = []
        print 'len(city_list):' + str(len(city_list_1))
        for city in city_list_1:
            city_list.append(city.strip())
    return city_list

def rec_prodid_select(city):
    db = mysql_connect()
    prod_select = 'SELECT prodId FROM product WHERE area LIKE \'%%{s}%%\';'.format(s=city)
    prod_res = db.query(prod_select)
    prodid_list=[]
    for prod in prod_res:
        prodid_list.append(prod.get('prodId'))
    # print prodid_list
    # if prodid_list!=[]:
    #     rand_prodid = random.sample(prodid_list, 1)
    # print rand_prodid
    return prodid_list
    db.close()

# 根据生成的各市随机prodId选取各市推荐prod
def rec_prod_select():
    db=mysql_connect()
    for city in define_city_list():
        if rec_prodid_select(city):
            rand_prodid=random.sample(rec_prodid_select(city),1)
            prod_select='SELECT * FROM product WHERE prodId={n};'.format(n=rand_prodid[0])
            rec_prod_res=db.query(prod_select)
            print rec_prod_res
    db.close()


if __name__ == '__main__':
    # rec_prodid_select('北京市')
    # 列表各城市中随机选取的product序号列表
    # for i in define_city_list():
    #     if rec_prodid_select(i):
    #         rand_prodid=random.sample(rec_prodid_select(i),1)
    #         print rec_prodid_select(i)
    #         print rand_prodid
    rec_prod_select()
