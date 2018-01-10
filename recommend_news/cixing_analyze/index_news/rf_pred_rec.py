#!/usr/bin/env python
# -- coding: utf-8 --
import numpy as np
from numpy import *
from snownlp import SnowNLP
from sklearn.externals import joblib
import jieba

# 禁推信源列表
ban_source=['头条寻人','房产情报站']

# 禁推词列表
ban_words=['减肥','瘦身','介绍','预售价']


def get_attr(title,content):
    '''
    :param title: 文章标题
    :param content: 文章内容
    :return: test_list，用于输入模型的参数特征值列表，依次为cnt_nper,cnt_ein,it_nfirst,tit_cnt_inter,tit_vin

    '''
    test_list = []
    title_s=SnowNLP(title)
    content_s=SnowNLP(content)
    t_tag=title_s.tags
    # 标题分词列表
    title_list = []
    # 标题词性列表
    title_tag_list=[]
    for w1,w2 in t_tag:
        # print (w1,w2)
        title_list.append(w1)
        title_tag_list.append(w2)

    # 标题的第一个词是否为名词
    if 'n' in str(title_tag_list[0]):
        title_nfirst=1
    else:
        title_nfirst=0


    # 标题是否含有动词
    if 'v' in title_tag_list or 'vn' in title_tag_list:
        title_vin=1
    else:
        title_vin=0


    # 内容关键词列表
    key_words = content_s.keywords(limit=10)
    k_n_len = 0

    # 内容关键词词性列表
    keywords_tag_list = []
    for i in key_words:
        for t,s in SnowNLP(i).tags:
            keywords_tag_list.append(s)
            if str(s).startswith('n'):
                k_n_len += 1

    # 内容关键字中名词占比
    cnt_nper = k_n_len / float(len(keywords_tag_list))

    # 内容关键字中是否含有标点符号等标注词性为e的项
    if 'e' in keywords_tag_list:
        cnt_ein=1
    else:
        cnt_ein=0



    # 标题与内容关键词是否有交集
    if list(set(title_list) & set(key_words)):
        tit_cnt_inter = 1
    else:
        tit_cnt_inter= 0

    test_list.append(cnt_nper)
    test_list.append(cnt_ein)
    test_list.append(title_nfirst)
    test_list.append(tit_cnt_inter)
    test_list.append(title_vin)
    # print (test_list)
    return test_list

def predict_rec_flag(title,content,source):
    '''

    :param title: 文章标题
    :param content: 文章内容
    :param source: 文章来源
    :return: rec_flag,返回为TRUE则推荐，返回为FALSE则不推荐
    '''
    test_data = get_attr(title=title, content=content)
    test_data = np.array(test_data).reshape(1, -1)
    rf_load = joblib.load('rec_model.m')
    # print('模型预测结果，1表示推荐，0表示不推荐：',rf_load.predict(test_data))
    if rf_load.predict(test_data)[0]==1:
        rec_flag=True
    # 如果source在ban_source内，则不推荐
    if source in ban_source:
        rec_flag=False

    # 如果标题中含有在ban_word内的词，则不推荐
    title_jieba_list=jieba.cut(title,cut_all=False)
    if list(set(title_jieba_list) & set(ban_words)):
        rec_flag=False
    print ('rec_flag:',rec_flag)
    return rec_flag


# 使用示例

# title='双鸭山市人民检察院对犯罪嫌疑人王金祥受贿案决定逮捕'
# content='''&lt;!--?xml version='1.0' encoding='utf-8'?--&gt;&lt;div&gt;&lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/1c5f00002030db77997d.jpeg&quot;&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;王金祥受贿案，于2016年9月6日双鸭山市人民检察院决定逮捕。&lt;/p&gt;&lt;/div&gt;'''
# source='房产情报站'

