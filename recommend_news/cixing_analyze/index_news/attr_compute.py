#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
def corpus_classify():
    with open('test_index_news','r') as fr,open('index_rec_classify_corpus','wb') as fw:
        lines=fr.readlines()
        write_flag=True
        for line in lines:
            line_dict={}
            line_list=line.split('\x01')
            line_dict['title'] = line_list[0]
            # 分类标志
            line_dict['flag']='1'
            # 标题以名词开头
            if 'n' in str(line_list[3][0]):
                line_dict['tit_nfirst']='1'
            else:
                line_dict['tit_nfirst']='0'
            # 标题含有动词
            if 'v' in line_list[3] or 'vn' in line_list[3]:
                line_dict['tit_vin']='1'
            else:
                line_dict['tit_vin'] ='0'
            # 关键字含有符号
            if 'e' in line_list[7]:
                line_dict['cnt_ein']='1'
            else:
                line_dict['cnt_ein']='0'
            #关键字名词百分比
            line_dict['cnt_nper']=line_list[8]
            # 标题和关键词交集不为空
            title_list=line_list[2].split(',')
            con_list=line_list[6].split(',')
            if list(set(title_list)&set(con_list)):
                line_dict['tit_cnt_inter']='1'
            else:
                line_dict['tit_cnt_inter'] ='0'


            if write_flag:
                print line_dict.keys()
                fw.write('\x01'.join(line_dict.keys())+'\n')

                write_flag = False
            else:
                print line_dict.values()
                fw.write('\x01'.join(line_dict.values())+'\n')

if __name__ == '__main__':
    corpus_classify()