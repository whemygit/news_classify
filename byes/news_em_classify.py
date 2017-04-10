#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import bayes
import bayes_test
from numpy import *
import numpy as np
import json
import torndb

reload(sys)
sys.setdefaultencoding("utf-8")

#利用bayes二分类算法对news_data数据进行情感分析，即改变em_teg字段值，0为负面，1为正面
###################################################################################################
#连接数据库
def mysql_connect():
    mysql_par={'ip':"192.168.0.202",
               'port':'3306',
               'database':'spider',
               'user':'root',
               'password':'neiwang-zhongguangzhangshi'}

    db=torndb.Connection(host=mysql_par['ip'],
                         database=mysql_par['database'],
                         user=mysql_par['user'],
                         password=mysql_par['password'])
    return db



def em_classify():
    db = mysql_connect()
    id_select = 'SELECT newsid FROM news_data;'
    newsid_list = db.query(id_select)
    for i in range(len(newsid_list)):
        sql='select * from news_data where newsid='+str(newsid_list[i].get('newsid'))
        res=db.query(sql)
        news_detail=res[0]                      #以news_data字段为键的字典
        news_id=news_detail.get('newsid')       #newsid
        news_text=news_detail.get('text')          #新闻正文

        MyVocablist=bayes_test.rdfile2list('vocablist')
        p_0=bayes_test.rdfile2array('p0')                                   #0类词库概率向量
        p_1=bayes_test.rdfile2array('p1')                                   #1类词库概率向量
        news_seg_list = bayes_test.strline_cut_outstop(news_text)
        wordVector = bayes.bagOfWords2VecMN(MyVocablist, news_seg_list)
        news_class=bayes.classifyNB(np.array(wordVector), p_0, p_1, 0.49)
        print news_class

        sql_ch_em='UPDATE news_data SET em_teg='+str(news_class)+' WHERE newsid='+str(news_id)+';'
        ch_em=db.execute(sql_ch_em)

    db.close()
#
# db=mysql_connect()
# id_select='SELECT newsid FROM news_data;'
# newsid_list=db.query(id_select)
# print type(newsid_list)
# print len(newsid_list)
# print newsid_list[0].get('newsid')
# print type(str(newsid_list[0].get('newsid')))

if __name__ == '__main__':
    em_classify()