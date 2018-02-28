#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb

reload(sys)
sys.setdefaultencoding("utf-8")

def write_kw_to_mysql(kw_data_file,mysql_param):
    db = torndb.Connection(host=mysql_param.get('host'), database=mysql_param.get('database'),
                           user=mysql_param.get('user'),
                           password=mysql_param.get('password'), charset=mysql_param.get('charset'))
    write_sql = '''INSERT INTO company_kw (company_name,company_abb) VALUES (%s,%s)'''
    with open(kw_data_file,'r') as fr:
        name_abb_dict={line.split(':')[0]:line.split(':')[1].strip() for line in fr.readlines()}
        for k,v in name_abb_dict.items():
            db.insert(write_sql,k,v)
            print k,v



if __name__ == '__main__':
    mysql = {
        "host": "117.78.60.108",
        "port": "3306",
        "database": "cityparlor",
        "password": "123456",
        "user": "es",
        "charset": "utf8"
    }
    kw_data_file='name_dict'

    write_kw_to_mysql(kw_data_file=kw_data_file,mysql_param=mysql)