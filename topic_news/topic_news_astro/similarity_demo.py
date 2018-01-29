#!/usr/bin/env python
# -- coding: utf-8 --
import logging
import jieba
from gensim import corpora, models, similarities

"""
主要求文章标题的相似性
similarity 方法来计算相似性
返回值 为 False的话是相似性高的
依赖的 python 包 有 jieba gensim 
"""
class similarityDemo():
    def __init__(self):
        self.raw_documents = []

    def similarity(self,querydata):
        flag = True
        if len(self.raw_documents) == 0:
            self.raw_documents.append(querydata)
            self.raw_documents.append(",;")
            return flag

        # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

        texts = [[word for word in jieba.cut(document)] for document in self.raw_documents]
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]

        tfidf = models.TfidfModel(corpus)

        corpus_tfidf = tfidf[corpus]

        query = [text for text in jieba.cut(querydata)]

        vec_bow = dictionary.doc2bow(query)
        vec_tfidf = tfidf[vec_bow]

        index = similarities.MatrixSimilarity(corpus_tfidf,num_features=len(dictionary))
        # index = similarities.Similarity('Similarity-tfidf-index',corpus_tfidf,num_features=600)
        # logging.info( index.get_similarities(vec_tfidf))
        # print  len(index.get_similarities(vec_tfidf))
        # for sim in index.get_similarities(vec_tfidf):
        for sim in index[vec_tfidf]:
            if sim > 0.80:
                # print sim
                flag = False
            else:
                self.raw_documents.append(querydata)

        return flag
