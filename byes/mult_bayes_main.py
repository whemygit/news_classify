#!/usr/bin/env python
# -- coding: utf-8 --
import jieba
import bayes
import bayes_multiple_class
import random
from numpy import *

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def outstop_cut_toline(filename, flag):
    """
    返回分词后的新闻矩阵
    :param filename: 输入文件路径
    :param flag: 输入新闻标记， True 为负面新闻 False 为正面新闻
    :return:
    """
    with open(filename, "r") as fr, open("D://myfile/stopw.txt", "r") as frs:
        lines = fr.readlines()
        stop = [line.strip().decode('utf-8') for line in frs.readlines()]
        seg_list_outstop = []
        for line in lines:
            line.replace(r'\t', '').replace(r'\n', '').replace(r' ', '').replace(r'，', '')
            seg_list = jieba.cut(line, cut_all=False)
            seg_list_outstop.append([w for w in seg_list if w not in stop])
        if flag:
            classList = [1] * len(lines)
        else:
            classList = [0] * len(lines)
        return seg_list_outstop, classList


def get_doc_list():
    """
    分别获取矩阵，类别，词的链表
    :return:
    """
    file_1 = 'D://myfile/spider_output/article_neg.neg'    #类别1
    file_2 = 'D://myfile/spider_output/article_pos.pos'

    # 分别返回正面和负面新闻的分词结果以及类别
    seg_list_neg, class_list_neg = outstop_cut_toline(file_1, 1)  # 负面
    seg_list_pos, class_list_pos = outstop_cut_toline(file_2, 2)  # 正面

    # 汇总返回结果
    doc_list = seg_list_neg + seg_list_pos  # 矩阵
    class_list = class_list_neg + class_list_pos  # 类别
    full_list = []  # 所有词
    for doc in doc_list:
        for d in doc:
            full_list += d
    return doc_list, class_list, full_list


def main():
    """
    运行主函数
    :return:
    """
    doc_list, class_list, full_list = get_doc_list()
    vocab_list = bayes_multiple_class.createVocabList(doc_list)
    # print vocab_list
    with open("D://myfile/spider_output/vocablist","w") as vocfw:
        vocfw.write("\x01".join(vocab_list))
    training_set = range(len(doc_list))
    test_set = []
    # 随机筛选100条新闻作为测试集，留下训练集
    for i in range(100):
        rand_index = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_index])
        del (training_set[rand_index])
    train_Mat = []
    train_classes = []
    # 训练阶段
    with open("D://myfile/spider_output/pVect_array","w") as fw_pVect_array,open("D://myfile/spider_output/array_class_p_list","w") as fw_pList:
        for doc_index in training_set:
            train_Mat.append(bayes_multiple_class.bagOfWords2Vec(vocab_list, doc_list[doc_index]))
            train_classes.append(class_list[doc_index])
        pVect_array, array_class_p_list=bayes_multiple_class.trainNBO(array(train_Mat), array(train_classes))

        fw_pVect_array.write("\x01".join(str(i) for i in pVect_array,))

        fw_pList.write("\x01".join(str(i) for i in array_class_p_list))

        error_Count = 0
    # 测试阶段
    for doc_index in test_set:
        wordVector = bayes_multiple_class.bagOfWords2Vec(vocab_list, doc_list[doc_index])
        if bayes_multiple_class.classifyNB(array(wordVector), pVect_array, array_class_p_list, unique(class_list)) != class_list[doc_index]:
            error_Count += 1
    print "the error rate is:", float(error_Count) / len(test_set)


if __name__ == '__main__':
    main()


