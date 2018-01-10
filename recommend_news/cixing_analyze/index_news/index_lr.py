#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,roc_auc_score,roc_curve
from sklearn.externals import joblib


reload(sys)
sys.setdefaultencoding("utf-8")
mpl.rcParams['font.sans-serif'] = [u'SimHei']  # 黑体 FangSong/KaiTi
mpl.rcParams['axes.unicode_minus'] = False

path='index_rec_classify_corpus_arti'

def load_data(path):
    data=pd.read_csv(path,delimiter='\x01')
    x=data[range(5)]
    y=pd.Categorical(data['flag']).codes
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7)
    return x_train,x_test,y_train,y_test

def model_lr_build():
    x_train, x_test, y_train, y_test = load_data(path=path)
    model=LogisticRegression()
    model.fit(x_train,y_train)
    y_test_hat=model.predict(x_test)
    accurate=accuracy_score(y_test,y_test_hat)
    precision=precision_score(y_test,y_test_hat)
    recall=recall_score(y_test,y_test_hat)
    predition = model.predict_proba(x_test)
    aucs = roc_auc_score(y_test, predition[:, 1:2])
    fpr, tpr, thresh = roc_curve(y_test, predition[:, 1:2])
    ctClass = [i * 0.01 for i in range(101)]
    print accurate,precision,recall,aucs
    # joblib.dump(model,'dt.m')
    return fpr, tpr, thresh,ctClass

def thresh_test(threshhold):
    x_train, x_test, y_train, y_test = load_data(path)
    fpr, tpr,thresh, ctClass=model_lr_build()
    idx=int(len(thresh)*threshhold)
    total_pts=len(y_test)
    P=sum(y_test)
    N=total_pts-P
    TP=tpr[idx]*P;FN=P-TP;FP=fpr[idx]*N;TN=N-FP
    print threshhold
    print 'threshhode value= ',thresh[idx]

    print 'TP= ', TP, 'FP= ', FP
    print 'FN= ', FN, 'TN= ', TN

    # print 'TP= ',TP/total_pts,'FP= ',FP/total_pts
    # print 'FN= ',FN/total_pts,'TN= ',TN/total_pts

    print 'TP= ',TP/P,'FP= ',FP/N
    print 'FN= ',FN/P,'TN= ',TN/N

    print 'precision= ',(TP+TN)/total_pts



def model_gbdt_build():
    x_train, x_test, y_train, y_test = load_data(path=path)
    model = GradientBoostingClassifier(subsample=0.5,learning_rate=0.05,max_depth=2,max_features=2,n_estimators=150)
    model.fit(x_train, y_train)
    num_esti=range(model.n_estimators)
    auc=[]
    prediction = model.staged_decision_function(x_test)
    # for i,y in enumerate(prediction):
    #     aucCalc=roc_auc_score(y_test,y)
    #     auc.append(aucCalc)
    #     print i,aucCalc,model.feature_importances_

    y_test_hat = model.predict(x_test)
    accurate=accuracy_score(y_test,y_test_hat)
    precision=precision_score(y_test,y_test_hat)
    recall=recall_score(y_test,y_test_hat)
    predition = model.predict_proba(x_test)
    aucs = roc_auc_score(y_test, predition[:, 1:2])
    print accurate,precision,recall,aucs



    # # joblib.dump(model,'dt.m')
    return num_esti,auc


if __name__ == '__main__':
    model_lr_build()
    # num_esti, auc=model_gbdt_build()
    # plt.plot(num_esti,auc,linewidth=2)
    # plt.xlabel('Number of trees in Ensemble')
    # plt.ylabel('auc')
    # plt.show()

    for threshhold in np.arange(0,1,0.05):
        thresh_test(threshhold=threshhold)