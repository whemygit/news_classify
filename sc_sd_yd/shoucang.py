#!/usr/bin/env python
# -- coding: utf-8 --
import requests
from lxml import etree
import re
import time

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def get_resp(data):
    resp = requests.post('http://192.168.0.225:8080/cityparlor-web/cityparlor/cityparlor/collect/news/save', data=data)
    print resp.content


def get_page_url(url_obj):
    try:
        resp = requests.get(url_obj)
    except Exception as e:
        try:
            resp = requests.get(url_obj)
        except Exception as e:
            pass
    doc = etree.HTML(resp.content)
    for url in doc.xpath('//div[@class="newsList"]/ul/li/a[2]'):
        yield url.xpath('@href')[0], url.xpath('@title')[0]


def replace_img(text, srcs):
    """
    替换内容中的图片路径
    :param text: 文本内容
    :param srcs: 链表形式的图片url
    :return:
    """
    for src in srcs:
        new_path = 'https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/' + src.split('/')[-1]
        # new_path = 'https://cityparlor.oss-cn-beijing.aliyuncs.com/img_test/datupian.jpg'
        text = text.replace(src, new_path)
    return text


def filter_tags(htmlstr):
    """
    清洗和过滤标签
    :param htmlstr: 页面筛选后的html代码块
    :return: 返回处理后的带标签内容
    """
    # 替换p标签
    s = re.sub(r'<p.*?>', '<p>', htmlstr)
    # 过滤img标签
    s = re.sub(r'width="\d+"', '', s)
    # 替换div
    s = re.sub(r'<div.*?>', '<div>', s)
    # 处理script标签
    s = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', '', s)
    s = re.sub(r'<\s*script[^>]*>', '', s)
    # 去掉a标签
    s = re.sub(r'<a.*?>', '', s)
    s = re.sub(r'</a>', '', s)
    return s


def page_parse(url, t):
    try:
        resp = requests.get(url)
    except Exception as e:
        try:
            resp = requests.get(url)
        except Exception as e:
            return
    doc = etree.HTML(resp.content)
    try:
        # text_desc = etree.tostring(doc.xpath('//div[@class="intro"]')[0], xml_declaration=True, encoding='utf-8')
        text_f = doc.xpath('//div[@class="info"]/div[@class="fl"]/span[2]//text()')[1].strip()
    except IndexError:
        return
    try:
        text = etree.tostring(doc.xpath('//div[@class="detail newsContentDetail"]')[0], xml_declaration=True,
                          encoding='utf-8')
    except IndexError:
        return
    img_l = re.findall('<img.+?src="(.+?)".+?/>', text)
    if img_l:
        for img in img_l:
            yield img
        img_app = ','.join('https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/' + _.split('/')[-1] for _ in img_l)
        text = replace_img(text, img_l)
        text = filter_tags(text)
        info_d = dict()
        info_d['title'] = t
        info_d['source'] = text_f
        info_d['content'] = text
        info_d['pics'] = img_app
        # info_d['newsDesc'] = text_desc
        # print title
        get_resp(info_d)


if __name__ == '__main__':
    localtime = time.localtime(time.time())
    y = time.strftime("%Y", localtime)
    m = time.strftime("%m", localtime)
    with open('src', 'w') as fw:
        for i in xrange(1, 150):
            url_f = 'http://www.artron.net/order_news.php?pathNamea=&pathNameb=&mouth={mouth}&year={year}&Page={page}'.format(
                mouth=m, year=y, page=i)
            # print url_f
            for u, title in get_page_url(url_f):
                for href in page_parse(u, title):
                    fw.write(href + '\n')