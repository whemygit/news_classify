#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import requests
from lxml import etree
import jieba
import time
import re
import torndb

reload(sys)
sys.setdefaultencoding("utf-8")

today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
yesterday=time.strftime('%Y-%m-%d',time.localtime(time.time()-86400))

def mysql_connect():
    mysql_par = {'ip': "192.168.0.202:3306",
                 'port': '3306',
                 'database': 'spider',
                 'user': 'suqi',
                 'password': '123456',
                 'charset':'utf8'}

    # mysql_par={'ip':"119.57.93.42",
    #            'port':'3306',
    #            'database':'spider',
    #            'user':'bigdata',
    #            'password':'zhongguangzhangshi'}


    db = torndb.Connection(host=mysql_par.get('ip'),
                           database=mysql_par.get('database'),
                           user=mysql_par.get('user'),
                           password=mysql_par.get('password')
                           # charset=mysql_par.get('charset')
                           )
    return db

def filter_tags(htmlstr):
    """
    清洗和过滤标签
    :param htmlstr: 页面筛选后的html代码块
    :return: 返回处理后的带标签内容
    """
    # 替换p标签
    s = re.sub(r'<p.*?>', '<p>', htmlstr)
    # 替换img属性
    s = re.sub(r'img_width="\d+"', '', s)
    s = re.sub(r'img_height="\d+"', '', s)
    # 替换div
    s = re.sub(r'<div.*?>', '<div>', s)
    # 处理script标签
    s = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', '', s)
    s = re.sub(r'<\s*script[^>]*>', '', s)
    # 去掉a标签
    s = re.sub(r'<a.*?>', '', s)
    s = re.sub(r'</a>', '', s)
    return s

def replace_img(text, srcs):
    for src in srcs:
        new_path = 'http://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/' + src.split('/')[-1]
        text = text.replace(src, new_path)
    return text


def news_cut_outstop(news_text):
    stopwd=[line.strip().decode('utf-8') for line in open('D:/gitcode/mypython/R+python/my_news_classify/stopw.txt','r').readlines()]
    news_text=news_text.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
    seg_list=jieba.cut(news_text,cut_all=False)
    seg_list_outstop=[w for w in seg_list if w not in stopwd]
    return seg_list_outstop

def wangyi_title_segset():
    main_url='http://www.163.com/'
    title_xpath_rules='//div[@class="yaowen_news"]/div/ul/li/a/text()'
    resp=requests.get(main_url)
    detail=etree.HTML(resp.text)
    yaowen_title_list=detail.xpath(title_xpath_rules)
    key_words_list = []
    for title in yaowen_title_list:
        for t in news_cut_outstop(title):
            if len(t) >= 2:
                key_words_list.append(t)
    keywords_set = set(key_words_list)
    return keywords_set

def souhu_title_segset():
    main_url='http://www.sohu.com/'
    title_xpath_rules=['//div[@class="news"]/p/a/text()','//div[@class="list16"]/ul/li/a/strong/text()','//div[@class="list16"]/ul/li/a/text()']
    resp=requests.get(main_url)
    detail=etree.HTML(resp.text)
    title_list = []
    for rule in title_xpath_rules:
        yaowen_title_list=detail.xpath(rule)
        for i in yaowen_title_list:
            title_list.append(i.strip())
    key_words_list = []
    for title in title_list:
        for t in news_cut_outstop(title):
            if len(t) >= 2:
                key_words_list.append(t)
    keywords_set = set(key_words_list)
    return keywords_set

def intersect_keywd_set():
    wangyi_keywd_set=wangyi_title_segset()
    souhu_keywd_set=souhu_title_segset()
    keywd_set=wangyi_keywd_set&souhu_keywd_set
    return keywd_set

def title_url_list():
    main_url='http://news.sina.com.cn/hotnews/#2'
    resp=requests.get(main_url)
    # print resp.content
    detail=etree.HTML(resp.content)
    title_list=detail.xpath('//td[@class="ConsTi"]/a/text()')
    url_list=detail.xpath('//td[@class="ConsTi"]/a/@href')
    title_url_dict={}
    for i,title in enumerate(title_list):
        title_url_dict.update({title:url_list[i]})
    return title_url_dict

def recomend_news():
    keywd_set=intersect_keywd_set()
    keywd_list=list(keywd_set)
    keywd_list.reverse()
    title_url_dict=title_url_list()
    rec_news_dict={}
    for keywd in keywd_list:
        # print keywd
        for title in title_url_dict:
            if keywd in title:
                rec_news_dict.update({title_url_dict.get(title):title})
        keywd_list.remove(keywd)
    return rec_news_dict

def news_spider():
    rec_news_dict=recomend_news()
    for url in rec_news_dict:
        # print url
        if url.startswith('http://slide') or url.startswith('http://video') or url.startswith('http://news') or url.startswith('http://sports'):
            # print url
            continue
        url_split=url.split('/')
        if today in url_split or yesterday in url_split:
            # print url
            if today in url_split:
                new_date=today
            else:
                new_date=yesterday
            new_content, imgs, img_show=news_detail_spider(url)
            new_title=rec_news_dict.get(url)
            new_source='新浪新闻'
            # print url, new_title, new_date, new_content, imgs, img_show
            # break
            yield new_title, new_date, new_source, new_content, imgs, img_show



def news_detail_spider(new_url):
    # new_url='http://news.sina.com.cn/s/wh/2017-08-21/doc-ifykcypq1380073.shtml'
    resp=requests.get(new_url)
    # print resp.content
    detail=etree.HTML(resp.content)
    # print chardet.detect(resp.content)
    # new_title=detail.xpath('//*[@id="main_title"]/text()')[0]
    # print new_title
    new_content = etree.tostring(detail.xpath('//*[@id="artibody"]')[0], xml_declaration=True,
                              encoding='utf-8').encode()
    new_content=filter_tags(new_content)
    new_content = re.sub(r'<p>[\s|\S]*?lcsds_icon.jpg[\s|\S]*?</p>', '', new_content)
    imgs=re.findall(r'<img.+?src="(.+?)".+?>', new_content)
    new_content=replace_img(new_content,imgs)
    img_show = []
    if len(imgs) == 1 or len(imgs) >= 3:  # 大于三张图可以考虑留一下。
        img_show = ','.join(
            ['https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/' + src.split('/')[-1] for src in
             imgs])
        if len(imgs) > 3:
            img_show = ','.join(img_show.split(',')[0:3])
    if not img_show:
        img_show = None
    return new_content,imgs,img_show


def main():
    category_id, category_pid, em_teg=0,0,2
    db = mysql_connect()
    import traceback
    sql = r"""insert into rec_news_data (category_id,category_pid,em_teg,title, news_date, text_f, text, img_show) values (%s, %s, %s, %s, %s, %s, %s, %s)"""
    rec_res=news_spider()
    with open('src', 'w ') as fw:
        for new_title, new_date, new_source, new_content, imgs, img_show in rec_res:
             db.insert(sql, category_id, category_pid, em_teg, new_title, new_date, new_source, new_content, img_show)
             for i in imgs:
                 fw.write(i+'\n')


if __name__ == '__main__':
    main()
    # keywd_set=intersect_keywd_set()
    # for i in keywd_set:
    #     print i
    # main()

