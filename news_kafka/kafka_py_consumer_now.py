#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from kafka import KafkaConsumer
import json

consumer=KafkaConsumer("news",auto_offset_reset='latest',bootstrap_servers=["192.168.0.202:1936"])

for msg in consumer:
    res=json.loads(msg[6])
    print msg[2],res
