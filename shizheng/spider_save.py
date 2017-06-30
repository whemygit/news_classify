#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import sys
import sys
import sys
import re
import time
import requests
from lxml import etree
import torndb
import json

reload(sys)
sys.setdefaultencoding("utf-8")

def mysql_connect():
    mysql_par = {'ip': "192.168.0.202",
                 'port': '3306',
                 'database': 'spider',
                 'user': 'root',
                 'password': 'neiwang-zhongguangzhangshi'}

    # mysql_par={'ip':"119.57.93.42",
    #            'port':'3306',
    #            'database':'spider',
    #            'user':'bigdata',
    #            'password':'zhongguangzhangshi'}


    db = torndb.Connection(host=mysql_par['ip'],
                           database=mysql_par['database'],
                           user=mysql_par['user'],
                           password=mysql_par['password'])
    return db

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }


# url = 'http://www.shenyang.gov.cn/zwgk/fggw/zcjd/index.shtml'
# url='http://www.shenyang.gov.cn/zwgk/fggw/zfwj/index.shtml'
# url='http://www.qingdao.gov.cn/n172/n68422/n26981869/index.html'
# url='http://www.foshan.gov.cn/zwgk/zcwj/zcjd/'
url='http://www.xa.gov.cn/ptl/def/def/index_1121_7019.html'
area = '西安'
category_id = '1'
category_pid = '14'
def get_resp():
    resp = requests.get(url)
    print resp
    # print resp.content
    return resp.content


def get_href():
    con=get_resp()
    doc = etree.HTML(con)
    res = doc.xpath('//a[@class="default"]/@href')
    titles=doc.xpath('//a[@class="default"]/@title')
    # create_date=doc.xpath('/html/body/div[5]/div/div[2]/div/div[1]/table/tbody/tr/td[3]/text()')
    print res
    # print len(res)
    # for r in res:
    #     print r
    print titles
    # print len(titles)
    # for i in titles:
    #     print i
    return res,titles

def get_detail():
    res,titles=get_href()
    for i,r in enumerate(res):
        try:
            resp=requests.get(r)
        except:
            print 'add someting'
            add_in='http://www.xa.gov.cn/websac/cat/'
            print add_in + r[-7:]
            resp=requests.get(add_in+r[-7:]+'.html')

        title=titles[i]
        doc=etree.HTML(resp.content)
        text_f='西安市政府网'
        # text_f=doc.xpath('/html/body/div[3]/div[4]/div[2]/text()[4]')
        # ar_content=re.findall(re.compile(r'</div></div>>>(.*?)<div class="con_line">', re.S),
        #                resp.content)[0]
        # try:
        #     ar_content=doc.xpath('//*[@id="vsb_content_501"]')
        # except IndexError as err:
        #     continue

        ar_content = doc.xpath('//*[@id="divContent"]')
        try:
            ar_content=etree.tostring(ar_content[0],xml_declaration=True,encoding='utf-8')
        except IndexError as err:
            print 'aaaaaa'
            continue
        #去掉a标签
        ar_content=re.sub(r'<a href=".*?">(.*?)</a>','',ar_content)


        # ar_content=re.sub(r'<div .*?>(.*?)</div>','',ar_content)
        # ar_content=re.sub(r'<div .*?>','',ar_content)
        # ar_content=re.sub(r'<h1>(.*?)</h1>','',ar_content)
        # ar_content=re.sub(r'<p style=".*?">(.*?)</p>','',ar_content)
        # print title
        # print ar_content
        # break
        yield title,text_f,ar_content


def save_sql():
    db=mysql_connect()
    sql = r"""insert into town_data_1 (area, category_id, category_pid, title, text_f, text)
             values (%s, %s, %s, %s, %s, %s)"""
    result=get_detail()
    for title,text_f,ar_content in result:
        db.insert(sql, area, category_id, category_pid, title, text_f, ar_content)
        print title
    db.close()

if __name__ == '__main__':
    # get_resp()
    # get_href()
    # get_detail()
    save_sql()