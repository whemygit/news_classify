#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import re
import time
import requests
from lxml import etree
import json
import torndb
import redis

reload(sys)
sys.setdefaultencoding("utf-8")

now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
print now
category_pid, em_teg = 0, 2

def mysql_connect():
    # mysql_par = {'ip': "192.168.0.202:3306",
    #              'port': '3306',
    #              'database': 'spider',
    #              'user': 'suqi',
    #              'password': '123456',
    #              'charset':'utf8'}

    mysql_par={'ip':"119.57.93.42",
               'port':'3306',
               'database':'spider',
               'user':'bigdata',
               'password':'zhongguangzhangshi'}


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

headers={"Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Cookie":"UM_distinctid=15daaea044060e-0600ce68bf14bd-4e47052e-1fa400-15daaea044162f; cnsuuid=9693639a-403e-81ef-8301-4b5c2d45c55e1330.582074663635_1501827142507; JSESSIONID=aaaVQbty0dQOxdzVq4R2v; __jsluid=1a98acfe2bf27aaf8100ea2933c5e301",
    "Host":"channel.chinanews.com",
    "Referer":"http://www.chinanews.com/society/",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

# main_url='http://channel.chinanews.com/cns/s/channel:sh.shtml?pager=1&pagenum=20&_='
def get_news_urllist(main_url):
    resp=requests.get(main_url,headers=headers)
    s=resp.text
    s = re.sub(r'var specialcnsdata = ', '', s)
    s=re.sub(r'\;','',s)
    s=s.strip()
    s_dict=json.loads(s.strip())
    new_url_list=[]
    new_title_list = []
    new_date_list = []
    for i in s_dict.values()[0]:
        new_url=i.get('url')
        new_title=i.get('title')
        new_date=i.get('url').split('/')
        new_date=str(new_date[4])+'-'+new_date[5]
        new_url_list.append(new_url)
        new_title_list.append(new_title)
        new_date_list.append(new_date)
        # yield new_url,new_title,new_date
    return new_url_list,new_title_list,new_date_list


def get_news_detail(new_url):
    resp=requests.get(new_url)
    detail=etree.HTML(resp.content)
    # new_text=detail.xpath('//*[@id="cont_1_1_2"]/div[6]')
    new_text = etree.tostring(detail.xpath('//div[@class="left_zw"]')[0], xml_declaration=True,
                              encoding='utf-8').decode()
    new_text = filter_tags(new_text)
    try:
        new_source=detail.xpath('//div[@class="left-t"]/text()')[0]
        new_source=new_source.split(r'来源：')[1]
    except:
        new_source=''
    imgs = re.findall(r'<img.+?src="(.+?)".+?>', new_text)
    new_text = replace_img(new_text, imgs)
    img_show = []
    if len(imgs) == 1 or len(imgs) >= 3:  # 大于三张图可以考虑留一下。
        img_show = ','.join(
            ['https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/' + src.split('/')[-1] for src in
             imgs])
        if len(imgs) > 3:
            img_show = ','.join(img_show.split(',')[0:3])
    if not img_show:
        img_show = None
    return new_text,new_source,imgs,img_show

category_dict={"cj":"caijing",
    "cul":"wenhua",
    "yl":"yule",
    "life":"shenghuo",
    "gn":"shizheng",
    "auto":"qiche",
    "ty":"tiyu",
    "sh":"shehui"}

tag_classsify={
    "auto":"0",
    "cj":"1",
    "sh":"3",
    "life":"4",
    "gn":"5",
    "ty":"6",
    "cul":"7",
    "yl":"8"}

news_type_id={
    "auto":"1708161042182380000",
    "cj":"1708161040317410000",
    "sh":"1708161038521350000",
    "life":"1708161041028580000",
    "gn":"1708161041390550000",
    "ty":"1708161040066730000",
    "cul":"1708161039170770000",
    "yl":"1708161039480920000"}



# main_url='http://channel.chinanews.com/cns/s/channel:cj.shtml?&pagenum=20&_='
# redis_urllist=redis.Redis()
def news_info_collect(main_url):
    new_url_list, new_title_list, new_date_list=get_news_urllist(main_url)
    # for url in new_url_list:
    #     if redis_urllist.exists(url):
    #         new_url_list.remove(url)
    #     else:
    #         redis_urllist.set(url,1)
    #         redis_urllist.expire(url,259200)
    for i,new_url in enumerate(new_url_list):
        new_title=new_title_list[i]
        new_date=new_date_list[i]
        if new_date==now:
            try:
                new_text, new_source, imgs, img_show=get_news_detail(new_url)
            except:
                continue
            news_info = dict()
            news_info['url']=new_url
            news_info['date'] = new_date
            news_info['title'] = new_title
            news_info['content'] = new_text
            news_info['source'] = new_source
            if news_info['source']=='':
                news_info['source']='中国新闻网'
            news_info['imgs'] = imgs
            news_info['img_show'] = img_show
            yield news_info

def main():
    db = mysql_connect()
    import traceback
    sql = r"""insert into _news_data_classify (category_id,category_pid,em_teg,title, news_date, text_f, img_show, text, classify_tag) values (%s, %s, %s,%s, %s, %s, %s, %s, %s)"""
    with open('src', 'w ') as fw:
        for item in category_dict:
            print item
            main_url = 'http://channel.chinanews.com/cns/s/channel:%s.shtml?&pagenum=20&_='%item
            classify_tag=tag_classsify.get(item)
            newstype_id = news_type_id.get(item)
            for news_info in news_info_collect(main_url):
                print news_info.get('url'),news_info.get('title'),news_info.get('source'),type(news_info.get('source'))
                try:
                    res = db.insert(sql, newstype_id, category_pid, em_teg,news_info.get('title'), news_info.get('date'), news_info.get('source'),news_info.get('img_show'), news_info.get('content'), classify_tag)
                except Exception as e:
                    print e
                for i in news_info.get('imgs'):
                    fw.write(i+'\n')



if __name__ == '__main__':
    main()
