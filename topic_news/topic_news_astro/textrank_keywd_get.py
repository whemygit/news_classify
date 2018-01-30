#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import HTMLParser
import numpy as np
from textrank4zh import TextRank4Keyword,TextRank4Sentence
import torndb
from gensim import corpora
import operator
reload(sys)
sys.setdefaultencoding("utf-8")

class keywd_tr():
    '''
    通过主题关键词从mysql拿出相关新闻，再通过内容关键词找出权重比较大的词，最终打印。通过人工筛选组成列表，用于主题新闻的内容筛选条件。
    本程序运行的最终结果如：
    春运 729
    旅客 450
    铁路 277
    车票 207
    出行 206
    客流 202
    strong 199
    购票 191
    火车票 156
    工作 148
    记者 148
    安全 147
    运输 135
    列车 124
    span 119
    春运期间 119
    服务 110
    今年 97
    抢票 97
    部门 86
    '''
    def __init__(self,mysql_params,query_keywd):
        self.mysql_params=mysql_params
        self.query_keywd=query_keywd
        self.dictionary,self.bow_corpus,self.doc_array=self.get_vocab()
        self.vocablist_dict=self.get_keywd_dict()

    def get_slq_data(self):
        mysql=self.mysql_params
        db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                               user=mysql.get('user'),
                               password=mysql.get('password'), charset=mysql.get('charset'))

        query_sql = '''SELECT id,title,content FROM t_top_news where title LIKE '%%{s}%%';'''.format(s=self.query_keywd)
        res_sql = db.query(query_sql)
        return res_sql

    def get_doc_list(self):
        res = self.get_slq_data()
        html_parser = HTMLParser.HTMLParser()
        doc_list=[]
        for i in res:
            keyw_list = []
            news_id=i.get('id')
            news_title=i.get('title')
            news_content=i.get('content')
            content = html_parser.unescape(news_content)
            word = TextRank4Keyword()
            word.analyze(content)
            w_list = word.get_keywords(num=10)
            for i in w_list:
                keyw_list.append(i.word)
            doc_list.append(keyw_list)
        return doc_list


    def get_vocab(self):
        doc_list=self.get_doc_list()
        dictionary = corpora.Dictionary(doc_list)     #关键词词库字典
        # print len(dictionary)
        bow_corpus = [dictionary.doc2bow(text) for text in doc_list]     #bagofwords索引矩阵
        row_num = len(doc_list)
        col_num = len(dictionary)
        doc_array = np.zeros((row_num, col_num), dtype=int)               #bagofwords矩阵
        for i, j in enumerate(bow_corpus):
            for word_index, fre in j:
                doc_array[i][word_index] = fre
        return dictionary,bow_corpus,doc_array

    def get_keywd_dict(self):
        vocablist_dict = {}
        for k, v in self.dictionary.items():
            # print k, v
            vocablist_dict[v] = sum(self.doc_array[:, int(k)])
        return vocablist_dict

    def get_sort_dict(self,n=20):                           #获取内容关键词中前10个高权重词
        sorted_dict=sorted(self.vocablist_dict.iteritems(),key=operator.itemgetter(1),reverse=True)
        top_n=sorted_dict[0:n]
        for i in top_n:
            print i[0],i[1]


        # print len(doc_list)
        # print doc_list



if __name__ == '__main__':
    # 本地连接26服务器
    # mysql = {
    #     "host": "117.78.60.108",
    #     "port": "3306",
    #     "database": "cityparlor",
    #     "password": "123456",
    #     "user": "es",
    #     "charset": "utf8"
    # }
    # 服务器连接26服务器
    mysql = {
        "host": "192.168.1.26",
        "port": 3306,
        "database": "cityparlor",
        "password": "123456",
        "user": "es",
        "charset": "utf8"}

    keywd='春运'
    model=keywd_tr(mysql_params=mysql,query_keywd=keywd)
    # res=model.get_slq_data()
    # for i in res:
    #     print i
    model.get_sort_dict()