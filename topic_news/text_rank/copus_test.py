#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import HTMLParser
import jieba
from textrank4zh import TextRank4Keyword,TextRank4Sentence
import torndb

reload(sys)
sys.setdefaultencoding("utf-8")

def test_data_get():
    mysql = {
        "host": "117.78.60.108",
        "port": "3306",
        "database": "cityparlor",
        "password": "123456",
        "user": "es",
        "charset": "utf8"
    }

    db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                           user=mysql.get('user'),
                           password=mysql.get('password'), charset=mysql.get('charset'))


    query_sql='''SELECT title,content FROM t_top_news where title LIKE '%%特朗普%%';'''
    res_sql=db.query(query_sql)
    return res_sql


def test():
    res=test_data_get()
    html_parser = HTMLParser.HTMLParser()
    topic_title_list = [u'特朗普', u'访华']
    key_word=u'特朗普'
    topic_content_list=[u'来华',u'中国',u'习近平',u'国事访问']
    with open('test1','w') as fw1,open('test2','w') as fw2:
        for i in res:
            keyw_list=[]
            title=i.get('title')
            content=i.get('content')
            content = html_parser.unescape(content)
            word = TextRank4Keyword()
            word.analyze(content)
            titlew_list=jieba.cut(title,cut_all=False)
            titlew_list=[i for i in titlew_list]
            w_list = word.get_keywords(num=10)
            for i in w_list:
                keyw_list.append(i.word)
            if len(list(set(topic_title_list) & set(titlew_list))) == 2 :
                print '\x01'.join(titlew_list)
                print '1', title, ':::', ','.join(keyw_list),':::','\x01'.join(titlew_list)
                fw1.write(title + ':' + ','.join(keyw_list) + '\n')
            elif list(set(topic_content_list) & set(keyw_list)):

                print '1', title,':',','.join(keyw_list),':::','\x01'.join(titlew_list)
                fw1.write(title+':'+','.join(keyw_list)+'\n')

            else:
                print '2',title, ':::',','.join(keyw_list),':::','\x01'.join(titlew_list)
                fw2.write(title+':'+','.join(keyw_list)+'\n')


if __name__ == '__main__':
    # test()
    res=test_data_get()
    for i in res:
        title=i.get('title')
        content=i.get('content')
        print title,content