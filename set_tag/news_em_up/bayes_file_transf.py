#!/usr/bin/env python
# -- coding: utf-8 --
#转换文件脚本，将读取的文件转换为需要的数据结构
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding("utf-8")


# 将读取的文本转换为数值型向量
import numpy
def rdfile2array(file_to_array):
    with open(file_to_array, "r") as afr:              #"D://myfile/spider_output/atest.txt"
        a = afr.read()
        p_array = numpy.array([float(w) for w in a.split("\x01")])
    return p_array


# 将读取的文本转换为列表
def rdfile2list(file_to_array):
    with open(file_to_array, "r") as afr:              #"D://myfile/spider_output/vocablist"
        a = afr.read()
        v_list = a.split("\x01")
    return v_list


#将一行字符串分词为不带停用词的词列表
def strline_cut_outstop(strLine):
    import jieba
    stop = [line.strip().decode('utf-8') for line in open("stopw.txt").readlines()]
    strLine.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
    seg_list = jieba.cut(strLine, cut_all=False)
    seg_list_outstop = [w for w in seg_list if w not in stop]
    return seg_list_outstop

