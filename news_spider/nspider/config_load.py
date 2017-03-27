#!/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import logging


class SpiderConf(object):
    """Class to store config info.

    Attributes:
        url_list_file:  The seed file which stores the request url list.
        output_directory:   The output data dir.
        max_depth:          The max crawl depth from the root url.
        crawl_interval:     The crawl request interval value.
        crawl_timeout:      The crawl request timeout value
        target_url:         The regex expression to store target url.
        thread_count:       The count limit for multi-threadings.
    """

    def __init__(self):
        self.url_list_file = "./urls"
        self.output_directory = "../output/article"
        self.crawl_interval = 1
        self.crawl_timeout = 5
        self.category_id = 1
        self.img_path = '../town/img/'
        self.category_pid = 11
        self.thread_count = 8
        self.stop_words = ['业务合作：', '经营许可证：', '我要评论', '许可证', '网站简介', '联系我们', '自治区网站', '客服热线：', '广告洽谈', '未经协议授权', '在线服务', '首 页', '受理范围', '联系电话', '办事服务', '网站检索功能', '免责声明']

    def conf_parse(self, conf):
        """Config parser"""
        conf_parser = ConfigParser.ConfigParser()
        try:
            conf_parser.read(conf)
        except ConfigParser.Error as e:
            logging.error("Fail to load conf(%s) as ConfigParser.Error: %s", conf, e)
            return "Fail"
        try:
            self.url_list_file = conf_parser.get("spider", "url_list_file")
            self.output_directory = conf_parser.get("spider", "output_directory")
            self.crawl_interval = int(conf_parser.get("spider", "crawl_interval"))
            self.crawl_timeout = int(conf_parser.get("spider", "crawl_timeout"))
            self.category_id = conf_parser.get("spider", "category_id")
            self.category_pid = conf_parser.get("spider", "category_pid")
            self.thread_count = int(conf_parser.get("spider", "thread_count"))
            self.stop_words = conf_parser.get("spider", "stop_words").split('\x01')
        except Exception as e:
            logging.error("Fail to parse conf as Exception:%s", e)
        return None
