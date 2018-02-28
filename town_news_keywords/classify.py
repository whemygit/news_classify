#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import torndb
import operator

reload(sys)
sys.setdefaultencoding("utf-8")


class Classification():
    def __init__(self,filtered_kw_path,category_dict):
        self.filtered_kw_path=filtered_kw_path
        self.category_dict=category_dict
        self.classify_kw_dict=self.get_classify_kw()

    def get_classify_kw(self):
        classify_kw_dict={}
        for file in os.listdir(self.filtered_kw_path):
            with open(self.filtered_kw_path+'/'+file,'r') as fr:
                lines=fr.readlines()
                classify_kw_dict[self.category_dict[file]]=[line.split('\x01')[0] for line in lines]
        return classify_kw_dict

    def get_classify_data(self,mysql,p_type_id):
        db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                               user=mysql.get('user'),
                               password=mysql.get('password'), charset=mysql.get('charset'))
        cid_query_sql = '''SELECT id,title,content FROM t_all_news WHERE p_type_id='{}' limit 1000;'''.format(p_type_id)
        cid_dict = db.query(cid_query_sql)
        for i in cid_dict:
            yield i['id'], i['title'],i['content']

    def classify(self,content):
        count_dict={}
        classify_kw_dict=self.classify_kw_dict
        for k,v in classify_kw_dict.items():
            count=len([kw for kw in v if kw in content])
            count_dict[k]=count

        sorted_dict=sorted(count_dict.iteritems(),key=operator.itemgetter(1),reverse=True)
        return sorted_dict[0][0]







if __name__ == '__main__':
    categroy_dict = {
        'fazhankw': '1709301224421460293',
        'minshengkw': '1709301224421460296',
        'renshikw': '1709301224421460294'
    }
    mysql = {
        "host": "117.78.60.108",
        "port": "3306",
        "database": "cityparlor",
        "password": "123456",
        "user": "es",
        "charset": "utf8"
    }
    p_type_id_list = ['1709301224421460293','1709301224421460296','1709301224421460294']
    model=Classification(filtered_kw_path='keywd_500/keywords_filter',category_dict=categroy_dict)
    for p_type_id in p_type_id_list:
        counts=0
        for id,title,content in model.get_classify_data(mysql=mysql,p_type_id=p_type_id):
            if model.classify(content=content)==p_type_id:
                counts+=1
        print p_type_id,counts