#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from sklearn.externals import joblib
import numpy as np

reload(sys)
sys.setdefaultencoding("utf-8")

def best_model_use(test_data):
    test_data=np.array(test_data).reshape(1,-1)
    dtm_load=joblib.load('dt_all_best.m')
    print dtm_load.predict(test_data)


def best_rfmodel_use(test_data):
    test_data=np.array(test_data).reshape(1,-1)
    dtm_load=joblib.load('rf_all_best.m')
    print dtm_load.predict(test_data)

if __name__ == '__main__':
    test_data=[0.6,1,0,1,1]
    best_model_use(test_data=test_data)
    best_rfmodel_use(test_data=test_data)
