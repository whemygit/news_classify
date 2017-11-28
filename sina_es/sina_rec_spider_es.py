#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import requests
from lxml import etree
import jieba
import time
import re
from es_write_read import es_store

reload(sys)
sys.setdefaultencoding("utf-8")

today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
yesterday=time.strftime('%Y-%m-%d',time.localtime(time.time()-86400))

#首先实例化es
es_model=es_store(index_name="sina_news",type_name="sina_news_rec")

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
    # 去掉尾注
    s = re.sub(r'<strong>本栏目.*?</strong>','',s)
    s = re.sub(r'<strong>新浪军事：最多军迷首选的军事门户！</strong>','',s)
    s = re.sub(r'<span .*?<strong>.*?</strong>：为了.*?关注。</span>','',s)
    return s

def replace_img(text, srcs):
    for src in srcs:
        new_path = 'http://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/' + src.split('/')[-1]
        text = text.replace(src, new_path)
    return text


def news_cut_outstop(news_text):
    stopwd=[line.strip().decode('utf-8') for line in open('/home/spider/sina_rec_es/stopw.txt','r').readlines()]
    # stopwd = [line.strip().decode('utf-8') for line in open('stopw.txt', 'r').readlines()]
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
        print keywd
        for title in title_url_dict:
            if keywd in title:
                # print keywd,title
                rec_news_dict.update({title_url_dict.get(title):title})
        keywd_list.remove(keywd)
    return rec_news_dict

def news_spider():
    rec_news_dict=recomend_news()
    for url in rec_news_dict:
        # print url
        'http://ent.sina.com.cn/s/m/2017-09-21/doc-ifymesii4778115.shtml'
        if url.startswith('http://slide') or url.startswith('http://video') or url.startswith('http://news') or url.startswith('http://sports') or url.startswith('http://ent'):
            # print url
            continue
        url_split=url.split('/')
        if today in url_split or yesterday in url_split:
            # print url
            if today in url_split:
                new_date=today
            else:
                new_date=yesterday
            try:
                new_title,new_content, imgs, img_show,new_source=news_detail_spider(url)
                print new_title,new_date,url
                yield new_title, new_date, new_source, new_content, imgs, img_show
            except:
                print 'no news available',url
                continue



def news_detail_spider(new_url):
    resp=requests.get(new_url)
    detail=etree.HTML(resp.content)
    try:
        new_title=detail.xpath('//*[@id="artibodyTitle"]/text()')[0]
    except:
        try:
            new_title = detail.xpath('//*[@id="main_title"]/text()')[0]
        except:
            new_title = detail.xpath('//h1[@class="main-title"]/text()')[0]

    #根据标题判断新闻是否已经存在，存在则不再重复抓取
    title_exist_flag=es_model.is_exist(new_title)
    if title_exist_flag==True:
        print "title already exist"
        return title_exist_flag
    else:
        new_content = etree.tostring(detail.xpath('//*[@id="artibody"]')[0], xml_declaration=True,
                                  encoding='utf-8')
        new_content=filter_tags(new_content)
        new_content = re.sub(r'<!--行情图 start-->[\s|\S]*?<!--行情图 end-->', '', new_content)
        new_content = re.sub(r'<!-- 引文 start -->[\s|\S]*?<!-- 引文 end -->', '', new_content)
        new_content = re.sub(r'<!--轮播 start-->[\s|\S]*?<!--直播推荐 end-->', '', new_content)
        new_content = re.sub(r'<!--港股大赛.*?start-->[\s|\S]*?<!--wapdump end-->', '', new_content)
        new_content = re.sub(r'<!-- 新浪财经直播 推广轮播 start -->[\s|\S]*?<!-- 新浪财经直播 推广轮播 end-->', '', new_content)
        new_content = re.sub(r'<p>[\s|\S]*?lcsds_icon.jpg[\s|\S]*?</p>', '', new_content)
        new_content = re.sub(r'<div>[\s|\S]*?icon01.png[\s|\S]*?</div>', '', new_content)
        new_content = re.sub(r'<img src=[\s|\S].*?usstocks0108.png[\s|\S].*?>', '', new_content)
        new_content = re.sub(r'<div><p>进入【新浪财经股吧】讨论</p></div>', '', new_content)
        new_content = re.sub(r'相关报道见.*?版', '', new_content)
        try:
            new_source=detail.xpath('//span[@class="source"]/a/text()')[0]
        except:
            new_source='新浪新闻'
        imgs=re.findall(r'<img.+?src="(.+?)".+?>', new_content)
        new_content=replace_img(new_content,imgs)
        img_show = []
        if len(imgs) == 1 or len(imgs) >= 3:  # 大于三张图可以考虑留一下。
            img_show = ','.join(
                ['https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/' + src.split('/')[-1] for src in
                 imgs])
            if len(imgs) > 3:
                img_show = ','.join(img_show.split(',')[0:3])
        if len(imgs)==2:
            img_show=['https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/' + src.split('/')[-1] for src in imgs][0]
        if not img_show:
            img_show = None
        return new_title,new_content,imgs,img_show,new_source


# def main():
#     '''
#     逐条上传至es
#     :return:
#     '''
#     spider_res=news_spider()
#     spider_dict={}
#     # 将抓取的数据存入es
#     # with open('/home/spider/sina_rec_es/src', 'w ') as fw:
#     with open('src', 'w ') as fw:
#         for new_title, new_date, new_source, new_content, imgs, img_show in spider_res:
#             spider_dict['title']=new_title
#             spider_dict['source']=new_source
#             spider_dict['content']=new_content
#             spider_dict['img_show']=img_show
#             spider_dict['new_date']=new_date
#             es_model.put_data_es(spider_dict)
#             print new_title,"store to es success"
#             #保存图片地址
#             for i in imgs:
#                 if i.startswith('//'):
#                     fw.write('http:'+i+'\n')
#                 else:
#                     fw.write(i+'\n')


def bulk_main():
    '''
    bulk批次上传数据至es
    :return:
    '''
    spider_res=news_spider()
    # 将抓取的数据存入es
    with open('/home/spider/sina_rec_es/src', 'w ') as fw:
    # with open('src', 'w ') as fw:
        for new_title, new_date, new_source, new_content, imgs, img_show in spider_res:
            spider_dict = {}
            spider_dict['title']=new_title
            spider_dict['source']=new_source
            spider_dict['content']=new_content
            spider_dict['img_show']=img_show
            spider_dict['new_date']=new_date
            #保存图片地址
            for i in imgs:
                if i.startswith('//'):
                    fw.write('http:'+i+'\n')
                else:
                    fw.write(i+'\n')
            #获取bulk_actons
            es_model.get_bulk_action(spider_dict)

    #批量放入
    # print es_model.bulk_actions
    es_model.bulk_put_data(es_model.bulk_actions)

if __name__ == '__main__':
    bulk_main()
    # main()


