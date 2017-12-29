#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

def load_data():
    with open('D:/gitcode/news_classify/recommend_news/cixing_analyze/local_news/test_local_news', 'r') as fr:
        lines = fr.readlines()
        for line in lines:
            line_list = line.split('\x01')
            yield line_list


def title_n_and_v():
    with open('D:/gitcode/news_classify/recommend_news/cixing_analyze/local_news/recomend_titlenv','w') as fw1,open('D:/gitcode/news_classify/recommend_news/cixing_analyze/local_news/urecomend_titlenv','w') as fw2:
        for line_list in load_data():
            if str(line_list[3][0]).startswith('n') and float(line_list[5])>0:
                fw1.write(str(line_list[0])+'\x01'+str(line_list[1])+'\n')
            else:
                fw2.write(str(line_list[0])+'\x01'+str(line_list[1])+'\n')

def con_n_and_title_v():
    with open('D:/gitcode/news_classify/recommend_news/cixing_analyze/local_news/recomend_conn_titlev','w') as fw1,open('D:/gitcode/news_classify/recommend_news/cixing_analyze/local_news/urecomend_conn_titlev','w') as fw2:
        for line_list in load_data():
            if 'v' in line_list[3] and float(line_list[8])>0.6:
                fw1.write(str(line_list[0])+'\x01'+str(line_list[1])+'\n')
            else:
                fw2.write(str(line_list[0])+'\x01'+str(line_list[1])+'\n')


if __name__ == '__main__':
    title_n_and_v()
    # con_n_and_title_v()