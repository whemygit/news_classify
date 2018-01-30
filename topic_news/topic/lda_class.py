#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
from html import unescape
from gensim import corpora
import lda
import jieba
import pymysql
import re


class LdaTopicWords():
    def __init__(self,data_source):
        self.data_source = data_source
        self.title_list,self.doc_list=self.get_doc_list()
        self.vocab_dictionary,self.vocab=self.get_vocab()
        self.doc_num=len(self.doc_list)
        self.word_num=len(self.vocab)
        self.bow_corpus_array=self.get_bow_corpus_array()
        self.stopwd=[line.strip().decode('utf-8') for line in open('stopw.txt','rb').readlines()]



    def get_data_sql(self):
        keywd='春运'
        mysql_params={
            "host": "117.78.60.108",
            "port": 3306,
            "database": "cityparlor",
            "password": "123456",
            "user": "es",
            "charset": "utf8"}
        mysql=mysql_params
        conn=pymysql.connect(host=mysql.get('host'),port=mysql.get('port'),user=mysql.get('user'),passwd=mysql.get('password'),db=mysql.get('database'), charset=mysql.get('charset'))
        cur=conn.cursor()
        cur.execute('''SELECT title,content FROM t_top_news where title LIKE '%%{s}%%';'''.format(s=keywd))
        res_sql=cur.fetchall()
        cur.close()
        conn.close()
        for i in res_sql:
            title=i[0]
            content=i[1]
            yield title,content


    def get_data_file(self):
        with open('email.txt','rb') as fr:
            lines=fr.readlines()
            for line in lines:
                try:
                    line_list=line.strip().decode('utf-8').split('\t')
                    title = line_list[0]
                    content = line_list[1]
                    content = re.sub('<.*?>', '', content)
                    content = re.sub('\n', '', content)
                    content = unescape(content)

                    yield title,content
                except:
                    continue


    def get_doc_list(self):
        doc_list=[]
        title_list=[]
        source=self.data_source
        if source=='sql':
            res=self.get_data_sql()
        else:
            res=self.get_data_file()
        for title,content in res:
            try:
                title_list.append(unescape(title))
                title=unescape(title)
                content=unescape(content)
                content = re.sub('<.*?>', '', content)
                # print(title,content)
                content_list=jieba.cut(content,cut_all=False)
                # print(content_list)
                content_list_1=[]
                for i in content_list:
                    # 是否去掉停用词
                    if i in self.stopwd:
                        continue
                    else:
                        content_list_1.append(i)

                doc_list.append(content_list_1)

            except:
                continue
            # print(doc_list)
                    # break
        # doc_list=[
        #     ['新春', '备', '年货', '新年', '联欢晚会', '备'],
        #     ['新春', '节目单', '春节', '联欢晚会', '红火'],
        #     ['大盘', '下跌', '股市', '散户'],
        #     ['下跌', '股市', '赚钱'],
        #     ['金猴', '新春', '红火', '新年'],
        #     ['新车', '新年', '年货', '新春'],
        #     ['股市', '反弹', '下跌'],
        #     ['股市', '散户', '赚钱'],
        #     ['新年', '看', '春节', '联欢晚会'],
        #     ['大盘', '下跌', '散户']
        # ]
        return title_list,doc_list


    def get_vocab(self):
        dictionary = corpora.Dictionary(self.doc_list)
        vocab_dictionary=dictionary.token2id
        vocablist=[]
        for k, v in dictionary.items():
            vocablist.append(v)
        vocab = tuple(vocablist)
        return vocab_dictionary,vocab


    def get_bow_corpus_array(self):
        dictionary = corpora.Dictionary(self.doc_list)
        bow_corpus = [dictionary.doc2bow(text) for text in self.doc_list]

        bow_corpus_array = np.zeros((self.doc_num, self.word_num), dtype=int)
        for i, j in enumerate(bow_corpus):
            for word_index, fre in j:
                bow_corpus_array[i][word_index] = fre
        return bow_corpus_array

    def lda_model(self):
        lda_model = lda.LDA(n_topics=5, n_iter=2000, random_state=1)
        lda_model.fit(self.bow_corpus_array)
        topic_word = lda_model.topic_word_
        print(topic_word.shape)
        n_top_words = 20
        for i, topic_dist in enumerate(topic_word):
            topic_words = np.array(self.vocab)[np.argsort(topic_dist)][:-(n_top_words + 1):-1]
            print('Topic {}: {}'.format(i, ' '.join(topic_words)))

        doc_topic = lda_model.doc_topic_
        print(doc_topic.shape)
        # print(doc_topic)

        for n in range(10):
            topic_most_pr = doc_topic[n].argmax()
            print("doc:{} topic:{}".format(n, topic_most_pr))



model=LdaTopicWords(data_source='sql')
# for title,content in model.get_data_sql():
#     print(title,content)
# print(model.data_source)
# print(model.stopwd)
# print(model.doc_list)
# print(model.vocab_dictionary)
# print(model.vocab)
# print(model.doc_num)
# print(model.word_num)
# print(model.bow_corpus_array)
model.lda_model()
# print(len(model.title_list))
# print(len(model.doc_list))
