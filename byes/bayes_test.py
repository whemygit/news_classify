#!/usr/bin/env python
# -- coding: utf-8 --
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
            wordVector = bayes.bagOfWords2VecMN(MyVocablist, line_seg_list)
            if bayes.classifyNB(np.array(wordVector), rdfile2array('D://myfile/spider_output/p0'), rdfile2array('D://myfile/spider_output/p1'), 0.49)==1:
                f1.write(lines[line_index])
            else:
                f0.write(lines[line_index])


if __name__ == '__main__':
    main('D://myfile/bayestest/news_from_json','D://myfile/bayestest/sample_class1','D://myfile/bayestest/sample_class0')