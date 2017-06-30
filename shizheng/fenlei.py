#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import re
import time
import json

import requests
from lxml import etree
import torndb
import gevent
from gevent import monkey

reload(sys)
sys.setdefaultencoding("utf-8")

for i in range(1,7):
    data={'pid':i}
    resp=requests.post('https://cms.loongscity.com/cityparlor-web/cityparlor/cityparlor/town/category/list',data=data)
    content=resp.content
    ret=json.loads(content)
    info=ret.get('retObj')
    for d in info:
        id=d.get('id')
        pid=d.get('pid')
        title=d.get('title')
        print pid,id,title
    print '\n'


#
# if __name__ == '__main__':
#     pass