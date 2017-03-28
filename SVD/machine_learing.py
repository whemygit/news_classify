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
# print U,Sigma,T

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

