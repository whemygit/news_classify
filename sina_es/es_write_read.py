#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch.helpers import scan

reload(sys)
sys.setdefaultencoding("utf-8")

# es = Elasticsearch()
# es = Elasticsearch(hosts=["192.168.1.98:9200","192.168.1.26:9200","192.168.1.103:9200"])
# es = Elasticsearch(hosts=["117.78.60.108:9200"])
es = Elasticsearch(hosts=["192.168.1.97:9200","192.168.1.172:9200","192.168.1.254:9200"])

class es_store():
    def __init__(self,index_name,type_name):
        if es.indices.exists(index=index_name)==False:
            es.indices.create(index=index_name)
        self.index=index_name
        self.type=type_name
        self.bulk_actions=[]
        self.post_data_num=self.get_post_num()
        self.post_id_list=self.get_post_idlist()

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


    def get_bulk_action(self,spider_dict):
        resp_dict={"is_resp":0}
        spider_dict.update(resp_dict)
        self.bulk_actions.append({"_index":self.index,"_type":self.type,"_source":spider_dict})

    def bulk_put_data(self,bulk_actions):
        res = bulk(es, actions=bulk_actions)
        print res[0]

    def read_data(self):
        res = es.search(index=self.index, doc_type=self.type, body={"query": {"constant_score": {"filter": {"term":{"is_resp": 0}}}}})
        post_data=res["hits"]["hits"]
        return post_data


    def update_resp(self,id):
        '''
        根据id修改is_resp的字段值，默认为0,上传后修改为1
        :param id: for hit in self.post_data,id=hit["_id"]
        :return:
        '''
        res = es.update(index=self.index, doc_type=self.type, id=id, body={"doc": {"is_resp": 1}})
        print res['result']


    def get_post_num(self):
        '''
        获取待上传data的个数
        :return:
        '''
        post_data_num_query=es.search(index=self.index,doc_type=self.type,body={"query": {"constant_score": {"filter": {"term": {"is_resp": 0}}}}})

        post_data_num = post_data_num_query["hits"]["total"]
        return post_data_num


    def get_post_idlist(self):
        '''
        获取待上传data的id列表
        :return:
        '''

        query_res = es.search(index=self.index, doc_type=self.type, body={"size": self.post_data_num, "_source": ["title"],
                                                                          "query": {"constant_score": {
                                                                              "filter": {"term": {"is_resp": 0}}}}})

        post_res=query_res["hits"]["hits"]
        post_id_list=[]
        for i in post_res:
            post_id_list.append(i.get('_id'))
        return post_id_list

    def get_post_data_withid(self,id):
        post_dict=es.get(index=self.index,doc_type=self.type,id=id)
        post_data_dict= post_dict['_source']
        return post_data_dict



