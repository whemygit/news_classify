#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import xlrd
import json
import torndb

reload(sys)
sys.setdefaultencoding("utf-8")

class NewsBasedCompany():
    def __init__(self,kwinfo_data_fp):
        self.kwinfo_data_fp=kwinfo_data_fp

    def get_leader_kw_xls(self):
        data = xlrd.open_workbook(self.kwinfo_data_fp)
        tabel = data.sheets()[0]
        nrows = tabel.nrows
        com_leader_jc_dict = {tabel.row_values(i)[0]: {tabel.row_values(i)[1]:tabel.row_values(i)[2].split(',')} for i in range(nrows)}
        return com_leader_jc_dict

    def get_leader_news_from_sql(self,mysql_params):
        if self.kwinfo_data_fp.endswith('xls'):
            com_leader_jc_dict = self.get_leader_kw_xls()
        else:
            raise ValueError('Cannot get com_leader_jc_dict from {}'.format(self.kwinfo_data_fp))

        mysql=mysql_params
        db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                               user=mysql.get('user'),
                               password=mysql.get('password'), charset=mysql.get('charset'))
        for k,v in com_leader_jc_dict.items():
            print k,v.keys()[0]
            query_sql_list = ['''SELECT id,title FROM t_top_news where content LIKE '%%{s}%%' and content LIKE '%%{v}%%';'''.format(s=v.keys()[0],v=kw) for kw in v.values()[0]]
            for query_sql in query_sql_list:
                res_sql=db.query(query_sql)
                for res in res_sql:
                    print 'news_id:{},news_title,{},company_name{}'.format(res['id'],res['title'],k)

    def get_company_kw_xls(self):
        data = xlrd.open_workbook(self.kwinfo_data_fp)
        tabel = data.sheets()[0]
        nrows = tabel.nrows
        com_kw_jc_dict = {tabel.row_values(i)[0]: tabel.row_values(i)[1].split(',') for i in range(nrows)}
        return com_kw_jc_dict


    def get_company_news_from_sql(self,mysql_params):
        if self.kwinfo_data_fp.endswith('xls'):
            com_kw_jc_dict = self.get_company_kw_xls()
        else:
            raise ValueError('Cannot get com_leader_jc_dict from {}'.format(self.kwinfo_data_fp))

        mysql=mysql_params
        db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                               user=mysql.get('user'),
                               password=mysql.get('password'), charset=mysql.get('charset'))
        for k,v in com_kw_jc_dict.items():
            print k,v
            query_sql_list = ['''SELECT id,title FROM t_top_news where title LIKE '%%{s}%%';'''.format(s=kw) for kw in v]
            for query_sql in query_sql_list:
                res_sql=db.query(query_sql)
                for res in res_sql:
                    print 'news_id:{},news_title,{},company_name{}'.format(res['id'],res['title'],k)



def leader_main():
    model=NewsBasedCompany('company_leader_namejc.xls')
    model.get_leader_news_from_sql(mysql_params=mysql)


def company_main():
    model=NewsBasedCompany('company_namejc.xls')
    model.get_company_news_from_sql(mysql_params=mysql)






if __name__ == '__main__':
    mysql = {
        "host": "117.78.60.108",
        "port": "3306",
        "database": "cityparlor",
        "password": "123456",
        "user": "es",
        "charset": "utf8"
    }
    # leader_main()
    company_main()
