#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import numpy as np
from numpy import *
reload(sys)
sys.setdefaultencoding("utf-8")

import bayes_multiple_class

# 将读取的文本转换为数值型向量
import numpy
def rdfile2array(file_to_array):
    with open(file_to_array, "r") as afr:              #"D://myfile/spider_output/atest.txt"
        a = afr.read()
        p_array = numpy.array([float(w) for w in a.split("\x01")])
    return p_array

#将读取的文本转换为矩阵
def file2matrix(filename):
    with open(filename, 'r') as fr:
        lines = fr.readlines()
        numOfLines = len(lines)
        eachline_len = len(lines[0].strip().split('\x01'))
        returnMat = zeros((numOfLines, eachline_len))
        index = 0
        for line in lines:
            line = line.strip()
            listFromLine = line.split('\t')
            returnMat[index, :] = listFromLine
            index += 1
    return returnMat

# with open('D://myfile/machine_learning_code/machinelearninginaction/Ch02/datingTestSet2.txt','r') as fr:
#     lines=fr.readlines()
#     numOfLines=len(lines)
#     eachline_len=len(lines[0].strip().split('\t'))
#     returnMat=zeros((numOfLines,eachline_len))
#     index=0
#     for line in lines:
#         line=line.strip()
#         listFromLine=line.split('\t')
#         returnMat[index,:]=listFromLine
#         index+=1
#     print returnMat[1]


# 将读取的文本转换为列表
def rdfile2list(file_to_array):
    with open(file_to_array, "r") as afr:              #"D://myfile/spider_output/vocablist"
        a = afr.read()
        v_list = a.split("\x01")
    return v_list



#将一行字符串分词为不带停用词的词列表
def strline_cut_outstop(strLine):
    import jieba
    stop = [line.strip().decode('utf-8') for line in open("D://myfile/stopw.txt").readlines()]
    strLine.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
    seg_list = jieba.cut(strLine, cut_all=False)
    seg_list_outstop = [w for w in seg_list if w not in stop]
    return seg_list_outstop


def main(infile_name,class1_file,class0_file):
    '''主要功能：利用bayes_main训练的贝叶斯模型参数测试新的测试集，即对新的要分类的文本用训练好的分类器分类
    输入：待分类的文本（包含多条新闻，每行一条）文件名，类型1结果文件名，类型0结果文件名
    输出：类型1结果文件，类型0结果文件'''
    import bayes
    import numpy as np
    MyVocablist=rdfile2list('D://myfile/spider_output/vocablist')
    with open(infile_name,'r') as fr,open(class1_file,'a') as f1,open(class0_file,'a') as f0:
        lines=fr.readlines()
        for line_index in range(len(lines)):
            line_seg_list=strline_cut_outstop(lines[line_index])
            wordVector = bayes_multiple_class.bagOfWords2Vec(MyVocablist, line_seg_list)
            if bayes_multiple_class.classifyNB(np.array(wordVector), rdfile2array('D://myfile/spider_output/p0'), rdfile2array('D://myfile/spider_output/p1'), 0.49)==1:
                f1.write(lines[line_index])
            else:
                f0.write(lines[line_index])


# if __name__ == '__main__':
#     main('D://myfile/bayestest/news_from_json','D://myfile/bayestest/sample_class1','D://myfile/bayestest/sample_class0')
print [2]*5      #类别列表

#遍历文件夹下的所有文件
s=os.sep
root='D://myfile'

for i in os.listdir(root):
    print i
    print type(i)
