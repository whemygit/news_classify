#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,roc_auc_score,roc_curve
from sklearn.externals import joblib


reload(sys)
sys.setdefaultencoding("utf-8")
mpl.rcParams['font.sans-serif'] = [u'SimHei']  # 黑体 FangSong/KaiTi
mpl.rcParams['axes.unicode_minus'] = False

# path='index_rec_classify_corpus_arti'
path='classify_corpus_correct_0'


def load_data(path):
    data=pd.read_csv(path,delimiter='\x01')
    x=data[range(5)]
    y=pd.Categorical(data['flag']).codes
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7)
    return x_train,x_test,y_train,y_test

def train_model():
    x_train, x_test, y_train, y_test=load_data(path)
    tree_num=np.arange(5,100,5)
    acc_list=[]

    for num in tree_num:
        clf=RandomForestClassifier(n_estimators=num,max_features=2)
        clf.fit(x_train,y_train)
        y_test_hat=clf.predict(x_test)
        acc=accuracy_score(y_test,y_test_hat)
        precision=precision_score(y_test,y_test_hat)
        recall=recall_score(y_test,y_test_hat)
        acc_list.append(acc)
        predition=clf.predict_proba(x_test)
        print num,acc,precision,recall,clf.n_features_,clf.feature_importances_
            # print num,type(predition),predition[:,1:2]
            # print clf.classes_
        # print clf.feature_importances_
    return tree_num,acc_list


def simple_train_model():
    x_train, x_test, y_train, y_test=load_data(path)
    clf=RandomForestClassifier(n_estimators=10,max_depth=4,max_features=2)
    clf.fit(x_train,y_train)
    y_test_hat=clf.predict(x_test)
    # y_test_prob=clf.predict_proba(x_test)
    # print y_test_prob
    acc=accuracy_score(y_test,y_test_hat)
    precision=precision_score(y_test,y_test_hat)
    recall=recall_score(y_test,y_test_hat)
    # joblib.dump(clf,'rf_all_best.m')
    joblib.dump(clf, 'rec_model.m')


    fp_list=[1 if j==0 and y_test_hat[i]==1 else 0 for i,j in enumerate(y_test)]

    test_error=x_test[np.array(fp_list)==1]
    error_index=test_error.index
    print acc,precision,recall,clf.n_features_,clf.feature_importances_
    return error_index



def get_error_datas(path):
    data = pd.read_csv(path, delimiter='\x01')
    # print data
    error_index=simple_train_model()
    with open('error_title','wb') as fw:
        for i in error_index:
            print data['title'][i]
            fw.write(str(i)+'\x01'+data['title'][i]+'\n')


def get_negative_data(path):
    data = pd.read_csv(path, delimiter='\x01')
    print data['title'][data['flag']==0]



def tree_num_accurate_plot():
    tree_num, acc_list=train_model()
    plt.figure(facecolor='w')
    plt.plot(tree_num,acc_list,'ro-',lw=2)
    plt.xlabel(u'决策树个数',fontsize=15)
    plt.ylabel(u'分类正确率',fontsize=15)
    plt.title(u'决策树个数与正确率',fontsize=17)
    plt.grid(True)
    plt.show()




def roc_curve_train():
    x_train, x_test, y_train, y_test=load_data(path)
    tree_num=np.arange(5,100,5)
    auc_list=[]
    for num in tree_num:
        clf=RandomForestClassifier(n_estimators=num,max_features=2,max_depth=4)
        clf.fit(x_train,y_train)
        y_test_hat=clf.predict(x_test)
        acc=accuracy_score(y_test,y_test_hat)
        precision=precision_score(y_test,y_test_hat)
        recall=recall_score(y_test,y_test_hat)
        predition=clf.predict_proba(x_test)
        aucs=roc_auc_score(y_test,predition[:,1:2])
        auc_list.append(aucs)
        # print num,pair,acc,precision,recall,clf.n_features_,clf.feature_importances_
        # print num,type(predition),predition[:,1:2]
        print num,aucs
    # print clf.feature_importances_
    return tree_num,auc_list


def best_roc_train():
    x_train, x_test, y_train, y_test=load_data(path)
    clf=RandomForestClassifier(n_estimators=10,max_depth=4,max_features=2)
    clf.fit(x_train,y_train)
    predition=clf.predict_proba(x_test)
    fpr,tpr,thresh=roc_curve(y_test,predition[:,1:2])
    ctClass=[i*0.01 for i in range(101)]
    # print type(fpr),fpr.shape,fpr
    # print type(tpr),tpr.shape,tpr
    # print type(thresh),thresh.shape,thresh
    return fpr,tpr,thresh,ctClass

def thresh_test(threshhold):
    x_train, x_test, y_train, y_test = load_data(path)
    fpr, tpr,thresh, ctClass=best_roc_train()
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


def model_data_correct(path):
    data = pd.read_csv(path, delimiter='\x01')
    # print data
    error_index = simple_train_model()
    for i in error_index:

        data['flag'][i]=1
    data.to_csv('classify_corpus_correct_0',sep='\x01',header=True,index=False)


if __name__ == '__main__':
    # x,y=load_data(path)
    # train_model()
    # simple_train_model()
    # 69棵树最高
    # tree_num_accurate_plot()
    # best_train_model_save_use()

    # tree_num, auc_list=roc_curve_train()
    # plt.plot(tree_num,auc_list)
    # plt.show()

    # fpr, tpr,thresh, ctClass=best_roc_train()
    # plt.plot(fpr,tpr,linewidth=2)
    # plt.plot(ctClass,ctClass,linestyle=':')
    # plt.xlabel('False Positive Rate')
    # plt.ylabel('True Positive Rate')
    # plt.show()

    # for threshhold in np.arange(0,1,0.05):
    #     thresh_test(threshhold=threshhold)

    get_error_datas(path=path)

    # get_negative_data(path=path)

    # model_data_correct(path='classify_corpus_correct_0')
