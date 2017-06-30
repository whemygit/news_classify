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
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.lanzhou.gov.cn',
    # 'If-Modified-Since':'Wed, 21 Jun 2017 06:10:24 GMT',
    # 'If-None-Match':'"bef1-5527239431400"',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }


# url = 'http://www.shenyang.gov.cn/zwgk/fggw/zcjd/index.shtml'
# url='http://www.shenyang.gov.cn/zwgk/fggw/zfwj/index.shtml'
# url='http://www.qingdao.gov.cn/n172/n68422/n26981869/index.html'
# url='http://www.foshan.gov.cn/zwgk/zcwj/zcjd/'
url='http://www.lzcz.gov.cn/zwgk/czsj/czsj_anr_/yjsxx4.htm'
area = '兰州'
category_id = '3'
category_pid = '1702101039265780000'
def get_resp():
    resp = requests.get(url)
    print resp.content
    return resp.content


def get_href():
    con=get_resp()
    doc = etree.HTML(con)
    res=re.findall(r'href=&quot;/art/.*.html',con)
    titles=re.findall(r'=\'0\'>.*?;ye',con)
    # res = doc.xpath('//*[@id="div3665"]/table/tbody/tr/td/table[5]/tbody/tr[2]/td/table/tbody/tr/td[1]/a/@href')
    # titles=doc.xpath('//*[@id="div3665"]/table/tbody/tr/td/table[5]/tbody/tr[2]/td/table/tbody/tr/td[1]/a/@mc')
    # # create_date=doc.xpath('/html/body/div[5]/div/div[2]/div/div[1]/table/tbody/tr/td[3]/text()')
    print res
    print len(res)
    # print titles
    # print len(titles)
    for i in titles:
        print i[5:-4]
    return res,titles

def get_detail():
    res,titles=get_href()
    for i,r in enumerate(res):
        try:
            resp=requests.get(r)
        except:
            print 'add someting'
            add_in='http://www.lanzhou.gov.cn'
            resp=requests.get(add_in+r)
        title=titles[i][5:-4]
        doc=etree.HTML(resp.content)
        text_f='兰州市政府网'
        # text_f=doc.xpath('/html/body/div[3]/div[4]/div[2]/text()[4]')
        # ar_content=re.findall(re.compile(r'</div></div>>>(.*?)<div class="con_line">', re.S),
        #                resp.content)[0]
        ar_content=doc.xpath('//*[@id="zoom"]')
        ar_content=etree.tostring(ar_content[0],xml_declaration=True,encoding='utf-8')
        # ar_content=re.sub(r'<div .*?>(.*?)</div>','',ar_content)
        # ar_content=re.sub(r'<div .*?>','',ar_content)
        # ar_content=re.sub(r'<h1>(.*?)</h1>','',ar_content)
        # ar_content=re.sub(r'<p style=".*?">(.*?)</p>','',ar_content)
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
    get_resp()
    get_href()
    # get_detail()
    # save_sql()