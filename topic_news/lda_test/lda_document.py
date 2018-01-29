#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
import lda
import lda.datasets

def get_datas():
    x=lda.datasets.load_reuters()
    vocab=lda.datasets.load_reuters_vocab()
    titles=lda.datasets.load_reuters_titles()
    return x,vocab,titles
    # print(x.shape)
    # print(x.sum())
    # print(len(vocab))
    # print(title)

def model_build():
    x, vocab, titles=get_datas()
    model=lda.LDA(n_topics=10,n_iter=2000,random_state=1)
    model.fit(x)
    topic_word=model.topic_word_
    print(topic_word.shape)
    n_top_words = 8
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words + 1):-1]
        print('Topic {}: {}'.format(i, ' '.join(topic_words)))

    doc_topic=model.doc_topic_
    print(doc_topic.shape)
    # print(doc_topic)

    for n in range(20):
        topic_most_pr=doc_topic[n].argmax()
        print("doc:{} topic:{}".format(n,topic_most_pr))

    for n in range(20):
        topic_most_pr=doc_topic[n].argmax()
        print("{} topic:{}".format(titles[n],topic_most_pr))


x,vocab,titles=get_datas()
# print(x)
# print(vocab)
# print(type(vocab))
print(titles)
# model_build()
# x=np.array([2,1,4,5,3])
# print(np.argsort(x))
# print(x[np.argsort(x)])
# print(x[np.argsort(x)][::-1])
# print(x[np.argsort(x)][3:1:-1])
# print(x[np.argsort(x)][1:3:1])
# print(x[np.argsort(x)][:2:])

#
# print(np.argsort(-x))
# print(x[np.argsort(-x)])