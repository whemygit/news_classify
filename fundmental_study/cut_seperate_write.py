#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

import jieba
#去停分词——对原文内容去掉停用词后分词,结果每行一条新闻,分写到10个文件
def outstop_cut_toline(filename):
    with open(filename,"r") as fin:
        lines=fin.readlines()
        news_num = len(lines)
        one_file_num = news_num/10
        stop = [line.strip().decode('utf-8') for line in open("D://gitcode/mypython/jieba1/stopw.txt","r").readlines()]                             #如：r"D:\gitcode\mypython\jieba1\stopw.txt"
        outfile = 'D://myfile/pos/article_out_'
        index = 0
        file_num = 0
        for line in lines:
            index += 1
            line.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
            seg_list = jieba.cut(line, cut_all=False)
            seg_list_outstop='\x01'.join([w for w in seg_list if w not in stop])
            if index >= one_file_num:
                index = 0
                file_num += 1
                print outfile  + str(file_num)
                continue
            with open(outfile + str(file_num), 'a') as fw:
                fw.write(seg_list_outstop)
    return seg_list_outstop



