#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from topic.get_topic_news import topic_news

#get_topic_news中topic_news类的使用测试及简单示例

topic_title_list = ['访华']
key_word = '特朗普'
topic_content_list = ['来华', '中国', '习近平', '国事访问']
model = topic_news(keywd=key_word, title_topic_list=topic_title_list, content_topic_list=topic_content_list)
res = model.data_get()
for title, content in res:
    topic_flag=model.is_topic_flag(title=title,content=content)
    if topic_flag:
        print('1:',title,topic_flag,'本新闻属于指定主题')
    else:
        print('2:',title,topic_flag)

