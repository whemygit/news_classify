#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
from gensim import corpora
import lda

doc_list=[
    ['新春','备','年货','新年','联欢晚会','备'],
    ['新春','节目单','春节','联欢晚会','红火'],
    ['大盘','下跌','股市','散户'],
    ['下跌','股市','赚钱'],
    ['金猴','新春','红火','新年'],
    ['新车','新年','年货','新春'],
    ['股市','反弹','下跌'],
    ['股市','散户','赚钱'],
    ['新年','看','春节','联欢晚会'],
    ['大盘','下跌','散户']
]

# doc_list=[
#     '新春 备 年货 新年 联欢晚会',
#     '新春 节目单 春节 联欢晚会 红火',
#     '大盘 下跌 股市 散户',
#     '下跌 股市 赚钱',
#     '金猴 新春 红火 新年',
#     '新车 新年 年货 新春',
#     '股市 反弹 下跌',
#     '股市 散户 赚钱',
#     '新年 看 春节 联欢晚会',
#     '大盘 下跌 散户'
# ]

print(doc_list)
dictionary=corpora.Dictionary(doc_list)
print(dictionary)
print(dictionary.token2id)
print(len(dictionary))
print(len(doc_list))

row_num=len(doc_list)
col_num=len(dictionary)

bow_corpus=[dictionary.doc2bow(text) for text in doc_list]
print(bow_corpus)

doc_array=np.zeros((row_num,col_num),dtype=int)
# print(doc_array)




for i,j in enumerate(bow_corpus):
    for word_index,fre in j:
        doc_array[i][word_index]=fre

print(doc_array)



vocablist=[]
for k,v in dictionary.items():
    print(k,v,int(k),type(v))
    vocablist.append(v)
print(vocablist)

vocab=tuple(vocablist)
print(vocab)

model = lda.LDA(n_topics=5, n_iter=1500, random_state=1)
model.fit(doc_array)
topic_word = model.topic_word_
print(topic_word.shape)
n_top_words = 3
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words + 1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))

doc_topic = model.doc_topic_
print(doc_topic.shape)
# print(doc_topic)

for n in range(10):
    topic_most_pr = doc_topic[n].argmax()
    print("doc:{} topic:{}".format(n, topic_most_pr))