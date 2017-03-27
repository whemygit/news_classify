#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass


#csv
def csv_read(infilename):
    '''读取可以解析为CSV格式的文件（每一列用逗号分开，每一行用换行符分开）
    输入：将要读取的文件的文件名
    输出：列表，元素是各行组成的列表，元素是行内以分隔符分割的元素'''
    import csv
    with open(infilename,'r') as fin:
        cin=csv.reader(fin)
        result=[row for row in cin]
        return result                     #以每行组成的列表（内部以分隔符分开）为元素组成的大列表结构，如：[['Doctor', 'No'], ['Rosa', 'Klebb'], ['Mister', 'Big'], ['Auric', 'Goldfinger'], ['Ernst', 'Blofeld']]


# a=csv_read('./csvin.txt')
# print a

def csv_write(infilename,c_write):
    '''csv格式文本写入文件：将形如[['Doctor', 'No'], ['Rosa', 'Klebb']]
    格式的数据结构按照一个列表元素一行的形式写入文件
    输入：要写入的文件的文件名，将要写入的列表
    输出；文件'''
    import csv
    with open(infilename,'w') as fout:
        csvout=csv.writer(fout)
        csvout.writerows(c_write)

# csv_write('./csvout.txt',a)

