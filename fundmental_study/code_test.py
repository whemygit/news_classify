#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass


# with open('D://myfile/bayestest/code.txt','r') as fin:
#     lines=fin.read()
#     print lines
#     decode_lines=lines.decode('iso-8859-15').encode('utf-8')
#     print decode_lines
#     # encode_lines=decode_lines.encode('utf-8')
#     # print encode_lines


#
import json
with open('D://myfile/output/article','r') as fr,open('D://myfile/output/article_out','w') as fw:                                  #spider输出为具有一个键的字典，值为列表
    for line in fr.readlines():
        news=json.loads(line)
        key=news.keys()[0]
        print key
        content=news.get(key)[5]
        fw.write(content)


