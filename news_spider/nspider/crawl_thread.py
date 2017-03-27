#!/bin/python
# -*- coding: utf-8 -*-

import threading
import Queue
import logging
import time
import traceback
import re

import webpage_urlopen
import webpage_parse
import webpage_save
import url_record


class ThreadCrawl(threading.Thread):
    """ Thread to crawl webpage.

    Attributes:
        url_queque: The queue stored request urls.
        conf:       Spider config info
    """

    def __init__(self, url_queue, spider_conf):
        threading.Thread.__init__(self)
        self.url_queue = url_queue
        self.conf = spider_conf

    def run(self):
        while True:
            _url, depth = self.url_queue.get()
            category_pid = 0
            try:
                category_pid, area, url = _url.split('\x01')
            except ValueError:
                area, url = _url.split('\x01')
            url = url.strip()
            area = area.strip()
            # url record repeatation check
            if url_record.url_record_get(url) is not None:
                self.url_queue.task_done()
                continue
            logging.info("ThreadCrawl url(%s) with threading:%s.", url, threading.current_thread())

            # webpage_urlopen, charset detect, decode/encode
            content = webpage_urlopen.webpage_urlopen(url, self.conf.crawl_timeout)
            if content is not None:
                # webpage_save which match the target_url
                if category_pid != 0:
                    # area, html, url, output, category_id, category_pid
                    res = webpage_save.save_file(area, content, url, self.conf.output_directory, self.conf.category_id,
                                                 category_pid, self.conf.img_path, self.conf.stop_words)
                    if res is not None:
                        self.url_queue.task_done()
                        continue
                    print "Succ to save url: ", url, " in Threading:", threading.current_thread(), 'category_pid:', category_pid

                # webpage_parse
                else:
                    sub_urls = []
                    try:
                        # 解析下一页的url  是下一页就添加二级标签
                        category_pid = self.conf.category_pid
                        sub_urls = webpage_parse.webpage_parse(area, content, url, category_pid)
                        logging.info("sub_urls: %s, category_pid: %s", sub_urls, category_pid)
                    except Exception as e:
                        logging.error("Fail to parse content of url(%s) as Exception:%s", url, e)
                        print traceback.print_exc(e)

                    # extend the url_queue with new sub_urls
                    for sub_url in sub_urls:
                        # url record repeatation check
                        if url_record.url_record_get(sub_url) is not None:
                            continue
                        self.url_queue.put([sub_url, depth + 1])
                print "Succ to crawl url: ", url, " in Threading:", threading.current_thread()
                url_record.url_record_put(url)
            self.url_queue.task_done()
            time.sleep(self.conf.crawl_interval)


def crawl_thread_control(urls, spider_conf):
    """Function to control the crawler threadings.

    Args:
        urls:           The url list to be crawled.
        spider_conf:    Spider conf object.
    """

    init_depth = 0
    url_queue = Queue.Queue()
    for url in urls:
        url_queue.put([url, init_depth])
    for i in xrange(spider_conf.thread_count):
        t = ThreadCrawl(url_queue, spider_conf)
        t.setDaemon(True)
        t.start()

    cur_ths = threading.enumerate()

    url_queue.join()

    cur_ths = threading.enumerate()
    logging.info("All multi-threading crawling works have been done.")
