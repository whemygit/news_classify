#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from es_write_read import es_store
reload(sys)
sys.setdefaultencoding("utf-8")
es_model=es_store(index_name="sina_news",type_name="sina_news_rec")
if __name__ == '__main__':
    post_data=es_model.read_data()
    for i in post_data:
        es_model.update_resp(i.get("_id"))