#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass


from numpy import *
import numpy as np

def LoadDataSet():
    '''数据加载函数，主要用于演示样例所用，说明建立模型所需要的基础数据格式
    输入：文本列表组成的列表，各文本所属类型的向量，两类别用0,1表示
    输出:同输入'''
    postingList=[['my','dog','has','flea',
                  'problems','help','please'],
                 ['maybe','not','take','him',
                  'to','dog','park','stupid'],
                 ['my','dalmation','is','so','cute',
                  'I','love','him'],
                 ['stop','posting','stupid','worthless','garbage'],
                 ['mr','licks','ate','my','steak','how','to','stop','him'],
                 ['quit','buying','worthless','dog','food','stupid']]
    classVec=[1,3,2,3,1,4]
    return postingList,classVec


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
           classify_result=Category[j]
    return classify_result


def testingNB():
    '''测试函数'''
    listOPosts,listClasses=LoadDataSet()
    myVocabList=createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(bagOfWords2Vec(myVocabList,postinDoc))
        pVect_array, array_class_p_list=trainNBO(array(trainMat),array(listClasses))
    testEntry=['quit','buying','worthless','dog','food','stupid']
    thisDoc=array(bagOfWords2Vec(myVocabList,testEntry))
    print testEntry,'classified as :',classifyNB(thisDoc,pVect_array, array_class_p_list,unique(listClasses))

# testingNB()

# def textParse(bigString):
#     import re
#     listOfTokens=re.split(r'w*',bigString)
#     return [tok.lower() for tok in listOfTokens if len(tok)>2]
#
# def spamTest():
#     docList=[];classList=[];fullText=[]
#     for i in range(1,26):                          #读取样本
#         wordList=textParse(open('aa%d'%i).read())
#         docList.append(wordList)
#         fullText.extend(wordList)
#         classList.append(1)
#         wordList = textParse(open('aa%d'%i).read())
#         docList.append(wordList)
#         fullText.extend(wordList)
#         classList.append(0)
#     vocabList=createVocabList(docList)              #生成词库
#     trainingSet=range(50);testSet=[]                #训练集和测试集序号
#     for i in range(10):
#         randIndex=int(random.uniform(0,len(trainingSet)))     #随机序列号
#         testSet.append(trainingSet[randIndex])                #随机序列加入测试集
#         del(trainingSet[randIndex])                           #同时将测试集中对应序列号删除
#     trainMat=[];trainClasses=[]
#     for docIndex in trainingSet:                              #根据对应序列生成训练集及类别向量
#         trainMat.append(bagOfWords2Vec(vocabList,docList[docIndex]))
#         trainClasses.append(classList[docIndex])
#     p0V,p1V,pSpam=trainNBO(trainMat,trainClasses)              #训练模型
#     errorCount=0
#     for docIndex in testSet:                                   #逐条测试测试集，测试结果与实际不符中错误数+1
#         wordVector=bagOfWords2Vec(vocabList,docList[docIndex])
#         if classifyNB(array(wordVector),p0V,p1V,pSpam)!=classList[docIndex]:
#             errorCount+=1
#     print 'the error rate is:',float(errorCount)/len(testSet)   #输出错误率