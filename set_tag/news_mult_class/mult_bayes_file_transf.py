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
            listFromLine = line.split('\x01')
            returnMat[index, :] = listFromLine
            index += 1
    return returnMat


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
    strLine=strLine.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
    seg_list = jieba.cut(strLine, cut_all=False)
    seg_list_outstop = [w for w in seg_list if w not in stop]
    return seg_list_outstop


# print array([1,2,3,4])
# print type(array([1,2,3,4]))


