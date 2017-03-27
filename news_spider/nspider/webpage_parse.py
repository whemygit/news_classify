#!/usr/bin/env python
# -- coding: utf-8 --
import urlparse
import re

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def webpage_parse(area, content, src_url, category_pid):
        """
        获取子链接
        :param url_obj:
        :param html:
        :return:
        """
        href_list = re.findall(r'<a.*?href="(.+?)".*?>', content)
        tag_obj = src_url.split('/')
        if 'http' in src_url:
            tag_obj = tag_obj[3:]
        is_index = 0
        a_list = list()
        r_list = list()
        for href in href_list:
            index = 0
            tag_h = href.split('/')
            no_index = set(tag_h)
            no_list = list(no_index)
            if 'index' in href or 'default' in href or len(tag_h) == 1 or 'list' in href:
                continue
            if len(no_index) == 2 and '.' in no_list[1]:
                continue
            if tag_h[0] == '.' or tag_h[0] == '..':
                r_list.append(href)
            else:
                for tag in tag_h:
                    if not tag:
                        continue
                    if tag in tag_obj:
                        index += 1
                if index == len(tag_obj):
                    continue
                if index > is_index:
                    is_index = index
                    a_list = list()
                    a_list.append(href)
                elif index < is_index:
                    continue
                else:
                    a_list.append(href)
        if len(r_list) >= 7:
            res_list = r_list
        else:
            res_list = a_list
        return ['\x01'.join([str(category_pid), area, urlparse.urljoin(src_url, _url)])for _url in res_list]


if __name__ == '__main__':
    pass
