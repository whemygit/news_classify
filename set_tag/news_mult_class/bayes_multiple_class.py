#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import jieba
from numpy import *
import numpy as np
import random
import os

reload(sys)
sys.setdefaultencoding("utf-8")


def createVocabList(dataSet):
    '''词库创建函数，用于利用输入的文本生成词库集，原则上包含所有在所有的文本中出现过的词（每个词出现一次的词集）
                   ，但实际处理工程中可添加去停用词等预处理
    输入：待训练的所有文本列表组成的列表，及LoadDataSet()输出的第一个参数
    输出：组成文本的所有词的词集，所有词组成的列表'''
    vocabSet=set([])
    for document in dataSet:
        vocabSet=vocabSet | set(document)
    return list(vocabSet)


def bagOfWords2Vec(vocabList,inputSet):
    '''向量转换函数：输入与seyOfWords2Vec完全相同，只不过在输出上有所变化，前者输出0和1组成的向量，0
    表示不出现，1表示出现，并没有出现次数的特征。而本函数为了体现每个词出现次数的特征，会输出对应词
    出现次数，一遇到出现该词，则在原来的基础上+1'''
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]+=1
        else:print "the word: %s is not in my Vocabulary!" %word
    return returnVec


#合成各类别新闻的先验概率向量
def classVec2classpList(classVec):
    '''类别标签向量转换为各类别比例函数：多类时，利用
    文本的类别类别计算各类所占概率，类别标签列表，如：classVec=[3,4,2,1,3,2]'''
    array_classVec=array(classVec)
    class_p_list=[]
    for i in unique(classVec):
        p=sum(array([w/i for w in array_classVec if w==i]))/float(len(classVec))
        # print 'the p of class+"i" is %f:' %p
        class_p_list.append(p)
        array_class_p_list=array(class_p_list)
    return array_class_p_list


def trainNBO(trainMatrix,trainCategory):
    '''训练算法函数：利用由上一步转换成的各文本词向量组成的词向量列表（该列表长度为文档个数，每个元素
                    的长度为词库长度的0,1词向量），以及各文本所属类型的向量，计算词库中各词属于指定文本
                    类别的条件概率向量和所有文档中类别1的文档出现的概率
    输入：词向量列表，文本所属类型向量
    输出：每个类别情况下词库中每个词出现的条件概率向量组成的矩阵，各类别文档出现的概率向量
'''
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    array_class_p_list=classVec2classpList(trainCategory)
    class_word_Num = np.ones((len(unique(trainCategory)),numWords))     #每个类别下词汇表中各词数量矩阵初始化值
    Denom=np.ones(len(unique(trainCategory)))+len(unique(trainCategory))-1   #每个类别下词总数向量初始化值
    pVect_array=np.zeros(shape(class_word_Num))
    for i in range(numTrainDocs):
        for j in unique(trainCategory):                          #唯一值列表
            if trainCategory[i] == j:
                class_word_Num[j-1]+=trainMatrix[i]
                Denom[j-1]+=sum(trainMatrix[i])
    for j in unique(trainCategory):
        pVect_array[j-1] =log(class_word_Num[j-1]/Denom[j-1])
    return pVect_array,array_class_p_list



def classifyNB(vec2Classify,pVect_array,array_class_p_list,Category):
    '''分类函数：计算后验概率，根据概率比较，判断待分类文本应属于概率较大的类
    输入：待分类的文本词向量，训练函数输出的结果,分类标签向量(必须为从1开始的连续序列！！！！！！！！)
    输出：待分类文本所属类别'''
    classify_p=np.zeros(len(array_class_p_list))
    for i in range(len(classify_p)):
        classify_p[i]=sum(vec2Classify*pVect_array[i])+log(array_class_p_list[i])
    classify_p=array(classify_p)
    # print 'classify_p:',classify_p
    for j in range(len(Category)):
        if classify_p[j] == classify_p.max():
           print classify_p
           print classify_p.std()
           classify_result=Category[j]
    return classify_result



def get_doc_list():
    """
    分别获取分词后文档矩阵，类别列表
    :input:多类别文本文档所在的路径
    output：doc_lisr,class_list
    """
    root = 'D://myfile/multclasscorpus'
    print root+'/'
    index = 1
    class_list = []
    doc_list = []
    for i in os.listdir(root):
        print len(os.listdir(root))
        print i
        # print type(i)
        with open(root+'/' + i, 'r') as fr, open("stopw.txt", "r") as frs:
            stop = [line.strip().decode('utf-8') for line in frs.readlines()]
            lines = fr.readlines()
            _class_list = [index] * len(lines)
            for line in lines:
                line=line.replace(r'\t', '').replace(r'\n', '').replace(r' ', '').replace(r'，', '').strip()
                seg_list = jieba.cut(line, cut_all=False)
                doc_list.append([w for w in seg_list if w not in stop])
        class_list.extend(_class_list)
        index += 1
    return doc_list,class_list

# #读取文件按首字母排序
# doc_label={'business':'1','chihe':'2','it':'3','learning':'4'}


def main():
    """
    运行主函数
    :return:
    """
    doc_list, class_list = get_doc_list()
    vocab_list = createVocabList(doc_list)
    # print vocab_list
    with open("vocablist","w") as vocfw:
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
    with open("pVect_array","w") as fw_pVect_array,open("array_class_p_list","w") as fw_pList:
        for doc_index in training_set:
            train_Mat.append(bagOfWords2Vec(vocab_list, doc_list[doc_index]))
            train_classes.append(class_list[doc_index])
        pVect_array, array_class_p_list=trainNBO(array(train_Mat), array(train_classes))

        for r in range(pVect_array.shape[0]):
            fw_pVect_array.write("\x01".join(str(i) for i in pVect_array[r,:])+'\n')

        fw_pList.write("\x01".join(str(i) for i in array_class_p_list))

        error_Count = 0
    # 测试阶段
    for doc_index in test_set:
        wordVector = bagOfWords2Vec(vocab_list, doc_list[doc_index])
        if classifyNB(array(wordVector), pVect_array, array_class_p_list, unique(class_list)) != class_list[doc_index]:
            error_Count += 1
    print "the error rate is:", float(error_Count) / len(test_set)

if __name__ == '__main__':
    main()
