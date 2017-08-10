#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from sklearn.feature_extraction.text import  TfidfVectorizer
import mult_bayes_file_transf
reload(sys)
sys.setdefaultencoding("utf-8")
def test():
    with open("pVect_array","r") as fr1:
        lines=fr1.readlines()
        for line in lines:
            aa=line.split('\x01')
            # print aa
            # print len(aa)

    with open("vocablist", "r") as fr2:
        lines = fr2.readlines()
        for line in lines:
            ss = line.split('\x01')
            print ss
            print len(ss)


def tf_idf_test():
    with open('D://myfile/multclasscorpus/it','r') as fr:
        lines=fr.readlines()
        for line in lines:
            print line
            count_vec = TfidfVectorizer()
            print count_vec.fit_transform(mult_bayes_file_transf.rdfile2list('vocablist'))
            print type(count_vec.fit_transform(mult_bayes_file_transf.strline_cut_outstop(line)))
            print count_vec.fit_transform(mult_bayes_file_transf.strline_cut_outstop(line)).shape
            print len(mult_bayes_file_transf.strline_cut_outstop(line))
            break


if __name__ == '__main__':
    # test()
    tf_idf_test()