#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

from numpy import *
U,Sigma,T=linalg.svd([[1,1],[7,7]])
# print U,Sigma,T


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
print Sigma

Sig3=mat([[Sigma[0],0,0],[0,Sigma[1],0],[0,0,Sigma[2]]])
print Sig3
print Sig3[0:2,:]

print U[:,:3]*Sig3*VT[:3,:]