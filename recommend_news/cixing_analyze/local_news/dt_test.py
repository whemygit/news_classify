#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.externals import joblib

reload(sys)
sys.setdefaultencoding("utf-8")
mpl.rcParams['font.sans-serif'] = [u'SimHei']  # 黑体 FangSong/KaiTi
mpl.rcParams['axes.unicode_minus'] = False

# path='D://gitcode/news_classify/recommend_news/cixing_analyze/local_news/rec_classify_corpus'
# path='D://gitcode/news_classify/recommend_news/cixing_analyze/local_news/recommend_classify.csv'
# path='D://gitcode/news_classify/recommend_news/cixing_analyze/local_news/recommend_classify_machine_my'
path='local_recommend_classify_machine'
path='local_recommend_classify_arti'

def load_data(path):
    data=pd.read_csv(path,delimiter='\x01')
    data_feature='cnt_nper','cnt_ein','tit_nfirst','tit_cnt_inter','tit_vin'
    data_class='1','0'
    x=data[range(5)]
    y=pd.Categorical(data['flag']).codes
    x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7,random_state=1)
    return x_train,x_test,y_train,y_test,data_feature,data_class

def model_build():
    x_train, x_test, y_train, y_test, data_feature, data_class = load_data(path=path)
    model=DecisionTreeClassifier(criterion='entropy')
    model.fit(x_train,y_train)
    y_test_hat=model.predict(x_test)
    accurate=accuracy_score(y_test,y_test_hat)
    precision=precision_score(y_test,y_test_hat)
    recall=recall_score(y_test,y_test_hat)
    print accurate,precision,recall,model.feature_importances_
    joblib.dump(model,'dt.m')
    return model,y_test_hat,accurate


def pdfdot_save():
    model,y_test_hat, accurate = model_build()
    tree.export_graphviz(model,out_file='news.dot')


def depth_test():
    x_train, x_test, y_train, y_test, data_feature, data_class = load_data(path=path)
    depth=np.arange(1,8)
    acc_list=[]
    for d in depth:
        clf=DecisionTreeClassifier(criterion='entropy',max_depth=d)
        clf.fit(x_train,y_train)
        y_test_hat=clf.predict(x_test)
        accurate=accuracy_score(y_test,y_test_hat)
        precision = precision_score(y_test, y_test_hat)
        recall = recall_score(y_test, y_test_hat)
        print d,'accurate:',accurate, 'precision:',precision, 'recall:',recall, clf.feature_importances_
        acc_list.append(accurate)
    return depth,acc_list

def depth_accurate_plot():
    depth, acc_list=depth_test()
    plt.figure(facecolor='w')
    plt.plot(depth,acc_list,'ro-',lw=2)
    plt.xlabel(u'决策树深度',fontsize=15)
    plt.ylabel(u'分类正确率',fontsize=15)
    plt.title(u'决策树深度与过拟合',fontsize=17)
    plt.grid(True)
    plt.show()

def dt_predict():
    test_data=np.array([0.2,1,1,1,1]).reshape(1,-1)
    # print test_data
    model, y_test_hat, accurate = model_build()
    result=model.predict(test_data)
    print result

def rec_model(test_data,path):
    model_dt=joblib.load(path)
    test_data=np.array(test_data).reshape(1,-1)
    flag=model_dt.predict(test_data)
    print flag


if __name__ == '__main__':
    # x_train, x_test, y_train, y_test, data_feature, data_class=load_data(path=path)
    # print y_test
    # model_build()
    # print accurate
    # pdfdot_save()
    # depth_test()
    # depth_accurate_plot()
    test_data=[0.6,1,1,1,1]
    rec_model(test_data,'dt.m')