#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import xlrd
import torndb
import random
reload(sys)
sys.setdefaultencoding("utf-8")

def get_qiye_name():
    data=xlrd.open_workbook('qiye_name.xls')

    tabel= data.sheets()[0]
    nrows=tabel.nrows
    name_set=set()
    for i in range(nrows):
        # print tabel.row_values(i)[0]
        name_set.add(tabel.row_values(i)[0])

    print len(name_set)
    for name in name_set:
        if u'股份' in name:
            print name+':'+name.split(u'股份')[0]
        elif u'有限' in name:
            print name+':'+name.split(u'有限')[0]
        elif u'集团' in name:
            print name+':'+name.split(u'集团')[0]
        else:
            print name



def get_leader_name():
    data = xlrd.open_workbook('leader_name_jc.xls')
    tabel = data.sheets()[0]
    nrows = tabel.nrows

    name_dict={tabel.row_values(i)[1]:tabel.row_values(i)[0] for i in range(nrows)}

    return name_dict


def get_data(name_dict):
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

    with open('name_leader_qiyejc_data','w') as fw:
        for k,v in name_dict.items():
            print k,v
            fw.write(k+' '+v+'\n')
            query_sql = '''SELECT id,title FROM t_top_news where content LIKE '%%{s}%%' and content LIKE '%%{v}%%';'''.format(s=k,v=v)
            res_sql = db.query(query_sql)
            for i in res_sql:
                fw.write( i['id']+' '+i['title']+'\n')

def get_random_id(mysql,p_type_id):
    id_query_sql='''SELECT id FROM t_all_news WHERE p_type_id='{}';'''.format(p_type_id)
    db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                           user=mysql.get('user'),
                           password=mysql.get('password'), charset=mysql.get('charset'))
    id_list=[i.get('id') for i in db.query(id_query_sql)]
    random_sample_len = int(len(id_list)*0.1)
    print random_sample_len
    random_sample=random.sample(id_list,random_sample_len)
    return random_sample

if __name__ == '__main__':
    # name_dict=get_leader_name()
    # get_data(name_dict=name_dict)
    mysql = {
        "host": "117.78.60.108",
        "port": "3306",
        "database": "cityparlor",
        "password": "123456",
        "user": "es",
        "charset": "utf8"
    }


    #     for id,cname in get_categoryid_dict(mysql=mysql):
    #         print id,cname
    #         '''1709301224421460056 参政议政
    # 1709301224421460293 发展规划
    # 1709301224421460294 人事动态
    # 1709301224421460295 法律法规
    # 1709301224421460296 民生保障'''
    #     t_all_news包含：293,294,296
    #     for i in range(2,12):
    #         print i


    # cid_dict = {'1709301224421460293': 'fazhan', '1709301224421460294': 'renshi', '1709301224421460296': 'minsheng'}
    # for cid, cid_title in cid_dict.items():
    #     print cid, cid_title
    #     for i in range(2, 12):
    #         random_sample_id = get_random_id(mysql=mysql, p_type_id=cid)
    #         query_sql_list=[]
    #         query_sql_list = ['''SELECT id,title,content FROM t_all_news where id='{s}';'''.format(s=id) for id in random_sample_id]
    #         for i in query_sql_list:
    #             print i


    d=set()
    d.add('ddd')
    print d
    d.add('ccc')
    print d
    d.add('ddd')
    print d