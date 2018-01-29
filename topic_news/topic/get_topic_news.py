#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from html import unescape
import jieba
from textrank4zh import TextRank4Keyword
import pymysql
import re



class topic_news():
    def __init__(self,keywd,title_topic_list,content_topic_list):
        '''
        根据输入参数判断一条新闻是否属于设定的专题,
        使用keywd从众多新闻中筛选出标题包含keywd的新闻，缩小判定范围,原始数据可以有多种来源，此方法中是从mysql中抽取数据，从其他来源抽取需要对get_data方法稍加修改
        根据其他两个输入参数对新闻做进一步判断
        python3，需要的第三方库有html,jieba,textrank4zh,pymsql和re


        :param keywd: str类型,用于按标题查找时使用的主体关键词，例如‘特朗普访华’专题的主体‘特朗普’
        :param title_topic_list:list类型,标题主题词列表，所属专题新闻标题中很大可能包含的主题词列表，例如‘特朗普访华’专题的['特朗普','访华']
        :param content_topic_list:list类型,内容主题词列表，所属专题新闻标题中很大可能包含的主题词列表，例如‘特朗普访华’专题的['来华','中国','习近平','国事访问']
        '''
        self.mysql_params={
            "host": "117.78.60.108",
            "port": 3306,
            "database": "cityparlor",
            "password": "123456",
            "user": "es",
            "charset": "utf8"}
        self.keywd=keywd
        self.title_topic_list=title_topic_list
        self.content_topic_list=content_topic_list

    def data_get(self):
        '''
        从mysql依据keywd获取数据,如果title_topic_list和content_topic_list均为空，则仅用此方法
        :return:
        '''
        mysql=self.mysql_params
        conn=pymysql.connect(host=mysql.get('host'),port=mysql.get('port'),user=mysql.get('user'),passwd=mysql.get('password'),db=mysql.get('database'), charset=mysql.get('charset'))
        cur=conn.cursor()
        cur.execute('''SELECT title,content FROM t_top_news where title LIKE '%%{s}%%';'''.format(s=self.keywd))
        res_sql=cur.fetchall()
        cur.close()
        conn.close()
        for i in res_sql:
            title=i[0]
            content=i[1]
            yield title,content

    def is_topic_flag(self,title,content):
        '''
        根据新闻标题和新闻内容判别该新闻是否属于某一特定专题
        :param title:需要判别新闻的新闻标题
        :param content:需要判别新闻的新闻内容
        :return:topic_flag,True为属于该专题，False为不属于该专题
        '''

        topic_flag=False                         #专题标记
        keywd_extr_list = []                      #内容抽取的关键词列表


        content = unescape(content)               #内容去掉转义符合
        content = re.sub('<.*?>', '', content)    #内容去掉<>格式的html标签
        word = TextRank4Keyword()
        word.analyze(content)
        w_list = word.get_keywords(num=10)
        for i in w_list:
            keywd_extr_list.append(i.word)         #利用textrank方法提取内容的10个关键词

        title = unescape(title)
        titlew_list = jieba.cut(title, cut_all=False)
        titlew_list = [i for i in titlew_list]     #利用结巴分词获取标题分词列表

        #判别主题
        #情况1，根据标题判断，如果标题中包含self.title_topic_list中的全部主题关键词，则topic_flag=Ture
        if len(list(set(self.title_topic_list) & set(titlew_list))) == len(self.title_topic_list):
            topic_flag=True

        # 情况2，根据内容判断，如果内容抽取的关键词列表keywd_extr_list和self.content_topic_list有交集，则topic_flag=Ture
        elif list(set(self.content_topic_list) & set(keywd_extr_list)):
            topic_flag=True
        else:
            topic_flag=False

        return topic_flag





