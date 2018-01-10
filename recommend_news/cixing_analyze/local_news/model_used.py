#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
from numpy import *
from snownlp import SnowNLP
from sklearn.externals import joblib

reload(sys)
sys.setdefaultencoding("utf-8")



def get_attr_array(content):
    attr_array=zeros(2)
    print attr_array
    content_s=SnowNLP(content.decode())
    key_words=content_s.keywords(limit=10)
    k_n_len=0
    keywords_tag_list = []
    for i in key_words:
        print i,SnowNLP(i).tags[0][0],SnowNLP(i).tags[0][1]
        keywords_tag_list.append(SnowNLP(i).tags[0][1])
        if SnowNLP(i).tags[0][1].startswith('n'):
            k_n_len+=1
    cnt_nper=k_n_len/float(len(keywords_tag_list))
    print cnt_nper

    if 'e' in keywords_tag_list:
        cnt_ein = 1
    else:
        cnt_ein = 0

    print cnt_ein
    attr_array[0]=cnt_nper
    attr_array[1]=cnt_ein
    return attr_array

def predict_rec(text):
    rec_flag=False
    test_data=get_attr_array(content=text)
    test_data = np.array(test_data).reshape(1, -1)
    rf_load = joblib.load('rf.m')
    print rf_load.predict(test_data)
    if rf_load.predict(test_data)[0]==1:
        rec_flag=True
    print rec_flag

if __name__ == '__main__':
    str=''''''
    predict_rec(text=str)