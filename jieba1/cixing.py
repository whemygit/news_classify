#encoding=utf-8
import jieba.posseg as pseg
words=pseg.cut("我爱北京天安门")
for w in words:
    print w.word,w.flag