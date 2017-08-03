#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import bayes_multiple_class
import mult_bayes_file_transf
from numpy import *
import numpy as np
import json
import torndb
reload(sys)
sys.setdefaultencoding("utf-8")

def mult_classify(news_text):
    MyVocablist=mult_bayes_file_transf.rdfile2list('vocablist')
    pVect_array=mult_bayes_file_transf.file2matrix('pVect_array')            #各类词库概率矩阵
    array_class_p_list=mult_bayes_file_transf.rdfile2array('array_class_p_list')   #各类新闻占比向量
    news_seg_list =mult_bayes_file_transf.strline_cut_outstop(news_text)
    wordVector = bayes_multiple_class.bagOfWords2Vec(MyVocablist, news_seg_list)
    news_class=bayes_multiple_class.classifyNB(np.array(wordVector), pVect_array,array_class_p_list,array([1,2,3,4]))
    print news_class


if __name__ == '__main__':
    with open('D://myfile/multclasscorpus/business','r') as fr:
        lines=fr.readlines()
        for line in lines:
            mult_classify(line)