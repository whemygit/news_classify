#!/usr/bin/env python
# -- coding: utf-8 --
import HTMLParser
import re
import sys
import json
import time

import MySQLdb
import datetime
city_key_recommend={"北京市":"铁路::公交系统::城市副中心::通州::怀柔::顺义::友谊医院::天坛医院::同仁医院::旧城保护::物流基地::北京段::城际铁路::火车站改建::新机场::清洁能源::研发::基因::卫星::研究所扩建::新能源::集成电路::纳米::中科院::产业园::金融中心::艺术小镇::国际文化::园艺::主题公园::夏日广场::干线工程::天然气工程::可再生::号线::机场线::南水北调::棚户区::胡同::园林绿化"}
def is_recommend(city_key_recommend,city_name,price,title,price_flag=20000000):
    reco_flage=0
    if price >= price_flag:
        if city_key_recommend.has_key(city_name):

            city_kes = city_key_recommend[city_name]
            for i in city_kes.split("::"):
                if i in title:
                    reco_flage = 1
                    print i
                    break

    return  reco_flage
