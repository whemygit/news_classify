#!/usr/bin/python
# coding:utf-8
import re
import urllib2, urllib, socket
import sys
import os
import time
import threading
import Queue

hds = {'User-Agent': 'chrome/28.0.1500.72', }


# proxy_h=urllib2.ProxyHandler({'http':'http://127.0.0.1:8087'})
# opener=urllib2.build_opener(proxy_h)
# urllib2.install_opener(opener)
def getHtml(url):
    page = urllib2.urlopen(urllib2.Request(url, None, hds)).read()  # 读取网页html源码
    return page


class getImgThread(threading.Thread):
    def __init__(self, imgUrl, fileName):
        threading.Thread.__init__(self)
        self.url = imgUrl
        self.fileName = fileName

    def run(self):
        mutex.acquire()
        print self.url
        mutex.release()
        try:
            urllib.urlretrieve(self.url, self.fileName)
        except IOError:
            time.sleep(1)


if __name__ == '__main__':
    socket.setdefaulttimeout(10)
    try:
        os.mkdir('/home/spider/rec_spider/img')
    except OSError, e:
        if e.errno == 17:  # 如果是文件已经存在，则不做任何操作
            pass
        else:  # 如果是其他异常，则打印出异常，并退出程序
            print e
            sys.exit()
    os.chdir('/home/spider/rec_spider/img')
    urls = []
    with open('/home/spider/rec_spider/src', 'r') as fr:
        urls = [src.strip() for src in fr.readlines()]
    mutex = threading.Lock()
    threads = []
    for URL in urls:  # 做一个遍历
        try:
            fileName = URL.split('/')[-1]  # 取文件名
            threads.append(getImgThread(URL, fileName))
        except Exception, e:
            pass
    for t in threads:
        if threading.activeCount() >= 500:
            time.sleep(5)
        t.start()
    for t in threads:
        t.join()
    print 'End'
