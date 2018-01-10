
import numpy as np
from numpy import *
from snownlp import SnowNLP
from sklearn.externals import joblib
import jieba
import os
'''
根据文章标题、文章内容、文章来源查看是否推荐
'''

class recFlag():
    def __init__(self):
        self.model=joblib.load('D://gitcode/news_classify/recommend_news/news_first_page/rec_model.m')
        self.ban_source=['头条寻人','房产情报站']
        self.ban_words=['减肥','瘦身','介绍','预售价']

    def get_attr(self,title,content):
        '''
            :param title: 文章标题
            :param content: 文章内容
            :return: test_list，用于输入模型的参数特征值列表，依次为cnt_nper,cnt_ein,it_nfirst,tit_cnt_inter,tit_vin

            '''
        test_list = []
        title_s = SnowNLP(title)
        content_s = SnowNLP(content)
        t_tag = title_s.tags
        # 标题分词列表
        title_list = []
        # 标题词性列表
        title_tag_list = []
        for w1, w2 in t_tag:
            # print (w1,w2)
            title_list.append(w1)
            title_tag_list.append(w2)

        # 标题的第一个词是否为名词
        if 'n' in str(title_tag_list[0]):
            title_nfirst = 1
        else:
            title_nfirst = 0

        # 标题是否含有动词
        if 'v' in title_tag_list or 'vn' in title_tag_list:
            title_vin = 1
        else:
            title_vin = 0

        # 内容关键词列表
        key_words = content_s.keywords(limit=10)
        k_n_len = 0

        # 内容关键词词性列表
        keywords_tag_list = []
        for i in key_words:
            for t, s in SnowNLP(i).tags:
                keywords_tag_list.append(s)
                if str(s).startswith('n'):
                    k_n_len += 1

        # 内容关键字中名词占比
        cnt_nper = k_n_len / float(len(keywords_tag_list))

        # 内容关键字中是否含有标点符号等标注词性为e的项
        if 'e' in keywords_tag_list:
            cnt_ein = 1
        else:
            cnt_ein = 0

        # 标题与内容关键词是否有交集
        if list(set(title_list) & set(key_words)):
            tit_cnt_inter = 1
        else:
            tit_cnt_inter = 0

        test_list.append(cnt_nper)
        test_list.append(cnt_ein)
        test_list.append(title_nfirst)
        test_list.append(tit_cnt_inter)
        test_list.append(title_vin)
        # print (test_list)
        return test_list

    def predict_rec_flag(self,title,content,source):
        '''

            :param title: 文章标题
            :param content: 文章内容
            :param source: 文章来源
            :return: rec_flag,返回为TRUE则推荐，返回为FALSE则不推荐
            '''
        test_data = self.get_attr(title=title, content=content)
        test_data = np.array(test_data).reshape(1, -1)
        rf_load = self.model

        # print('模型预测结果，1表示推荐，0表示不推荐：',rf_load.predict(test_data))
        if rf_load.predict(test_data)[0] == 1:
            rec_flag = True
        # 如果source在ban_source内，则不推荐
        if source in self.ban_source:
            rec_flag = False

        # 如果标题中含有在ban_word内的词，则不推荐
        title_jieba_list = jieba.cut(title, cut_all=False)
        if list(set(title_jieba_list) & set(self.ban_words)):
            rec_flag = False
        print('rec_flag:', rec_flag)
        return rec_flag

