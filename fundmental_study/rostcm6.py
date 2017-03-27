#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass
import pandas as pd
inputfile="D:/emotion_analyse/news_from_json_f.txt"

data1=pd.read_csv(inputfile,encoding="utf-8",header=None)
print data1[0]