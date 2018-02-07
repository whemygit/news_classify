#!/usr/bin/env python
# -- coding: utf-8 --
import pymysql



class topic_news():
    def __init__(self,mysql_params,keywd,area,other_keywd_list=[]):
        '''
        根据输入参数判断一条新闻是否属于设定的专题,
        使用keywd从众多新闻中筛选出标题包含keywd的新闻，缩小判定范围,原始数据可以有多种来源，此方法中是从mysql中抽取数据，从其他来源抽取需要对get_data方法稍加修改
        根据其他两个输入参数对新闻做进一步判断
        python3，需要的第三方库有html,jieba,textrank4zh,pymsql和re


        :param keywd: str类型,用于按标题查找时使用的主体关键词，例如‘特朗普访华’专题的主体‘特朗普’
        '''

        self.mysql_params=mysql_params
        self.keywd=keywd
        self.area=area
        self.other_keywd_list=other_keywd_list


    def data_get(self):
        '''
        从mysql依据keywd获取数据,如果title_topic_list和content_topic_list均为空，则仅用此方法
        :return:
        '''
        mysql=self.mysql_params
        conn=pymysql.connect(host=mysql.get('host'),port=mysql.get('port'),user=mysql.get('user'),passwd=mysql.get('password'),db=mysql.get('database'), charset=mysql.get('charset'))
        cur=conn.cursor()
        cur.execute(
            '''SELECT id,title,content FROM t_top_news where title LIKE '%%{s}%%' AND area='{area}' and report_id is NULL AND pics is not NULL AND create_date LIKE '%%{date}%%';'''.format(
                s=self.keywd,date='2018',area=self.area))
        res_sql=cur.fetchall()
        cur.close()
        conn.close()
        for i in res_sql:
            news_id=i[0]
            news_title=i[1]
            news_content=i[2]
            yield news_id,news_title,news_content


    def is_report_flag(self,content):
        '''
        根据新闻内容判别该新闻是否属于某一特定专题，内容中包含关键词other_keywd_list中的词则推送为专题，否则不推送
        :param title:需要判别新闻的内容
        :return:report_flag,True为属于该专题，False为不属于该专题
        '''
        report_flag = False  # 专题标记
        for i in self.other_keywd_list:
            if i in content:
                report_flag=True
                return report_flag


