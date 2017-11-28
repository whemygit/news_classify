#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import json
from html.parser import HTMLParser
import re
from jsonstr import jsonstr,city_key_recommend,industry_keywords_recommend



"""
bussiness 商机分类关键字字典
title  商机文章标题
context 商机文章内容

返回字典{
business_pid_1："12,4", 商机分类的大类
business_id_1:"12_1,4_2" 商机分类的小类

}
"""



def business_predict(title,jsonstr = jsonstr,default_pid='1708271201536210157'):
    predict_pid =set()
    predict_id =set()
    json_ob=json.loads(jsonstr)
    for jsob in json_ob:
        if jsob['key_words'] in title:
             pid= jsob['pid']
             id= jsob['id']
             predict_pid.add(pid)
             predict_id.add(id)
    # print  len(predict_pid)
    if len(predict_pid)==0:
        predict_pid.add(default_pid)

    # if len(predict_id) == 0:
    #     predict_id.add(default_pid)
    pid_str=','.join(predict_pid)
    id_str=','.join(predict_id)

    return {"business_pid_1":pid_str,"business_id_1":id_str}



# # 获取商机的金额
# unit_dict = {
#     '万': '0000',
#     '十万': '00000',
#     '百万': '000000',
#     '千万': '0000000',
#     '亿': '00000000',
#     '十亿': '000000000',
#     '百亿': '0000000000',
#     '千亿': '00000000000'
# }
#
# def get_money(content):
#     if not content:
#         return content
#     html = HTMLParser()
#     content_html = html.unescape(content)
#     content_html = html.unescape(content_html)
#     unit_list = ['', '万', '十万', '百万', '千万', '亿', '十亿', '百亿', '千亿']
#     regex_list = ['工程规模.*?(\d+){unit}元', '投资.*?(\d+){unit}元', '预算.*?(\d+){unit}元', '采购.*?(\d+){unit}元',
#                   '项目.*?(\d+){unit}元', '总额.*?(\d+){unit}元', '金额.*?(\d+){unit}元', '概算.*?(\d+){unit}元']
#     s = re.sub('<[^>]*>', '', content_html)
#     is_match = False
#     limit = 0
#     for regex in regex_list:
#         if is_match:
#             break
#         for unit in unit_list:
#             reg = regex.format(unit=unit)
#             res = re.findall(reg, s)
#             if res:
#                 if not unit and int(res[0]) < 1000 or int(res[0]) == 0:
#                     continue
#                 if unit:
#                     limit = res[0] + unit_dict.get(unit)
#                 else:
#                     limit = res[0]
#                 is_match = True
#                 break
#     return limit

unit_dict = {
    '万': 10000,
    '十万': 100000,
    '百万': 1000000,
    '千万': 10000000,
    '亿': 100000000,
    '十亿': 1000000000,
    '百亿': 10000000000,
    '千亿': 100000000000
}

def get_money(content):
    limit = 0
    if not content:
        return limit
    html = HTMLParser()
    content_html = html.unescape(content)
    content_html = html.unescape(content_html)
    unit_list = ['', '万', '十万', '百万', '千万', '亿', '十亿', '百亿', '千亿']
    regex_list = ['工程规模.*?(\d+[\.]?\d+){unit}元', '总?投资.*?(\d+[\.]?\d+){unit}元', '预算.*?(\d+[\.]?\d+){unit}元',
                  '采购.*?(\d+[\.]?\d+){unit}元',
                  '项目.*?(\d+[\.]?\d+){unit}元', '总额.*?(\d+[\.]?\d+){unit}元', '金额.*?(\d+[\.]?\d+){unit}元',
                  '概算.*?(\d+[\.]?\d+){unit}元']
    s = re.sub('<[^>]*>', '', content_html)
    s = s.replace(" ", "")
    is_match = False

    for regex in regex_list:
        if is_match:
            break
        for unit in unit_list:
            reg = regex.format(unit=unit)

            res = re.findall(reg, s)

            if res:
                if not unit and float(res[0]) < 1000 or float(res[0]) == 0:
                    continue
                if unit:
                    limit = float(res[0]) * unit_dict.get(unit)

                else:
                    limit = res[0]

                is_match = True
                break

    return limit



def is_recommend(city_name,price,title,city_key_recommend=city_key_recommend,price_flag=20000000):
    reco_flage=0
    if float(price) >= price_flag:
        # if city_key_recommend.has_key(city_name):
        if city_name in city_key_recommend.keys():
            city_kes = city_key_recommend[city_name]
            for i in city_kes.split("::"):
                if i in title:
                    reco_flage = 1
                    print (i)
                    break
    return  reco_flage

def is_full_recommend(price,title,industry_keywords_recommend=industry_keywords_recommend,price_flag=20000000):
    reco_flage=0
    if float(price) >= price_flag:
            city_kes = industry_keywords_recommend.split("::")
            for i in city_kes:
                if i in title:
                    reco_flage = 1
                    print (i)
                    break

    return  reco_flage
