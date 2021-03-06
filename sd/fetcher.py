#!/usr/bin/env python
# -- coding: utf-8 --

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

areas = ['北京市', '天津市', '上海市', '广州市', '深圳市', '石家庄市', '太原市', '呼和浩特市', '唐山市', '大同市', '包头市', '秦皇岛市', '阳泉市', '乌海市', '邯郸市',
         '长治市', '赤峰市', '邢台市', '晋城市', '呼伦贝尔市', '保定市', '朔州市', '通辽市', '张家口市', '忻州市', '乌兰察布市', '承德市', '吕梁市', '鄂尔多斯市', '沧州市',
         '晋中市', '巴彦淖尔市', '廊坊市', '临汾市', '衡水市', '运城市', '沈阳市', '长春市', '哈尔滨市', '大连市', '吉林市', '齐齐哈尔市', '鞍山市', '四平市', '牡丹江市',
         '抚顺市', '辽源市', '佳木斯市', '本溪市', '通化市', '大庆市', '丹东市', '白山市', '伊春市', '锦州市', '白城市', '鸡西市', '营口市', '松原市', '鹤岗市',
         '阜新市', '双鸭山市', '辽阳市', '七台河市', '盘锦市', '绥化市', '铁岭市', '黑河市', '朝阳市', '葫芦岛市', '南京市', '杭州市', '合肥市', '福州市', '南昌市',
         '济南市', '无锡市', '宁波市', '芜湖市', '厦门市', '赣州市', '青岛市', '徐州市', '温州市', '蚌埠市', '泉州市', '宜春市', '淄博市', '常州市', '绍兴市', '淮南市',
         '莆田市', '吉安市', '枣庄市', '苏州市', '湖州市', '马鞍山市', '漳州市', '上饶市', '东营市', '南通市', '嘉兴市', '淮北市', '龙岩市', '抚州市', '烟台市',
         '连云港市', '金华市', '铜陵市', '三明市', '九江市', '潍坊市', '淮安市', '衢州市', '安庆市', '南平市', '景德镇市', '济宁市', '盐城市', '台州市', '黄山市',
         '宁德市', '萍乡市', '泰安市', '扬州市', '丽水市', '阜阳市', '新余市', '威海市', '镇江市', '舟山市', '宿州市', '鹰潭市', '日照市', '泰州市', '滁州市', '滨州市',
         '宿迁市', '六安市', '德州市', '宣城市', '聊城市', '池州市', '临沂市', '亳州市', '菏泽市', '莱芜市', '郑州市', '武汉市', '长沙市', '开封市', '黄石市', '株洲市',
         '洛阳市', '十堰市', '湘潭市', '平顶山市', '荆州市', '衡阳市', '安阳市', '宜昌市', '邵阳市', '鹤壁市', '襄阳市', '岳阳市', '新乡市', '鄂州市', '张家界市',
         '焦作市', '荆门市', '益阳市', '濮阳市', '黄冈市', '常德市', '许昌市', '孝感市', '娄底市', '漯河市', '咸宁市', '郴州市', '三门峡市', '随州市', '永州市',
         '商丘市', '怀化市', '周口市', '驻马店市', '南阳市', '信阳市', '南宁市', '海口市', '深圳市', '柳州市', '三亚市', '珠海市', '桂林市', '儋州市', '汕头市',
         '梧州市', '三沙市', '佛山市', '北海市', '韶关市', '崇左市', '湛江市', '来宾市', '肇庆市', '贺州市', '江门市', '玉林市', '茂名市', '百色市', '惠州市', '河池市',
         '梅州市', '钦州市', '汕尾市', '防城港市', '河源市', '贵港市', '阳江市', '清远市', '东莞市', '中山市', '潮州市', '揭阳市', '云浮市', '成都市', '贵阳市',
         '昆明市', '拉萨市', '绵阳市', '六盘水市', '昭通市', '昌都市', '自贡市', '遵义市', '曲靖市', '山南市', '攀枝花市', '铜仁市', '玉溪市', '日喀则市', '泸州市',
         '毕节市', '普洱市', '林芝市', '德阳市', '安顺市', '保山市', '广元市', '丽江市', '遂宁市', '临沧市', '内江市', '乐山市', '资阳市', '宜宾市', '南充市', '达州市',
         '雅安市', '广安市', '巴中市', '眉山市', '西安市', '兰州市', '西宁市', '银川市', '乌鲁木齐市', '铜川市', '嘉峪关市', '海东市', '石嘴山市', '克拉玛依市', '宝鸡市',
         '金昌市', '吴忠市', '吐鲁番市', '咸阳市', '白银市', '固原市', '哈密市', '渭南市', '天水市', '中卫市', '汉中市', '酒泉市', '安康市', '张掖市', '商洛市',
         '武威市', '延安市', '定西市', '榆林市', '陇南市', '平凉市', '庆阳市']
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
    response = requests.get(url, timeout=10, headers=headers, proxies=proxies)
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
    r = requests.get('http://127.0.0.1:8000/?types=0&count=5&country=国内')
    ip_ports = json.loads(r.text)
    ip = ip_ports[0][0]
    port = ip_ports[0][1]
    proxies = {
        'http': 'http://%s:%s' % (ip, port),
        'https': 'http://%s:%s' % (ip, port)
    }
    return proxies


def fetch_content(url):
    response = fetch_page(url)
    page = response.content
    if page == '{}':
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
    title_url = ['http://www.toutiao.com/a' + str(r.get('id')) + '/' for r in res]
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
    print url
    jobs = [gevent.spawn(fetch_content, url) for url in title_url]
    gevent.joinall(jobs)

    for page in [job.value for job in jobs]:
        if not page:
            continue
        doc = etree.HTML(page)
        try:
            t = doc.xpath('//*[@id="article-main"]/h1/text()')[0].strip()
            r = doc.xpath('//*[@id="article-main"]/div[1]')[0]
            text_f = r.xpath('span[@class="src"]/text()')[0].strip()
            news_date = r.xpath('span[@class="time"]/text()')[0].strip().split(' ')[0]
            text = etree.tostring(doc.xpath('//*[@id="article-main"]/div[2]')[0], xml_declaration=True,
                                  encoding='utf-8')
            if news_date != date_n:
                continue
        except IndexError, e:
            continue
        text = filter_tags(text)
        imgs = re.findall(r'<img.+?src="(.+?)".+?/>', text)
        text = replace_img(text, imgs)
        text = str(MySQLdb.escape_string(text))  # 转译字符串
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
    with open('/home/spider/img_down/src', 'w ') as fw:
        for area in areas:
            a = urllib.quote(area)
            url = 'http://www.toutiao.com/search_content/?offset=0&format=json&keyword={area}&autoload=true&count=100&cur_tab=1'.format(
                area=a)
            for i in parse(area, url):
                fw.write(i + '\n')


if __name__ == '__main__':
    run()
