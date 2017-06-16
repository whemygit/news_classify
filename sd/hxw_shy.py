#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import sys
import sys
import re
import time
import requests
from lxml import etree
import urllib
from bs4 import BeautifulSoup
import torndb
import json

reload(sys)
sys.setdefaultencoding("utf-8")

now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
print now

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
    s = re.sub(r'width="\d+"', '', s)
    s = re.sub(r'height="\d+"', '', s)
    # 处理script标签
    s = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', '', s)
    s = re.sub(r'<\s*script[^>]*>', '', s)
    # 去掉a标签
    s = re.sub(r'<a.*?>', '', s)
    s = re.sub(r'</a>', '', s)
    # 去掉input标签
    s = re.sub(r'<input.*?>', '', s)
    return s


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

def replace_img(text, srcs_1,srcs):
    for i,src in enumerate(srcs_1):
        new_path = 'https://cityparlor.oss-cn-beijing.aliyuncs.com/sd_yd_img/img/' + srcs[i].split('/')[-1]
        text = text.replace(src, new_path)
    return text


def get_content(url):
    resp=requests.get(url,headers=header)
    return resp.text

def get_new_href(content):
    doc=etree.HTML(content)
    href=doc.xpath('//h2/a/@href')
    # title=doc.xpath('//h2/a/text()')
    return href

def get_article_detail():
    content_1=get_content('https://www.huxiu.com/')
    type_id = '1705171148455171636'
    hrefs=get_new_href(content_1)
    for href in hrefs:
        content = get_content('https://www.huxiu.com' + href)
        if not content:
            continue

        doc=etree.HTML(content)

        try:
            create_date = doc.xpath('//span[@class="article-time pull-left"]/text()')[0].split(' ')[0]
        except IndexError as err:
            create_date = doc.xpath('//span[@class="article-time"]/text()')[0].split(' ')[0]
        if create_date!=now:
            break

        try:
            title = doc.xpath('//h1[@class="t-h1"]/text()')[0]
        except IndexError as er:
            continue
        title = re.sub('\n', '', title)
        title = re.sub(' ', '', title)

        try:
            first_pic = doc.xpath('//div[@class="article-img-box"]/img/@src')[0]
            first_pic = first_pic.split('?')[0]
            pic = '<p><img src="' + first_pic + '"/></p>'
        except IndexError as err:
            pic = ''

        try:
            article_content = \
            re.findall(re.compile(r'<div id=.* class="article-content-wrap">(.*?)<div class="neirong-shouquan">', re.S),
                       content)[0]
        except IndexError as err:
            try:
                article_content = re.findall(
                    re.compile(r'<div id=.* class="article-content-wrap">(.*?)<div class="neirong-shouquan-public">',
                               re.S), content)[0]
            except:
                continue
        article_content = pic + article_content.encode('utf-8')
        article_content = filter_tags(article_content)

        imgs = []
        imgs_1 = re.findall('<img.*?src="(.*?)".*?>', article_content)
        for img in imgs_1:
            if '?' in img:
                imgs.append(img.split('?')[0])
            else:
                imgs.append(img)
        # print imgs
        s = '/0'  # 图片格式不对，跳过
        flag = 0
        for im in imgs:
            if im.endswith(s):
                flag = 1
                break
        if flag == 1:
            continue

        article_content = replace_img(article_content, imgs_1, imgs)
        # print article_content
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

        yield title, create_date, article_content, img_show, classify, imgs,type_id

def get_name_and_id():
    # proxies=get_proxies()
    resp = requests.get('http://cms.loongscity.com/cityparlor-web/cityparlor/cityparlor/channel/celebrity/list')
    info = json.loads(resp.content)
    ret = info.get('retObj')
    for r in ret:
        r = json.loads(json.dumps(r))
        f = r.get('fun')
        if f != 'washington':
            continue
        info_d = dict()
        info_d['title'] = r.get('title')
        info_d['celebrity_id'] = r.get('id')
        info_d['fun'] = f
        info_d['type_id'] = r.get('typeId')
        yield info_d


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

def save_and_write():
    db=mysql_connect()
    sql = "INSERT INTO syd (title,content,create_date,img_show,classify,type_id) VALUES (%s,%s,%s,%s,%s,%s)"

    res=get_article_detail()
    with open('src', 'w') as fw:
        for title,create_date,article_content,img_show,classify,imgs,type_id in res:
            if img_show:
                print title
                try:
                    db.insert(sql, title, article_content, create_date,img_show,classify,type_id)
                except:
                    print 'Error connecting to MySQL on 192.168.0.202'
                    continue
                for i in imgs:
                    fw.write(i+'\n')
    db.close()


def update_mysql():
    db=mysql_connect()
    select_sql='SELECT title FROM sd_hxw;'
    title_select=db.query(select_sql)
    print title_select
    for ar_title in title_select:
        print ar_title['title']
        info_d = get_name_and_id()
        for celebrity_info in info_d:
            name = celebrity_info.get('title')
            if name in  ar_title['title']:
                fun = celebrity_info.get('fun')
                celebrity_id = celebrity_info.get('celebrity_id')

                update_s='UPDATE sd_hxw SET celebrity_id=%s,fun=%s WHERE title=%s;'%(celebrity_id,fun,ar_title['title'])
                db.execute(update_s)
    db.close()


if __name__ == '__main__':
    save_and_write()
    update_mysql()
