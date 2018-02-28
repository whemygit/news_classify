#!/usr/bin/env python
# -- coding: utf-8 --
from topic_news_get import topic_news
from topic_news_post import get_report_id,report_news_post



# mysql_params={
#     "host": "117.78.60.108",
#     "port": 3306,
#     "database": "cityparlor",
#     "password": "123456",
#     "user": "es",
#     "charset": "utf8"}

mysql_params={
    "host": "192.168.1.26",
    "port": 3306,
    "database": "cityparlor",
    "password": "123456",
    "user": "es",
    "charset": "utf8"}


# title_keywd_list=['英国首相','英首相','特雷莎']
# # keywd='英国首相'                                                             #获取有可能为专题的新闻
# report_id,report_area = get_report_id('英首相')                                        #获取专题id所用关键词
# other_keywd_list=['访华']

title_keywd_list=['冬奥会']
# keywd='英国首相'                                                             #获取有可能为专题的新闻
report_id,report_area= get_report_id('冬奥会')                                        #获取专题id所用关键词
other_keywd_list=['平昌']

for keywd in title_keywd_list:
    if other_keywd_list==[]:
        model=topic_news(mysql_params==mysql_params,keywd=keywd,area=report_area,other_keywd_list=[])
        for id,title,content in model.data_get():
            print(id,title)
            try:
                report_news_post(news_id=id, report_id=report_id)
                print('上传的标题为：',title)
            except:
                print('上传失败')
    else:
        model=topic_news(mysql_params=mysql_params,keywd=keywd,area=report_area,other_keywd_list=other_keywd_list)
        for id,title,content in model.data_get():
            flag=model.is_report_flag(content)
            if flag==True:
                try:
                    report_news_post(news_id=id, report_id=report_id)
                    print('上传的标题为：', title)
                except:
                    print('上传失败')
