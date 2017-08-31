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

keywds_dict={
    "市政建设":"市政设施,公园,场馆,环保工程,批发市场,园林绿化,园区建设,道路建设,城镇建设,基础设施,产业园区,城市综合体,城市改造,搬迁,拆迁,城乡,社区",
    "土地开发":"土地,土地出让,土地转让,产业园区,特色城镇,廉租,房屋交易,开发合作,土地使用,土地租赁",
    "医疗康养":"药品,新药,药品销售,开发,医疗器械,生物医药,医疗执照,医养,养老,健康,保健,休闲养生,医药,康体,药材,养老院,社会福利院,颐老院,疗养院,康养",
    "能源矿产":"冶金,能源,矿,矿产,电力,热力,动力,煤,煤炭,石油,开采,金属,冶炼,化工,新材料,新能源,吨,钒钛钢铁稀土,燃料,天然气,煤层气,页岩气,石材",
    "知识产权":"商标,专利,品牌特许,创新,独创,产权,版权,发明,著作权,工业产权,商号",
    "文化创意":"媒介,广告,游戏电玩,广播,电影,电视,影视,电竞,文化创意,文化艺术,传媒,文案",
    "金融投资":"金融,金融执照,保险,证券,基金,资产,股债,股权,货币,资本",
    "交通运输":"运输工具,铁路,铁道,道路,公路,港口,码头,桥梁,涵洞,物流,支路建设,仓储,航运,空运,陆运,水运,船舶,航空,集装箱,民航,管道运输,配送,运输保管",
    "农林牧渔":"农牧生产,农牧加工,农牧销售,农牧技术,水利工程,水利灌溉,农业示范区,渔具,农业,林业,畜牧业,渔业,水产品,农产品,农产品加工,水产畜牧养殖,种植,家禽,蔬菜,肉类,林产品加工",
    "网络科技":"智慧城市,电信,网络技术,高新技术,信息技术,互联网,软件,生物科技,电子信息,网络",
    "先进制造":"食品加工,服装,纺织,电子家电,印刷出版,生物科技,机械化工,医药设备,汽摩制造,人工智能,制造,环保机械,新型材料,零部件,配件制造,加工配送,新材料,燃料,机械制造,装备制造,提纯,金属制造",
    "建筑建材":"房屋建设,建筑材料,装饰,装潢,贸易区,房地产,建材,装修,楼宇,楼盘,建筑",
    "旅游开发":"景区开发,酒店餐饮,休闲场所,游乐设备,湿地公园,文化旅游区,商业中心,交通枢纽,生态旅游,风景区,特色文化,再生资源,休闲,旅游纪念品,码头建设,养老旅游项目"
}

category_dict={
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

def set_category_id():
    sql = '''select bid,title,text from business_opportunity_copy limit 5;'''
    res = db.query(sql)
    for r in res:
        category_list=[]
        classify_dict={}
        print r.get('title')
        # print r.get('text')
        for i,keywds in enumerate(keywds_dict.values()):
            for keywd in keywds.split(","):
                if keywd in r.get('text'):
                    print keywd
                    category_list.append(category_dict.get(keywds_dict.keys()[i]))
                    if keywds_dict.keys()[i] not in classify_dict:
                        classify_dict.update({keywds_dict.keys()[i]: 1})
                    else:
                        classify_dict[keywds_dict.keys()[i]] += 1
        print category_list
        print classify_dict

if __name__ == '__main__':
    set_category_id()
    # for i,j in enumerate(keywds_dict.values()):
    #     print i,j,keywds_dict.keys()[i]
    #     for keywd in j.split(","):
    #         if keywd==j.split(",")[1]:
    #             print keywd
    #             break
