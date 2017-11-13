#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from elasticsearch import Elasticsearch

reload(sys)
sys.setdefaultencoding("utf-8")
es = Elasticsearch()

class es_store():
    def __init__(self,index_name,type_name):
        if es.indices.exists(index=index_name)==False:
            es.indices.create(index=index_name)
        self.index=index_name
        self.type=type_name

    def is_exist(self,title):
        exist_flag=False
        res = es.search(index=self.index, doc_type=self.type, body={"query": {
            "constant_score": {"filter": {"match": {"title.keyword": title}}}}})
        if res['hits']['total']>0:
            exist_flag=True
        return exist_flag

    def put_data_es(self,spider_dict):
        resp_dict={"is_resp":0}
        doc_dict=spider_dict
        doc_dict.update(resp_dict)
        res = es.index(index=self.index, doc_type=self.type, body=doc_dict)
        print 'created:',res['created']

    # def read_data(self):
    #     res = es.search(index=self.index, doc_type=self.type, body={"query": {"match": {"resp": 0}}})
    #     post_data=res["hits"]["hits"]
    #     return post_data

    def read_data(self):
        res = es.search(index=self.index, doc_type=self.type, body={"query": {"constant_score": {"filter": {"term":{"is_resp": 0}}}}})
        post_data=res["hits"]["hits"]
        return post_data

    # #使用示例
    # def data_post(self):
    #     '''
    #     r['_source']返回要上传的字典
    #     :return:
    #     '''
    #     # post_data=self.read_data()
    #     for r in post_data:
    #         post_dict=r['_source']


    def update_resp(self,id):
        '''
        根据id修改is_resp的字段值，默认为0,上传后修改为1
        :param id: for hit in self.post_data,id=hit["_id"]
        :return:
        '''
        es=Elasticsearch()
        res = es.update(index=self.index, doc_type=self.type, id=id, body={"doc": {"is_resp": 1}})
        print res['result']




