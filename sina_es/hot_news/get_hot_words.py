#!/usr/bin/env python
# -- coding: utf-8 --
import requests
from lxml import etree
import jieba


headers = {
    'accept': 'textml,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.8',
    'cookie': '_user_id=1708281259017703024; _user_account=suqi;',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

def requests_post_shouye(data):
    '''推荐至首页的地址'''
    resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/index/add', data=data,
                         headers=headers)   #服务器
    # resp = requests.post('http://117.78.41.235:8080/cityparlor-web/cityparlor/cityparlor/index/add', data=data,
    #                      headers=headers)  # 本地
    return resp


def news_cut_outstop(news_text):
    stopwd = [line.strip().decode('utf-8') for line in open('hotword_stopwd.txt', 'rb').readlines()]
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

def get_hotwd_list():
    wangyi_keywd_set=wangyi_title_segset()
    souhu_keywd_set=souhu_title_segset()
    keywd_set=wangyi_keywd_set&souhu_keywd_set
    hotwd_list = list(keywd_set)
    return hotwd_list


def is_rec_firstpage(title):
    '''
    根据标题判断是否将本条新闻推荐至首页
    :param title: 新闻的标题字符串
    :return: flag返回为false则不推荐，返回为true则推荐
    '''
    flag=False
    hotwd_list=get_hotwd_list()
    inter_hotwd=[]
    for i in hotwd_list:
        if i in title:
            inter_hotwd.append(i)
    if inter_hotwd:
        flag=True
    return flag

# def firstpage_post(title):
#     '''
#     上传时用
#     flag为TRUE的情况下将新闻推至首页
#     :return:
#     '''
#     flag=is_rec_firstpage(title)
#     if flag==True:
        # 推荐至首页,代码示例如下，其中d为向后台上传时的字典
        # rec_data = {}
        # rec_data['area'] = 0
        # rec_data['title'] = d.get('title')
        # rec_data['source'] = d.get('source')
        # rec_data['isTop'] = 0
        # rec_data['isEssential'] = 0
        # rec_data['classify'] = d.get('classify')
        # rec_data['objId'] = json.loads(resp.content).get('retObj')
        # rec_data['objType'] = 'news'
        # rec_data['languageVersion'] = d.get('languageVersion')
        # rec_data['imageUrl'] = d.get('pics')
        # resp_shouye = requests_post_shouye(rec_data)
        # print
        # resp_shouye.content, d.get('title'), 'shouyetuijian', rec_data.get('area'), rec_data.get('languageVersion')



if __name__ == '__main__':
    flag=is_rec_firstpage(u'习近平同布特弗利卡总统互致贺电庆祝阿尔及利亚一号通信卫星发射成功')
    print(flag)
