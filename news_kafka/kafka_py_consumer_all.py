#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from kafka import KafkaConsumer
import json

consumer=KafkaConsumer("news",consumer_timeout_ms=10000,auto_offset_reset='earliest',bootstrap_servers=["192.168.0.202:1936"])

for msg in consumer:
    res=json.loads(msg[6])
    print msg[2],res
    print res['title']
msg_num= msg[2]       #msg数量
print 'msg_num: ',msg_num
