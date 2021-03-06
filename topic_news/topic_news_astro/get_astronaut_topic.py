#!/usr/bin/env python
# -- coding: utf-8 --
from topic_news_post import get_report_id,report_news_post
import pymysql



class astronaut_topic_news():
    def __init__(self,keywd,other_keywd_list):
        '''
        根据输入参数判断一条新闻是否属于设定的专题,
        使用keywd从众多新闻中筛选出标题包含keywd的新闻，缩小判定范围,原始数据可以有多种来源，此方法中是从mysql中抽取数据，从其他来源抽取需要对get_data方法稍加修改
        根据其他两个输入参数对新闻做进一步判断
        python3，需要的第三方库有html,jieba,textrank4zh,pymsql和re


        :param keywd: str类型,用于按标题查找时使用的主体关键词，例如‘特朗普访华’专题的主体‘特朗普’
        '''
        # self.mysql_params={
        #     "host": "117.78.60.108",
        #     "port": 3306,
        #     "database": "cityparlor",
        #     "password": "123456",
        #     "user": "es",
        #     "charset": "utf8"}
        self.mysql_params={
            "host": "192.168.1.26",
            "port": 3306,
            "database": "cityparlor",
            "password": "123456",
            "user": "es",
            "charset": "utf8"}

        self.keywd=keywd
        self.other_keywd_list=other_keywd_list


    def data_get(self):
        '''
        从mysql依据keywd获取数据,如果title_topic_list和content_topic_list均为空，则仅用此方法
        :return:
        '''
        mysql=self.mysql_params
        conn=pymysql.connect(host=mysql.get('host'),port=mysql.get('port'),user=mysql.get('user'),passwd=mysql.get('password'),db=mysql.get('database'), charset=mysql.get('charset'))
        cur=conn.cursor()
        cur.execute('''SELECT id,title FROM t_top_news where title LIKE '%%{s}%%' AND report_id is NULL AND pics is not NULL;'''.format(s=self.keywd))
        res_sql=cur.fetchall()
        cur.close()
        conn.close()
        for i in res_sql:
            news_id=i[0]
            news_title=i[1]
            yield news_id,news_title


    def is_report_flag(self,title):
        '''
        根据新闻标题判别该新闻是否属于某一特定专题
        :param title:需要判别新闻的新闻标题
        :return:report_flag,True为属于该专题，False为不属于该专题
        '''
        report_flag = False  # 专题标记
        for i in self.other_keywd_list:
            if i in title:
                report_flag=True
                return report_flag


keywd='航天员'
other_keywd_list=['中国','群体','新时代','忠诚','英雄']
report_id = get_report_id('航天员')

model=astronaut_topic_news(keywd=keywd,other_keywd_list=other_keywd_list)
for id,title in model.data_get():
    report_flag=model.is_report_flag(title=title)
    print(id,title,report_flag)
    if report_flag:
        try:
            report_news_post(news_id=id, report_id=report_id)
            print('上传的标题为：',title)
        except:
            print('上传失败')