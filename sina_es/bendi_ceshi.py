#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from es_write_read import es_store
reload(sys)
sys.setdefaultencoding("utf-8")
es_model=es_store(index_name="sina_news",type_name="sina_news_rec")

actions=[{"_index":"ts_index","_type":"ts_type","_source":{ "articleID" : "XHDK-A-1293-#fJ3", "userID" : 1,"postDate": "2017-01-01" }},
    {"_index":"ts_index","_type":"ts_type","_source":{"articleID" : "KDKE-B-9947-#kL5", "userID" : 1,"postDate": "2017-01-02" }},
    {"_index":"ts_index","_type":"ts_type","_source":{"articleID" : "JODL-X-1937-#pV7", "userID" : 2, "postDate": "2017-01-01" }},
    {"_index":"ts_index","_type":"ts_type","_source":{"articleID" : "QQPX-R-3956-#aD8", "userID" : 2, "postDate": "2017-01-02" }}]

def bulk_post():
    es=Elasticsearch()
    res=bulk(es,actions)
    print res

if __name__ == '__main__':
    bulk_post()