#!/usr/bin/env python
# -- coding: utf-8 --
import HTMLParser
import json
import requests
from lxml import etree
import re
import traceback
import gevent
import urllib
from gevent import monkey
import time
import torndb
import MySQLdb

monkey.patch_all()

areas = ['北京市', '天津市', '上海市', '广州市', '深圳市',
         '鞍山市', '阜新市', '锦州市', '铁岭市', '辽阳市',
         '葫芦岛市', '营口市', '盘锦市', '沈阳市', '本溪市',
         '朝阳市', '抚顺市', '大连市', '丹东市','哈尔滨市',
         '龙岩市', '呼和浩特市', '阿坝藏族羌族自治州',
         '长春市','南京市','武汉市','重庆市',
         '成都市','西安市','石家庄市','太原市',
         '唐山市','包头市','吉林市','齐齐哈尔市',
         '徐州市','杭州市','福州市','南昌市',
         '济南市','青岛市','淄博市','郑州市',
         '长沙市','贵阳市','昆明市','兰州市',
         '乌鲁木齐市','合肥市','南宁市','海口市',
         '西宁市','银川','宁波市','厦门市','雄安新区',
         '肥城市', '胶州市', '即墨市', '龙口市',
         '平阴', '荣成市', '新泰市', '诸城市', '邹城市',
         '江西省','张家口市','三亚市','抚州市','赣州市',
         '贵溪市','吉安市','景德镇市',
         '九江市','南昌县','萍乡市','上饶市',
         '新余市','宜春市','鹰潭市','樟树市']
mysql = {
    "host": "119.57.93.42",
    "port": "3306",
    "database": "spider",
    "password": "zhongguangzhangshi",
    "user": "bigdata",
    "charset": "utf8"
}
# mysql = {
#     "host": "192.168.0.202",
#     "port": "3306",
#     "database": "spider",
#     "password": "123456",
#     "user": "suqi",
#     "charset": "utf8"
# }

category_id, category_pid, em_teg = 0, 0, 2

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

date_n = time.strftime("%Y-%m-%d", time.localtime(time.time()))

try:
    db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                           user=mysql.get('user'),
                           password=mysql.get('password'), charset=mysql.get('charset'))
except Exception, e:
    print(traceback.print_exc(e))


def fetch_page(url, proxies={}):
    try:
        print url
        response = requests.get(url, timeout=10, headers=headers, proxies=proxies)
    except requests.ConnectionError:
        time.sleep(10)
        try:
            response = requests.get(url, timeout=10, headers=headers, proxies=proxies)
        except Exception as e:
            return None
    except Exception as e:
        return None
    return response


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


def get_proxies():
    r = requests.get('http://127.0.0.1:8000/?types=0&count=10&country=国内')
    ip_ports = json.loads(r.text)
    import random
    size = random.randint(0, len(ip_ports) - 1)
    ip_ports_random = ip_ports[size]
    ip = ip_ports_random[0]
    port = ip_ports_random[1]
    proxies = {
        'http': 'http://%s:%s' % (ip, port),
        'https': 'http://%s:%s' % (ip, port)
    }
    return proxies


def fetch_content(url):
    response = fetch_page(url)
    if not response:
        return None
    page = response.content
    if page == '{}' or page == '':
        proxies = get_proxies()
        resp = fetch_page(url, proxies=proxies)
        page = resp.content
    return page


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}


def geturl(url):
    resp = fetch_page(url)
    res_j = json.loads(resp.content)
    res = res_j.get('data')
    if not res:
        proxies = get_proxies()
        resp = fetch_page(url, proxies=proxies)
        res_j = json.loads(resp.content)
        res = res_j.get('data')
    title_url = ['http://www.toutiao.com' + str(r.get('source_url')) for r in res]
    return title_url


def replace_img(text, srcs):
    """
    替换内容中的图片路径
    :param text: 文本内容
    :param srcs: 链表形式的图片url
    :return:
    """
    for src in srcs:
        new_path = 'http://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/' + src.split('/')[-1] + '.jpeg'
        text = text.replace(src, new_path)
    return text


def parse(area, url):
    title_url = geturl(url)
    print date_n, url
    jobs = [gevent.spawn(fetch_content, url) for url in title_url]
    gevent.joinall(jobs)
    for page in [job.value for job in jobs]:
        if not page:
            continue
        doc = etree.HTML(page)
        try:
            t = re.findall(r"title: '(.+)?'", page)[0]
            text_f = re.findall(r"source: '(.+)?'", page)[0]
            news_date = re.findall(r"time: '(.+)?'", page)[0].split(' ')[0]
            content = re.findall(r"content: '(.+)?'\.replace", page)[0].decode('utf-8')
            html = HTMLParser.HTMLParser()
            text = html.unescape(content)
            if news_date != date_n:
                continue
        except IndexError, e:
            continue
        text = filter_tags(text)
        imgs = re.findall(r'<img.+?src="(.+?)".+?>', text)
        text = replace_img(text, imgs)
        # text = str(MySQLdb.escape_string(text))  # 转译字符串
        img_show = []
        if len(imgs) == 1 or len(imgs) >= 3:  # 大于三张图可以考虑留一下。
            img_show = ','.join(
                ['https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/' + src.split('/')[-1] + '.jpeg' for src in
                 imgs])
            if len(imgs) > 3:
                img_show = ','.join(img_show.split(',')[0:3])
        if not img_show:
            img_show = None
        sql = r"""insert into _news_data (area, category_id, category_pid, title, news_date, text_f, img_show, text, em_teg) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        try:
            res = db.insert(sql, area, category_id, category_pid, t, news_date, text_f, img_show, text, em_teg)
                # res_sql = \
                #     'delete from _news_data  where newsid in (select newsid from (select  max(newsid) as newsid,count(title)' \
                #     ' as count from _news_data group by title having count > 1 order by count desc) as tab )'
                # db.execute(res_sql)
        except Exception as e:
            print e
        if imgs:
            for i in imgs:
                yield i


def run():
    with open('/home/spider/news_spider_1/src', 'w ') as fw:
        for area in areas:
            a = urllib.quote(area)
            url = 'http://www.toutiao.com/search_content/?offset=0&format=json&keyword={area}&autoload=true&count=100&cur_tab=1'.format(
                area=a)
            for i in parse(area, url):
                fw.write('http:' + i + '\n')

if __name__ == '__main__':
    run()
