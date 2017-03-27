#!/usr/bin/env python
# -- coding: utf-8 --
import threading

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

url_record = set()
lock = threading.RLock()


def url_record_put(url):
    """
    put new url record int to the set
    :param url: The new url will be stored in the record.
    :return:
    """
    with lock:
        url_record.add(url)


def url_record_get(url):
    """
    get if the url exists in the record
    :param url:
    :return:
    """

    with lock:
        if url not in url_record:
            url = None
    return url


if __name__ == '__main__':
    pass
