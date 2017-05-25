#!/usr/bin/env python
# -- coding: utf-8 --
from numpy import *

import sys

reload(sys)
sys.setdefaultencoding("utf-8")



def createVocabList(dataSet):
    """
    创建一个包含在所有文档中出现的不重复词的列表
    :param dataSet:
    :return:
    """
    vocabSet = set([])  # 创建一个空集 返回一个不重复的词表
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # 创建两个集合的并集
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    """
    :param vocabList: 词汇表
    :param inputSet: 某个文档
    :return: 返回文档向量，向量的每一个元素为0或1，分表表示词汇表中的单词在输入文档中是否出现
    """
    returnVec = [0] * len(vocabList)  # 创建一个与输入等长的所有元素都为0的向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word : %s is not in my Vocabulary!" % word
    return returnVec


def bagOfWords2VecMN(vocabList, inputSet):
    """
    贝叶斯词袋模型
    函数与上函数几乎完全相同，唯一不同的是每当遇到一个单词时，会增加词向量中的对应值,而不是只将对应的数值设置为1
    :param vocabList:
    :param inputSet:
    :return:
    """
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    """
    :param trainMatrix: 文档矩阵
    :param trainCategory: 每篇文档类别标签所构成的向量
    :return:
    """
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # 初始化概率 初始化  很关键。。 长度不变！不变！！不变！！！ 兄弟很关键啊！~
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        # 向量相加
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0
