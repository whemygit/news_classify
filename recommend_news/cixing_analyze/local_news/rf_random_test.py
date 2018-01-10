#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score
from sklearn.externals import joblib
from sklearn.externals.six import StringIO


reload(sys)
sys.setdefaultencoding("utf-8")
mpl.rcParams['font.sans-serif'] = [u'SimHei']  # 黑体 FangSong/KaiTi
mpl.rcParams['axes.unicode_minus'] = False

# path='D://gitcode/news_classify/recommend_news/cixing_analyze/local_news/rec_classify_corpus'
# path='D://gitcode/news_classify/recommend_news/cixing_analyze/local_news/recommend_classify.csv'
path='D://gitcode/news_classify/recommend_news/cixing_analyze/local_news/recommend_classify_machine_my'
def load_data(path):
    data=pd.read_csv(path,delimiter='\x01')
    x=data[range(5)]
    y=pd.Categorical(data['flag']).codes
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7)
    return x_train,x_test,y_train,y_test

def train_model():
    x_train, x_test, y_train, y_test=load_data(path)
    attr_index_list=[]
    ncols= x_train.shape[1]
    nAttr=3
    idxAtrr=random.sample(range(ncols),nAttr)
    idxAtrr.sort()
    attr_index_list.append(idxAtrr)
    print attr_index_list


    acc_list=[]
    clf=RandomForestClassifier(n_estimators=10,min_samples_split=100)
    clf.fit(x_train[idxAtrr],y_train)
    y_test_hat=clf.predict(x_test[idxAtrr])
    acc=accuracy_score(y_test,y_test_hat)
    precision=precision_score(y_test,y_test_hat)
    recall=recall_score(y_test,y_test_hat)
    acc_list.append(acc)
    print idxAtrr,acc,precision,recall,clf.n_features_,clf.feature_importances_
        # print clf.feature_importances_
    # return tree_num,acc_list

def tree_num_accurate_plot():
    tree_num, acc_list=train_model()
    plt.figure(facecolor='w')
    plt.plot(tree_num,acc_list,'ro-',lw=2)
    plt.xlabel(u'决策树个数',fontsize=15)
    plt.ylabel(u'分类正确率',fontsize=15)
    plt.title(u'决策树个数与正确率',fontsize=17)
    plt.grid(True)
    plt.show()

def best_train_model_save_use():
    x,y=load_data(path)
    clf=RandomForestClassifier(n_estimators=69,min_samples_leaf=10,criterion='entropy')
    clf.fit(x,y)
    print clf.oob_score_
    test_data = np.array([0.2, 1, 1, 1, 1]).reshape(1,-1)
    print clf.predict(test_data)
    joblib.dump(clf,filename='rf.m')
    rf_load=joblib.load('rf.m')
    print rf_load.predict(test_data)



if __name__ == '__main__':
    # x,y=load_data(path)
    train_model()
    # 69棵树最高
    # tree_num_accurate_plot()
    # best_train_model_save_use()
