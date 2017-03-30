#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass
#####################################################################################
from numpy import *
U,Sigma,T=linalg.svd([[1,1],[7,7]])
# print mat([[1,1],[7,7]])
# print mat([[1,1],[7,7]]).T       矩阵转置
# print mat([[1,1],[7,7]]).I
#矩阵分解
def loadExData():
    return [[1,1,1,0,0],
            [2,2,2,0,0],
            [1,1,1,0,0],
            [5,5,5,0,0],
            [1,1,0,2,2],
            [0,0,0,3,3],
            [0,0,0,1,1]]

Data=loadExData()
U,Sigma,VT=linalg.svd(Data)
# print Sigma
#
# Sig3=mat([[Sigma[0],0,0],[0,Sigma[1],0],[0,0,Sigma[2]]])
# print Sig3
# print Sig3[0:2,:]
#
# print U[:,:3]*Sig3*VT[:3,:]


##############################################################################
#相似度计算
from numpy import *
from numpy import linalg as la

def ecludSim(inA,inB):                                 #欧氏距离相似性
    return 1.0/(1.0+la.norm(inA-inB))

def pearsSim(inA,inB):                                  #皮尔逊相关相似性
    if len(inA)<3:return 1.0
    return 0.5+0.5*corrcoef(inA,inB,rowvar=0)[0][1]

def cosSim(inA,inB):                                    #余弦相似性
    num=float(inA.T*inB)
    denom=la.norm(inA)*la.norm(inB)
    return 0.5+0.5*(num/denom)

# myMat=mat(loadExData())
# print ecludSim(myMat[:,0],myMat[:,4])
# print ecludSim(myMat[:,0],myMat[:,0])
# print cosSim(myMat[:,0],myMat[:,4])
# print cosSim(myMat[:,0],myMat[:,0])
# print pearsSim(myMat[:,0],myMat[:,4])
# print pearsSim(myMat[:,0],myMat[:,0])

def standEst(dataMat,user,simMeas,item):
    n=shape(dataMat)[1]
    simTotal=0.0;ratSimTotal=0.0
    for j in range(n):
        userRating=dataMat[user,j]
        if userRating==0:continue                                       #查找该用户没有评价过的物品，没评价则跳过该物品，因此需要遍历的是user没有评价item的同时评价过item[j]的item，便于参考计算评价
        overLap=nonzero(logical_and(dataMat[:,item].A>0,
                                    dataMat[:,j].A>0))[0]                #寻找两列中同时不为0的元素所在行，即同时被除user之外的其他相同用户评价过的两个物品，以便两者的计算相似性
        if len(overLap)==0:similarity=0
        else:similarity=simMeas(dataMat[overLap,item],
                                dataMat[overLap,j])
        # print 'the %d and %d similarity is: %f' %(item,j,similarity)
        simTotal+=similarity                                             #待分析的物品跟所有可计算相似性的物品的相似度累计值
        ratSimTotal+=similarity*userRating                               #相似度与该用户给出的相似物品评价的乘积，便于根据相似度计算预估评分
    if simTotal==0:return 0
    else:return ratSimTotal/simTotal                                    #预估评分即user对所有相似物品评分的相似度加权平均值

# dataMat=mat(loadExData())
# print dataMat
# # print dataMat[:,3].A>0
# # print dataMat[:,3]>0
# print logical_and(dataMat[:,2].A>0,dataMat[:,3].A>0)
# print nonzero(logical_and(dataMat[:,2].A>0,dataMat[:,3].A>0))
# print nonzero(logical_and(dataMat[:,2].A>0,dataMat[:,3].A>0))[0]

def recommend(dataMat,user,N=3,simMeas=cosSim,estMethod=standEst):
    unratedItems=nonzero(dataMat[user,:].A==0)[1]                                    #找出user行中元素为0所在的列
    if len(unratedItems)==0:return 'you rated everyting'
    itemScores=[]
    for item in unratedItems:                                                       #遍历user未进行评价的物品
        estimatedScore=estMethod(dataMat,user,simMeas,item)                          #调用estMethod进行评级，默认为standEst方法
        itemScores.append((item,estimatedScore))                                     #物品及预估评分
    return sorted(itemScores,key=lambda jj:jj[1],reverse=True)[:N]                 #从大到小排序并返回前N个

# dataMat=mat(loadExData())
# print dataMat
# print dataMat[1,:].A==0
# print nonzero(dataMat[1,:].A==0)
# print nonzero(dataMat[1,:].A==0)[1]

myMat=mat(loadExData())
# # print myMat
# myMat[0,1]=myMat[0,0]=myMat[1,0]=myMat[2,0]=4
# myMat[3,3]=2
# print myMat
#
# print recommend(myMat,2)
# print recommend(myMat,2,simMeas=ecludSim)
# print recommend(myMat,5)

#利用SVD提高推荐的效果
def loadExData2():
    return [[2,0,0,4,4,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,5],
            [0,0,0,0,0,0,0,1,0,4,0],
            [3,3,4,0,3,0,0,2,2,0,0],
            [5,0,5,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,5,0,0,5,0],
            [4,0,4,0,0,0,0,0,0,0,5],
            [0,0,0,0,0,4,0,0,0,0,4],
            [0,0,0,0,0,0,5,0,0,5,0],
            [0,0,0,3,0,0,0,0,4,5,0],
            [1,1,2,1,1,2,1,0,4,5,0]]
from numpy import linalg as la
dataMat=mat(loadExData2())
U,Sigma,VT=la.svd(dataMat)
# print Sigma
# print U
# print U.T
# print eye(4)
# print eye(4)*Sigma[:4]



def svdEst(dataMat,user,simMeas,item):
    n=shape(dataMat)[1]
    # print '1111111111'
    # print shape(dataMat)                             #(11L, 11L)
    simTotal=0.0;ratSimTotal=0.0
    U, Sigma, VT = la.svd(dataMat)
    Sig4=mat(eye(4)*Sigma[:4])
    xformedItems=dataMat.T*U[:,:4]*Sig4.I
    # print '22222222222'
    # print shape(xformedItems)                         #(11L, 4L)
    for j in range(n):
        userRating=dataMat[user,j]
        if userRating==0 or j==item:continue
        similarity=simMeas(xformedItems[item,:].T,
                           xformedItems[j,:].T)
        # print 'the %d and %d similarity is: %f' %(item,j,similarity)
        simTotal+=similarity
        ratSimTotal+=similarity*userRating
    if simTotal==0:return 0
    else:return ratSimTotal/simTotal

# myMat=mat(loadExData2())
# # print recommend(myMat,1,N=5,estMethod=svdEst)
# # print recommend(myMat,1,N=5,estMethod=standEst)
# print recommend(myMat,9,N=5,estMethod=svdEst)

