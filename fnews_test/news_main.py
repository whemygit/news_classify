#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

# #转换为json数据
# import json
# import re
#
# with open('D:/gitcode/mypython/news_spider/output/article', 'r') as fr, open('D://gitcode/mypython/news_spider/output/article_out', 'w') as fw:
#     for line in fr.readlines():
#         line_json = json.loads(line)
#         key = line_json.keys()[0]
#         info = line_json.get(key)[5]
#         text = re.sub('<.*?>', '', info)
#         text1=re.sub("&#13;","",text)
#         text2 = re.sub("\n", "", text1)
#         fw.write(text2+"\n")


# #通篇提取关键词
# from uf import util
# util.seg_extract('D://gitcode/mypython/fnews_test/news_from_json',"D://gitcode/mypython/fnews_test/keywd_seg.txt", False)
#
# #去停用词留关键词分词模块
# from uf import fenci
# fenci.keyoutstop_cut_toline('D://gitcode/mypython/fnews_test/news_from_json',"D://gitcode/mypython/fnews_test/each_keyoutstop_fenci_result","D:\gitcode\mypython\jieba1\stopw.txt","D://gitcode/mypython/fnews_test/keywd_seg.txt")
#
# #lda模型构建模块
# from lda1 import lda_topic_func_output
#
# lda_topic_func_output.lda_topic_tf(infile='D://gitcode/mypython/fnews_test/each_keyoutstop_fenci_result', outputfile1='D://gitcode/mypython/fnews_test/lda_output1', n_topics=10)
#
# from uf import lda_topic_func
# lda_topic_func.lda_topic_tf(infile='D://gitcode/mypython/fnews_test/each_keyoutstop_fenci_result',n_topics=10)



#依据负面词二分新闻为正负面两个文件
from uf import fenci
fenci.srchnega_eachnews_toline("D://gitcode/mypython/news_spider/output/article_out","D://gitcode/mypython/news_spider/output/article_neg",\
                               "D://gitcode/mypython/news_spider/output/article_pos","D://myfile/negative")

