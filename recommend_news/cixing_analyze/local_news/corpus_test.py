#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb
from snownlp import SnowNLP

reload(sys)
sys.setdefaultencoding("utf-8")

mysql = {
    "host": "117.78.60.108",
    "port": "3306",
    "database": "cityparlor",
    "password": "123456",
    "user": "es",
    "charset": "utf8"
}

db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))

def get_source_list():
    rec_source_sql='''SELECT source FROM t_source_local_news WHERE rec_flag='1';'''
    rec_res=db.query(rec_source_sql)
    rec_source_list=[]
    for i in rec_res:
        rec_source_list.append(i.get('source'))
    return rec_source_list

def corpus_classify():
    rec_source_list=get_source_list()
    with open('test_local_news','r') as fr,open('rec_classify_corpus','wb') as fw:
        lines=fr.readlines()
        write_flag=True
        for line in lines:
            line_dict={}
            line_list=line.split('\x01')
            line_dict['title'] = line_list[0]
            # 分类标志
            if line_list[1] in rec_source_list:
                line_dict['flag']='1'
            else:
                line_dict['flag']='0'
            # 标题以名词开头
            if str(line_list[3][0]).startswith('n'):
                line_dict['tit_nfirst']='1'
            else:
                line_dict['tit_nfirst']='1'
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