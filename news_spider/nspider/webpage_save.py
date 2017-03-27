#!/usr/bin/env python
# -- coding: utf-8 --
import os
import logging
import json
import urllib
from readability import Document
import re
import urlparse

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

town_img_path = '../town/img/'


def save_file(area, html, url, output, category_id, category_pid, img_path, stop_words):
    out_dict = dict()
    res = get_info(html, url, category_id, category_pid, img_path, stop_words)
    if not res:
        return 'Fail'
    out_dict[area] = res
    try:
        with open(output, "a") as fw:
            fw.write(json.dumps(out_dict) + '\n')
        logging.info("Success to save url(%s) to local file.", url)
    except IOError as e:
        logging.error("Failed to save url(%s) to local as Exception: %s.", url, e)
    return None


def get_info(html, url, category_id, category_pid, img_path, stop_words):
    doc = Document(html)
    try:
        article = doc.summary()  # 新闻内容
    except Exception as e:
        return None
    tags_p = re.findall('<p[.\s\S]*?>[.\s\S]*?</p>', article)
    if len(tags_p) <= 2:
        return None
    _title = doc.title()
    if '_' in _title:
        t = _title.split('_')
        title = t[0]
        try:
            text_f = re.findall(u'来源：(.*?)<', html)[0]  # 新闻来源
        except IndexError:
            text_f = t[-1]
    else:
        title = _title
        text_f = None
    text, img_list = parser(html, url)  # 新闻内容 图片
    is_stop = [w for w in stop_words if w in text]
    if is_stop:
        return None
    img_show = []
    if len(img_list) == 1 or len(img_list) == 3:
        img_show = ','.join(
            ['http://cityparlor.oss-cn-beijing.aliyuncs.com/town/img/' + src.split('/')[-1] for src in img_list])
    update = get_update(html)
    for img_href in img_list:
        get_img_s(img_href, img_path + img_href.split('/')[-1])
    return [category_id, category_pid, title, update, text_f, text, img_show]


def get_update(html):
    """
    新闻发布时间精细化处理
    ps：待优化
    :param html:
    :return:
    """
    try:
        update = re.findall('\d{4}-\d+-\d+', html)[0]
    except IndexError:
        try:
            update = re.findall('\d+年\d+月\d+', html)[0].replace('年', '-').replace('月', '-')
        except Exception:
            return None
    return update


def replace_img(text, srcs):
    """
    替换内容中的图片路径
    :param text: 文本内容
    :param srcs: 链表形式的图片url
    :return:
    """
    for src in srcs:
        new_path = 'http://cityparlor.oss-cn-beijing.aliyuncs.com/town/img/' + src.split('/')[-1]
        text = text.replace(src, new_path)
    return text


def get_img_url(img_url_list, img_name_list):
    """
    获取新闻中图片链接
    :param img_url_list:
    :param img_name_list:
    :return:
    """
    for img_name in img_name_list:
        for img_url in img_url_list:
            if img_name in img_url:
                yield img_name, img_url


def parser(html, url):
    """
    新闻主体内容替换和图片标签
    :param html:
    :param img_url_list:
    :return:
    """
    article = Document(html).summary()
    article = filter_tags(article)
    img_list = re.findall('<img.+?src="(.+?)".+?/>', article)
    article = replace_img(article, img_list)
    if img_list:
        img_list = [urlparse.urljoin(url, src) for src in img_list]
    return article, img_list


def get_img_s(img_url, img_path):
    """
    下载图片
    :param img_url:
    :param img_path:
    :return:
    """
    try:
        data = urllib.urlopen(img_url).read()
        f = file(img_path, "wb")
        f.write(data)
        f.close()
    except IOError:
        print img_url


def filter_tags(html):
    """
    清洗和过滤标签
    :param htmlstr: 页面筛选后的html代码块
    :return: 返回处理后的带标签内容
    """
    # 替换p标签
    s = re.sub(r'<p.*?>', '<p>', html)
    # 替换span标签
    s = re.sub(r'<span.*?>', '<span>', s)
    # 替换div
    s = re.sub(r'<div.*?>', '<div>', s)
    # 处理script标签
    s = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', '', s)
    s = re.sub(r'<\s*script[^>]*>', '', s)
    # 去掉a标签
    s = re.sub(r'<a.*?>', '', s)
    s = re.sub(r'</a>', '', s)
    # 去掉style标签
    s = re.sub(r'<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', '', s)
    s = re.sub(r'<\s*style[^>]*>', '', s)
    return s


if __name__ == '__main__':
    area = 'beijing'
    url = 'http://www.gov.cn/zhengce/2017-03/09/content_5175649.htm'
    import webpage_urlopen
    html = webpage_urlopen.webpage_urlopen(url, 5)
    output = '../output/article'
    category_id = 1
    category_pid = 11
    save_file(area, html, url, output, category_id, category_pid)
