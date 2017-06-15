#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

c='https://img.huxiucdn.com/article/content/201512/08/1208338475.jpg'

a='http://img-proxy.huxiu.com/http://mmbiz.qpic.cn/mmbiz_jpg/l4sfibEYR5pWMia1ib0DILOicp1vj3cyBalia3QZxITGvD0Gia8yFeq0g474EbXrqPicdAChtkiaxNtwI50rO9jibdWmibwQ/0'
print  a.startswith('http://img-proxy')
print 'http://img-proxy' in c



# if __name__ == '__main__':
#     pass