#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
from gensim import corpora
import numpy as np
import operator


reload(sys)
sys.setdefaultencoding("utf-8")


class KeyWdStat():
    def __init__(self,file_path):
        self.file_path=file_path
        self.dictionary, self.doc_list=self.get_kw_vocab()

    def get_kw_vocab(self):
        file_list=os.listdir(self.file_path)
        doc_list=[]
        for file in file_list:
            with open(self.file_path+'/'+file,'r') as fr:
                lines=fr.readlines()
                kw_list=[line.split('\x01')[0] for line in lines]
                doc_list.append(kw_list)
        dictionary = corpora.Dictionary(doc_list)     #索引为键，词为值
        return dictionary,doc_list

    def get_kw_final(self):
        row_num = len(self.doc_list)
        print row_num
        col_num = len(self.dictionary)
        print col_num

        bow_corpus = [self.dictionary.doc2bow(text) for text in self.doc_list]
        doc_array = np.zeros((row_num, col_num), dtype=int)
        print doc_array.shape
        for i, j in enumerate(bow_corpus):
            for word_index, fre in j:
                doc_array[i][word_index] = fre
        print self.dictionary[0]

        vocab_dict={}
        for k,v in self.dictionary.items():
            vocab_dict[v]=sum(doc_array[:, int(k)])
        sorted_dict = sorted(vocab_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
        with open(self.file_path.split('/')[0] + '/' +self.file_path.split('/')[1]+ 'kw_list', 'w') as fw:
            for key,value in sorted_dict:
                print key,value
                fw.write(key+'\x01'+str(value)+'\n')

def fazzhanguihua_kw():
    model = KeyWdStat(file_path='keywd_500/fazhan')
    model.get_kw_final()

def renshidongtai_kw():
    model = KeyWdStat(file_path='keywd_500/renshi')
    model.get_kw_final()

def minshengbaozh_kw():
    model = KeyWdStat(file_path='keywd_500/minsheng')
    model.get_kw_final()

if __name__ == '__main__':
    # fazzhanguihua_kw()
    # renshidongtai_kw()
    minshengbaozh_kw()