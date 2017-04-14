#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import mysql_connect
reload(sys)
sys.setdefaultencoding("utf-8")

#297个城市列表
def define_city_list():
    with open('D://myfile/city_list','r') as fr:
        city_list= fr.readlines()
        print 'len(city_list):'+str(len(city_list))
        # for city in city_list:
        #     print city.strip()
    return city_list


#新闻城市列表
def news_city_list_get():
    '''关联字段序列获取函数'''
    db = mysql_connect.mysql_connect()
    select_sql='SELECT area FROM (SELECT newsid, area FROM news_data GROUP BY area) as tab;'
    select_res=db.query(select_sql)
    news_city_list=[]
    for city in select_res:
        city_name=city.get('area')
        # print city_name
        news_city_list.append(city_name)
    print 'len(news_city_list):'+str(len(news_city_list))
    return news_city_list
    db.close()


#bo城市列表
def bo_city_list_get():
    '''关联字段序列获取函数'''
    db = mysql_connect.mysql_connect()
    select_sql='SELECT city FROM (SELECT bid, city FROM business_opportunity_1 GROUP BY city) as tab;'
    select_res=db.query(select_sql)
    bo_city_list=[]
    for city in select_res:
        city_name=city.get('city')
        # print city_name
        bo_city_list.append(city_name)
    print 'len(bo_city_list):'+str(len(bo_city_list))
    return bo_city_list
    db.close()

#bo城市列表
def prod_city_list_get():
    '''关联字段序列获取函数'''
    db = mysql_connect.mysql_connect()
    select_sql='SELECT area FROM (SELECT prodId, area FROM product GROUP BY area) as tab;'
    select_res=db.query(select_sql)
    prod_city_list=[]
    for city in select_res:
        city_name=city.get('area')
        # print city_name
        prod_city_list.append(city_name)
    print 'len(prod_city_list):'+str(len(prod_city_list))
    return prod_city_list
    db.close()


#bo城市列表
def comp_city_list_get():
    '''关联字段序列获取函数'''
    db = mysql_connect.mysql_connect()
    select_sql='SELECT city FROM (SELECT Id, city FROM company GROUP BY city) as tab;'
    select_res=db.query(select_sql)
    comp_city_list=[]
    for city in select_res:
        city_name=city.get('city')
        # print city_name
        comp_city_list.append(city_name)
    print 'len(comp_city_list):'+str(len(comp_city_list))
    return comp_city_list
    db.close()

if __name__ == '__main__':
    city_list=define_city_list()
    news_city_list=news_city_list_get()
    bo_city_list=bo_city_list_get()
    prod_city_list=prod_city_list_get()
    comp_city_list=comp_city_list_get()
    # prod_city_list1 = []
    # for city in prod_city_list:
    #     prod_city_list1.append(city)
    # print prod_city_list1
    # print prod_city_list1==prod_city_list


    #
    # news_no_city=[city for city in city_list if city not in comp_city_list]
    # print 'len(news_no_city):'+str(len(news_no_city))
    # for city in news_no_city:
    #     print city.strip()

    # bo_no_city=[city for city in city_list if city not in bo_city_list]
    # print 'len(bo_no_city):'+str(len(bo_no_city))
    # for city in bo_no_city:
    #     print city.strip()
    #
    # prod_no_city = [city for city in city_list if city not in prod_city_list]
    # print 'len(prod_no_city):' + str(len(prod_no_city))
    # for city in prod_no_city:
    #     print city.strip()