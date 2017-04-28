#!/usr/bin/env python
# -- coding: utf-8 --
import requests


import sys

reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    resp = requests.get('http://news.artron.net/20170407/n921863.html')
    print resp.content