#!/usr/bin/env python
# -- coding: utf-8 --
import os
import jieba
import bayes
import bayes_multiple_class
import random
from numpy import *

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def outstop_cut_toline(filename):
    """
    返回分词后的新闻矩阵
    :param filename: 输入文件路径
    """
    with open(filename, "r") as fr, open("D://myfile/stopw.txt", "r") as frs:
        lines = fr.readlines()
        stop = [line.strip().decode('utf-8') for line in frs.readlines()]
        seg_list_outstop = []
        for line in lines:
            line.replace(r'\t', '').replace(r'\n', '').replace(r' ', '').replace(r'，', '')
            seg_list = jieba.cut(line, cut_all=False)
            seg_list_outstop.append([w for w in seg_list if w not in stop])
        return seg_list_outstop


def get_doc_list():
    """
    分别获取分词后文档矩阵，类别列表
    :input:多类别文本文档所在的路径
    output：doc_lisr,class_list
    """
    root = 'D://myfile/test'
    print root+'/'
    index = 1
    class_list = []
    doc_list = []
    for i in os.listdir(root):
        print len(os.listdir(root))
        print i
        print type(i)
        with open(root+'/' + i, 'r') as fr, open("D://myfile/stopw.txt", "r") as frs:
            stop = [line.strip().decode('utf-8') for line in frs.readlines()]
            lines = fr.readlines()
            _class_list = [index] * len(lines)
            for line in lines:
                line.replace(r'\t', '').replace(r'\n', '').replace(r' ', '').replace(r'，', '')
                seg_list = jieba.cut(line, cut_all=False)
                doc_list.append([w for w in seg_list if w not in stop])
        class_list.extend(_class_list)
        index += 1
    return doc_list,class_list

# root='D://myfile/test'
# index=1
# class_list=[]
# doc_list=[]
# for i in os.listdir(root):
#     print len(os.listdir(root))
#     print i
#     print type(i)
#     with open(root+'/'+i,'r') as fr,open("D://myfile/stopw.txt", "r") as frs:
#         stop = [line.strip().decode('utf-8') for line in frs.readlines()]
#         lines=fr.readlines()
#         _class_list=[index]*len(lines)
#         for line in lines:
#             line.replace(r'\t', '').replace(r'\n', '').replace(r' ', '').replace(r'，', '')
#             seg_list = jieba.cut(line, cut_all=False)
#             doc_list.append([w for w in seg_list if w not in stop])
#     class_list.extend(_class_list)
#     index+=1
# print doc_list
# print class_list
# print len(doc_list)



def main():
    """
    运行主函数
    :return:
    """
    doc_list, class_list = get_doc_list()
    vocab_list = bayes_multiple_class.createVocabList(doc_list)
    # print vocab_list
    with open("D://myfile/mult_bayes/vocablist","w") as vocfw:
        vocfw.write("\x01".join(vocab_list))
    training_set = range(len(doc_list))
    test_set = []
    # 随机筛选10%条新闻作为测试集，留下训练集
    for i in range(int(len(doc_list)*0.1)):
        rand_index = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_index])
        del (training_set[rand_index])
    train_Mat = []
    train_classes = []
    # 训练阶段
    with open("D://myfile/mult_bayes/pVect_array","w") as fw_pVect_array,open("D://myfile/mult_bayes/array_class_p_list","w") as fw_pList:
        for doc_index in training_set:
            train_Mat.append(bayes_multiple_class.bagOfWords2Vec(vocab_list, doc_list[doc_index]))
            train_classes.append(class_list[doc_index])
        pVect_array, array_class_p_list=bayes_multiple_class.trainNBO(array(train_Mat), array(train_classes))

        for r in range(pVect_array.shape[0]):
            fw_pVect_array.write("\x01".join(str(i) for i in pVect_array[r,:])+'\n')

        fw_pList.write("\x01".join(str(i) for i in array_class_p_list))

        error_Count = 0
    # 测试阶段
    for doc_index in test_set:
        wordVector = bayes_multiple_class.bagOfWords2Vec(vocab_list, doc_list[doc_index])
        if bayes_multiple_class.classifyNB(array(wordVector), pVect_array, array_class_p_list, unique(class_list)) != class_list[doc_index]:
            error_Count += 1
    print "the error rate is:", float(error_Count) / len(test_set)


if __name__ == '__main__':
    doc_list, class_list = get_doc_list()
    print class_list
    print len(doc_list)


