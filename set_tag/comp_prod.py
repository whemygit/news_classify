#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb
import mysql_connect


reload(sys)
sys.setdefaultencoding("utf-8")

#填充mysql中company表数据
def comp_insert():
    '''将youpin文本文件中的数据向mysql中company表填充'''
    db=mysql_connect.mysql_connect()
    with open('youpin','r') as fr:
        sql = "INSERT INTO company (city,title,class,companyDesc) VALUES (%s,%s,%s,%s)"
        for line in fr.readlines():
            print line
            comp_info=line.split('\x01')
            print comp_info
            # print comp_info[4][1:-1]
            db.insert(sql, comp_info[1], comp_info[3], comp_info[0],
                      comp_info[4][1:-1])
    db.close()

def comp_class_get(company):
    '''从设置标签所依据的数据表返回指定字段等于company时的标签值'''
    db=mysql_connect.mysql_connect()
    select_sql='SELECT title, class FROM company WHERE title='+'\''+company+'\''
    # print select_sql
    select_res=db.query(select_sql)
    comp_class=select_res[0].get('class')
    print comp_class
    return comp_class
    db.close()


def get_company(table_set):
    '''选择要设置标签的数据库表，返回设置标签时所要依据的字段列表'''
    db=mysql_connect.mysql_connect()
    select_sql='SELECT title FROM '+table_set
    print select_sql
    select_res=db.query(select_sql)
    comp_list=[]
    for comp in select_res:
        comp_name=comp.get('title')
        print comp_name                                    ###########武汉大学名称格式问题
        comp_list.append(comp_name)
    return comp_list
    db.close()


if __name__ == '__main__':
    #通过company的分类为product表的classPid标签设置值
    for comp in get_company('product'):
        classPid=comp_class_get(comp)
        update_sql='UPDATE product SET classPid='+str(classPid)+' WHERE companyName='+'\''+comp+'\''
    # get_company()