title='减肥成功'
content='''&lt;div&gt;&lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/3a0200045f5b0c277ccb.jpeg&quot;   alt=&quot;明日土拍，7幅地起拍总价超55亿！&quot; inline=&quot;0&quot;&gt;&lt;/p&gt;&lt;p&gt;时间：2017年9月15日9:30&lt;/p&gt;&lt;p&gt;地点：厦门市湖里区云顶北路842号厦门市政务服务中心一层新闻发布厅&lt;/p&gt;&lt;p&gt;&lt;strong&gt;地块信息&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;经济指标&lt;/p&gt;&lt;p&gt;（点击图片可查看大图）&lt;/p&gt;&lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/39ff00048b6271820f23.jpeg&quot;   alt=&quot;明日土拍，7幅地起拍总价超55亿！&quot; inline=&quot;0&quot;&gt;&lt;/p&gt;&lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/39ff00048b619f905de1.jpeg&quot;   alt=&quot;明日土拍，7幅地起拍总价超55亿！&quot; inline=&quot;0&quot;&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;地块详情&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;位置图&lt;/p&gt;&lt;p&gt;&lt;strong&gt;地块区位图&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/3a0400029d25e35c5cb4.jpeg&quot;   alt=&quot;明日土拍，7幅地起拍总价超55亿！&quot; inline=&quot;0&quot;&gt;&lt;/p&gt;&lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/3a01000472f212295264.jpeg&quot;   alt=&quot;明日土拍，7幅地起拍总价超55亿！&quot; inline=&quot;0&quot;&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;&clubs; 地块信息&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;2017TP04&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;地块位置：同安区同安新城12-14片区通福路与滨海旅游路交叉口西南侧(A地块)&lt;/p&gt;&lt;p&gt;容积率：&lt;strong&gt;2.4&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;建筑限高&lt;strong&gt; 18-60米&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;2017TP05&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;位置：同安区同安新城12-14片区通福路与滨海旅游路交叉口西南侧(B地块)&lt;/p&gt;&lt;p&gt;容积率：&lt;strong&gt;2.3&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;建筑限高 &lt;strong&gt;18-60米&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;&clubs; 周边项目&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;融信地块 &lt;strong&gt;去配建楼面价33532元/㎡&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;保利地块 &lt;strong&gt;去配建楼面价34759&lt;/strong&gt;&lt;strong&gt;元/㎡&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;禹洲地块 &lt;strong&gt;楼面价31519&lt;/strong&gt;&lt;strong&gt;元/㎡&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;融信铂悦湾&lt;strong&gt; 售价约45000&lt;/strong&gt;&lt;strong&gt;元/㎡&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;地块区位图&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/3a0000047e8fb9b1fdaa.jpeg&quot;   alt=&quot;明日土拍，7幅地起拍总价超55亿！&quot; inline=&quot;0&quot;&gt;&lt;/p&gt;&lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/3a01000472f357c32216.jpeg&quot;   alt=&quot;明日土拍，7幅地起拍总价超55亿！&quot; inline=&quot;0&quot;&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;&clubs; 地块信息&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;X2017P02&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;地块位置：翔安区13-06下潭尾南片区翔安大道与亭洋路交叉口西北侧（B-06）&lt;/p&gt;&lt;p&gt;容积率：&lt;strong&gt;2.4&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;建筑限高&lt;strong&gt; &amp;gt;18米&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;X2017P03&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;位置：翔安区13-06下潭尾南片区翔安大道与亭洋路交叉口西北侧（B-07）&lt;/p&gt;&lt;p&gt;容积率：&lt;strong&gt;2.4&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;建筑限高&lt;strong&gt; 18-60米&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;X2017P04&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;位置：翔安区13-06下潭尾南片区翔安大道与亭洋路交叉口西北侧（B-08）&lt;/p&gt;&lt;p&gt;容积率：&lt;strong&gt;2&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;建筑限高&lt;strong&gt; &amp;gt;18米&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;X2017P05&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;位置：翔安区13-06下潭尾南片区翔安大道与亭洋路交叉口西北侧（B-09）&lt;/p&gt;&lt;p&gt;容积率：&lt;strong&gt;2.4&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;建筑限高&lt;strong&gt; &amp;gt;18米&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;&clubs; 周边项目&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;首开领翔上郡：&lt;strong&gt;售价约&lt;/strong&gt;&lt;strong&gt;29000元/㎡&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;地块区位图&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/3a0000047ee693a85ae4.jpeg&quot;   alt=&quot;明日土拍，7幅地起拍总价超55亿！&quot; inline=&quot;0&quot;&gt;&lt;/p&gt;&lt;p&gt;&lt;img src=&quot;https://cityparlor.oss-cn-beijing.aliyuncs.com/news/img/39fa0004858336df7a26.jpeg&quot;   alt=&quot;明日土拍，7幅地起拍总价超55亿！&quot; inline=&quot;0&quot;&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;&clubs; 地块信息&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;地块位置：集美区11-11集美新城片区杏锦路与海翔大道交叉口东北侧&lt;/p&gt;&lt;p&gt;容积率：&lt;strong&gt;2.8&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;建筑限高&lt;strong&gt; &amp;gt;18米&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;&clubs; 周边项目&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;国贸天悦：&lt;strong&gt;新品待售&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;中交和美新城：&lt;strong&gt;新品待售&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;莲花首岸：&lt;strong&gt;售价约&lt;/strong&gt;&lt;strong&gt;37800元/㎡ &lt;/strong&gt;&lt;/p&gt;&lt;p&gt;本次公开出让地块均采用&lt;strong&gt;&ldquo;限地价、竞配建&rdquo;&lt;/strong&gt;方式拍卖出让，不设拍卖底价。当拍卖竞价达到竞价上限价格时，不再接受更高报价，转为竞报无偿移交政府的居住建筑面积（以下简称&ldquo;竞配建面积&rdquo;）。&lt;/p&gt;&lt;p&gt;每次竞报竞配建面积应不少于&lt;strong&gt;500平方米&lt;/strong&gt;，竞报竞配建面积最高者为竞得人。成交土地出让金即为竞价上限价格。关于竞配建面积移交要求详见出让文件中的出让合同。&lt;/p&gt;&lt;p&gt;图文 / 厦门地产资讯&lt;/p&gt;&lt;p&gt;版权 / 克而瑞&lt;/p&gt;&lt;/div&gt;'''
source='房产'


predict_rec_flag(title=title,content=content,source=source)