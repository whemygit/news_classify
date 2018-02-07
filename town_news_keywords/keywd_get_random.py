#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import HTMLParser
import numpy as np
from textrank4zh import TextRank4Keyword,TextRank4Sentence
import torndb
from gensim import corpora
import operator
import random
reload(sys)
sys.setdefaultencoding("utf-8")

class keywd_tr():
    '''
    分批次随机，通过主题关键词从mysql拿出相关模块资讯一定百分比的随机id集合，再通过id获取内容提取关键词，生成批次份儿的关键词词库
    '''

    def __init__(self,mysql_params,query_sql_list):
        self.mysql_params=mysql_params
        self.query_sql_list=query_sql_list
        self.dictionary,self.bow_corpus,self.doc_array=self.get_vocab()
        self.vocablist_dict=self.get_keywd_dict()


    def get_slq_data(self):
        mysql=self.mysql_params
        db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                               user=mysql.get('user'),
                               password=mysql.get('password'), charset=mysql.get('charset'))
        for query_sql in self.query_sql_list:
            res_sql = db.query(query_sql)
            yield res_sql

    def get_doc_list(self):
        # res = self.get_slq_data()
        html_parser = HTMLParser.HTMLParser()
        doc_list=[]
        for i in self.get_slq_data():
            keyw_list = []
            news_id=i[0].get('id')
            news_title=i[0].get('title')
            news_content=i[0].get('content')
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

    def get_sort_dict(self,n=500):                           #获取内容关键词中前10个高权重词
        sorted_dict=sorted(self.vocablist_dict.iteritems(),key=operator.itemgetter(1),reverse=True)
        top_n=sorted_dict[0:n]
        for i in top_n:
            print i[0],i[1]
        return top_n


def get_categoryid_dict(mysql):
    cid_query_sql='''SELECT id,title FROM t_all_type WHERE fun='town_news';'''
    db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                           user=mysql.get('user'),
                           password=mysql.get('password'), charset=mysql.get('charset'))
    cid_dict = db.query(cid_query_sql)
    for i in cid_dict:
        yield i['id'],i['title']


def get_random_id(mysql,p_type_id):
    id_query_sql='''SELECT id FROM t_all_news WHERE p_type_id='{}';'''.format(p_type_id)
    db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                           user=mysql.get('user'),
                           password=mysql.get('password'), charset=mysql.get('charset'))
    id_list=[i.get('id') for i in db.query(id_query_sql)]
    random_sample_len = int(len(id_list)*0.1)
    print random_sample_len
    random_sample=random.sample(id_list,random_sample_len)
    return random_sample


if __name__ == '__main__':
    # 本地连接26服务器
    mysql = {
        "host": "117.78.60.108",
        "port": "3306",
        "database": "cityparlor",
        "password": "123456",
        "user": "es",
        "charset": "utf8"
    }
    # 服务器连接26服务器
    # mysql = {
    #     "host": "192.168.1.26",
    #     "port": 3306,
    #     "database": "cityparlor",
    #     "password": "123456",
    #     "user": "es",
    #     "charset": "utf8"}

#     for id,cname in get_categoryid_dict(mysql=mysql):
#         print id,cname
#         '''1709301224421460056 参政议政
# 1709301224421460293 发展规划
# 1709301224421460294 人事动态
# 1709301224421460295 法律法规
# 1709301224421460296 民生保障'''
#     t_all_news包含：293,294,296
#     for i in range(2,12):
#         print i


    cid_dict={'1709301224421460293':'fazhan','1709301224421460294':'renshi','1709301224421460296':'minsheng'}
    for cid,cid_title in cid_dict.items():
        print cid,cid_title
        for i in range(2,12):
            random_sample_id=get_random_id(mysql=mysql,p_type_id=cid)
            query_sql_list=[]
            for id in random_sample_id:
                query_sql_list.append('''SELECT id,title,content FROM t_all_news where id='{s}';'''.format(s=id))

            model=keywd_tr(mysql_params=mysql,query_sql_list=query_sql_list)

            top_n=model.get_sort_dict()
            with open(cid_title+str(i)+'key500','w') as fw:
                for i in top_n:
                    fw.write(i[0]+'\x01'+str(i[1])+'\n')


