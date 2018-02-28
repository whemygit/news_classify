#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb

reload(sys)
sys.setdefaultencoding("utf-8")

class NewsBasedComkwSql():

    def __init__(self,mysql_params):
        self.mysql=mysql_params

        self.db = torndb.Connection(host=self.mysql.get('host'), database=self.mysql.get('database'),
                               user=self.mysql.get('user'),
                               password=self.mysql.get('password'), charset=self.mysql.get('charset'))
        self.name_kw_dict = self.get_name_kw_dict()


    def get_name_kw_dict(self):
        '''
        查询出公司全称，公司简称为键值对的字典，根据后续需求可以查询出根据company_id,company_abb为键值对的字典
        :return:
        '''

        select_sql = '''SELECT company_name,company_abb FROM company_kw;'''
        kw_res=self.db.query(select_sql)
        name_kw_dict={}
        for i in kw_res:
            name_kw_dict[i.get('company_name')]=i.get('company_abb').split(',')
        return name_kw_dict


    def get_news_bname_kw_dict(self):
        for k,v in self.name_kw_dict.items():
            print k,','.join(v)
            query_sql_list = ['''SELECT id,title FROM t_top_news where title LIKE '%%{s}%%';'''.format(s=kw) for kw in v]
            for query_sql in query_sql_list:
                res_sql=self.db.query(query_sql)
                for res in res_sql:
                    print 'news_id:{},news_title,{},company_name{}'.format(res['id'],res['title'],k)

if __name__ == '__main__':
    mysql = {
        "host": "117.78.60.108",
        "port": "3306",
        "database": "cityparlor",
        "password": "123456",
        "user": "es",
        "charset": "utf8"
    }
    model=NewsBasedComkwSql(mysql_params=mysql)
    model.get_news_bname_kw_dict()