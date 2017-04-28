#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import time
import re
import urllib
import json
import requests
from lxml import etree

reload(sys)
sys.setdefaultencoding("utf-8")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

# now_date = getdate()

date_n = time.strftime("%Y-%m-%d", time.localtime(time.time()))


def geturl(url):
    resp = requests.get(url, timeout=5, headers=headers)
    res_j = json.loads(resp.content)
    res = res_j.get('data')
    title_url = [(r.get('title'), 'http://www.toutiao.com/a' + str(r.get('id')) + '/') for r in res]
    return title_url


def get_up_resp(data):
    resp = requests.post('http://192.168.0.225:8080/cityparlor-web/cityparlor/cityparlor/channel/news/save', data=data)
    print resp.content


def filter_tags(htmlstr):
    """
    清洗和过滤标签
    :param htmlstr: 页面筛选后的html代码块
    :return: 返回处理后的带标签内容
    """
    # 替换p标签
    s = re.sub(r'<p.*?>', '<p>', htmlstr)
    # 替换div
    s = re.sub(r'<div.*?>', '<div>', s)
    # 替换img属性
    s = re.sub(r'img_width="\d+"', '', s)
    s = re.sub(r'img_height="\d+"', '', s)
    # 处理script标签
    s = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', '', s)
    s = re.sub(r'<\s*script[^>]*>', '', s)
    # 去掉a标签
    s = re.sub(r'<a.*?>', '', s)
    s = re.sub(r'</a>', '', s)
    return s


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


def get_resp(url, celebrity_id, fun, type_id):
    title_url = geturl(url)
    for t, u in title_url:
        try:
            resp = requests.get(u, timeout=5, headers=headers)
        except Exception, e:
            print(u)
        if resp.url == u and resp.status_code == 200:
            doc = etree.HTML(resp.content)
            try:
                text = etree.tostring(doc.xpath('//*[@id="article-main"]/div[2]')[0], xml_declaration=True,
                                      encoding='utf-8')
                # if now_date != update:
                #     print area, update
                #     break
            except IndexError, e:
                continue
            text = filter_tags(text)
            imgs = re.findall('<img.+?src="(.+?)".+?/>', text)
            text = replace_img(text, imgs)
            img_show = ''
            classify = 1
            if len(imgs) == 1 or len(imgs) >= 3:  # 大于三张图可以考虑留一下。
                img_show = ','.join(
                    ['https://cityparlor.oss-cn-beijing.aliyuncs.com/sd_yd_img/' + src.split('/')[-1] + '.jpeg' for src in
                     imgs])
                if len(imgs) == 1:
                    classify = 2
                if len(imgs) > 3:
                    img_show = ','.join(img_show.split(',')[0:3])
            if img_show:
                info_d = dict()
                info_d['title'] = t
                info_d['content'] = text
                info_d['celebrityId'] = celebrity_id
                info_d['typeId'] = type_id
                info_d['fun'] = fun
                info_d['pic'] = img_show
                info_d['isNewRecord'] = True
                info_d['isTop'] = 0
                info_d['isEssential'] = 0
                info_d['recommend'] = 0
                info_d['classify'] = classify
                get_up_resp(info_d)
                for i in imgs:
                    yield i
                        # img_name = i.split('/')[-1].encode('utf-8')
                        # img_path = '../img/' + img_name + '.jpg'
                        # get_img_s(i, img_path)


def run():
    with open('pic_sy', 'w ') as fw, open('ml', 'r') as fr:
        for line in fr.readlines():
            name, p_id, _fun, l_id = line.split('\x01')
            a = urllib.quote(name)
            url = 'http://www.toutiao.com/search_content/?offset=0&format=json&keyword={area}&autoload=true&count=50&cur_tab=1'.format(
                area=a)
            print name, url
            for n in get_resp(url, p_id, _fun, l_id):
                fw.write(n + '\n')


if __name__ == '__main__':
    run()
