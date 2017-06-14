#!/usr/bin/env python
# -- coding: utf-8 --
import re
import time
import json

import requests
from lxml import etree
import torndb
import gevent
from gevent import monkey

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# mysql = {
#     "host": "119.57.93.42",
#     "port": "3306",
#     "database": "spider",
#     "password": "zhongguangzhangshi",
#     "user": "bigdata",
#     "charset": "utf8"
# }

monkey.patch_all()

mysql = {
    "host": "192.168.0.202",
    "port": "3306",
    "database": "spider",
    "password": "123456",
    "user": "suqi",
    "charset": "utf8"
}

db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))

date_n = time.strftime("%Y-%m-%d", time.localtime(time.time()))


def get_proxies():
    r = requests.get('http://127.0.0.1:8000/?types=0&count=5&country=国内')
    ip_ports = json.loads(r.text)
    print ip_ports
    ip = ip_ports[0][0]
    port = ip_ports[0][1]
    proxies = {
        'http': 'http://%s:%s' % (ip, port),
        'https': 'http://%s:%s' % (ip, port)
    }
    return proxies


def get_response(url, title=None, create_date=None):
    resp = requests.get(url)
    if title:
        return resp, title, create_date
    return resp


def get_page_url(url):
    page = get_response(url)
    try:
        content = json.loads(page.content)
    except ValueError:
        print url
    try:
        for info in content.get('data').get('items'):
            url = info.get('url')
            title = info.get('title')
            create_date = info.get('created_at').split(' ')[0]
            if not url:
                url = 'https://baijia.baidu.com/s?old_id=' + info.get('id')
            url = url.replace('baijiahao', 'baijia')
            yield url, title, create_date
    except Exception:
        print content, url


def get_page_content(url_list, entertainment_list):
    jobs = [gevent.spawn(get_response, url, title, create_date) for url, title, create_date in url_list]
    gevent.joinall(jobs)

    for page, title, create_date in [job.value for job in jobs]:
        # print title, create_date
        celebrity_id, fun, type_id = '', 'washington', '1705151252197800035'
        for d in entertainment_list:
            if d.get('title') in title:
                celebrity_id = d.get('celebrity_id')
                fun = d.get('fun')
                type_id = d.get('type_id')
                break
        text = re.findall(re.compile(r'<section class="news-content">(.*?)<div class="rights">', re.S), page.content)[0]
        text = filter_tags(text)
        imgs = re.findall('<img.+?src="(.+?)".+?/>', text)
        text = replace_img(text, imgs)
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
        if img_show:
            print create_date, fun, page.status_code, page.url
            save_to_mysql(title, text, celebrity_id, type_id, fun, img_show, classify, create_date)
            for i in imgs:
                yield i


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


def save_to_mysql(title, content, celebrity_id, type_id, fun, img_show, classify, create_date):
    sql = r"""insert into _t_channel_news (title, content, celebrity_id, type_id, fun, img_show, classify, create_date) values (%s, %s, %s, %s, %s, %s, %s, %s)"""
    try:
        res = db.insert(sql, title, content, celebrity_id, type_id, fun, img_show, classify, create_date)
        # res_sql = \
        #     'delete from _news_data  where newsid in (select newsid from (select  max(newsid) as newsid,count(title)' \
        #     ' as count from _news_data group by title having count > 1 order by count desc) as tab )'
        # db.execute(res_sql)
    except Exception as e:
        print e


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


def get_name_and_id():
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


def run(url_f, entertainment_list):
    with open('src', 'w') as fw:
        for num in xrange(18):
            href = url_f.format(num=num * 15)
            url_list = [(url, title, create_date) for url, title, create_date in get_page_url(href)]
            try:
                for img in get_page_content(url_list, entertainment_list):
                    fw.write(img + '\n')
            except IndexError as e:
                print e


if __name__ == '__main__':
    u = 'https://baijia.baidu.com/listarticle?ajax=json&_limit=15&_skip={num}&quality=1&_desc=top_st%2Cupdated_at'
    e_list = [n for n in get_name_and_id()]
    run(u, e_list)
    # for i in get_name_and_id():
    #     print i