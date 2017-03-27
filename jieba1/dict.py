#encoding=utf-8
import sys
sys.path.append("../")
import jieba

test_sent = "李小福是创新办主任也是云计算方面的专家;"
words=jieba.cut(test_sent)
for w in words:
    print w


jieba.load_userdict("userdict.txt")
import jieba.posseg as pseg
result = pseg.cut(test_sent)
for w in result:
    print w.word, "/", w.flag, ", ",


