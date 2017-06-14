#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import re
import time
import requests
from lxml import etree
import urllib
from bs4 import BeautifulSoup
import torndb

reload(sys)
sys.setdefaultencoding("utf-8")

def mysql_connect():
    mysql_par={'ip':"192.168.0.202",
               'port':'3306',
               'database':'spider',
               'user':'root',
               'password':'neiwang-zhongguangzhangshi'}

    # mysql_par={'ip':"119.57.93.42",
    #            'port':'3306',
    #            'database':'spider',
    #            'user':'bigdata',
    #            'password':'zhongguangzhangshi'}


    db=torndb.Connection(host=mysql_par['ip'],
                         database=mysql_par['database'],
                         user=mysql_par['user'],
                         password=mysql_par['password'])
    return db

def filter_tags(htmlstr):
    """
    清洗和过滤标签
    :param htmlstr: 页面筛选后的html代码块
    :return: 返回处理后的带标签内容
    """
    s = re.sub(r'<p class="image">', '', htmlstr)
    # 替换p标签
    s = re.sub(r'<p.*?>', '<p>', s)
    # 去掉h和style标签
    s = re.sub(r'</?h.>', '', s)
    s = re.sub(r'<style>[\s.\S]*?</style>', '', s)
    # 替换div
    s = re.sub(r'<div.*?>', '', s)
    # 替换img属性
    s = re.sub(r'img_width="\d+"', '', s)
    s = re.sub(r'img_height="\d+"', '', s)
    # 处理script标签
    s = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', '', s)
    s = re.sub(r'<\s*script[^>]*>', '', s)
    # 去掉a标签
    s = re.sub(r'<a.*?>', '', s)
    s = re.sub(r'</a>', '', s)
    # 去掉input标签
    s = re.sub(r'<input.*?>', '', s)
    return s

def replace_img(text, srcs):
    """
    替换内容中的图片路径
    :param text: 文本内容
    :param srcs: 链表形式的图片url
    :return:
    """
    for src in srcs:
        new_path = 'https://cityparlor.oss-cn-beijing.aliyuncs.com/sd_yd_img/img/' + src.split('/')[-1]
        text = text.replace(src, new_path)
    return text


def file2dit(filepath):
    with open(filepath,'r') as fr:
        lines=fr.readlines()
        d={}
        for line in lines:
            # print line
            line=line.replace('\n','')
            kv=line.split(':',1)
            d[kv[0]]=kv[1]
        return d

header=file2dit('header')
data=file2dit('data')
print data

def get_content(url):
    resp=requests.get(url,headers=header,params=data)
    return resp.text

def get_new_href(content):
    doc=etree.HTML(content)
    href=doc.xpath('//h2/a/@href')
    return href

def get_detail():
    content=get_content('https://www.huxiu.com/search.html?')
    for href in get_new_href(content):
        content=get_content('https://www.huxiu.com'+href)
        # print content
        doc=etree.HTML(content)

        title=doc.xpath('//h1[@class="t-h1"]/text()')[0]
        title=re.sub('\n','',title)
        title=re.sub(' ','',title)

        try:
            create_date=doc.xpath('//span[@class="article-time pull-left"]/text()')[0].split(' ')[0]
        except IndexError as err:
            print 'create_date tag changed!'
            create_date=doc.xpath('//span[@class="article-time"]/text()')[0].split(' ')[0]
        print create_date

        # bs_obj=BeautifulSoup(content,'lxml')
        # article_content=bs_obj.find_all('div',{'class':'article-content-wrap'})[0]
        article_content = re.findall(re.compile(r'<div id=.* class="article-content-wrap">(.*?)<div class="neirong-shouquan-public">', re.S), content)[0]
        article_content = filter_tags(article_content)

        imgs = re.findall('<img.+?src="(.+?)".+?/>', article_content)
        article_content = replace_img(article_content, imgs)
        img_show = ''
        classify = 1
        if len(imgs) == 1 or len(imgs) >= 3:  # 大于三张图可以考虑留一下。
            img_show = ','.join(
                ['https://cityparlor.oss-cn-beijing.aliyuncs.com/sd_yd_img/img/' + src.split('/')[-1] for src
                 in
                 imgs])
            if len(imgs) == 1:
                classify = 2
            if len(imgs) > 3:
                img_show = ','.join(img_show.split(',')[0:3])

        yield title,create_date,article_content,img_show,classify

if __name__ == '__main__':
    db=mysql_connect()
    sql = "INSERT INTO syd (title,content,create_date,img_show,classify) VALUES (%s,%s,%s,%s,%s)"

    res=get_detail()
    for title,create_date,article_content,img_show,classify in res:
        if img_show:
            db.insert(sql, title, article_content, create_date,img_show,classify)
    db.close()


