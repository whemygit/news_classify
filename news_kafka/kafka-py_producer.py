#!/usr/bin/env python
# -- coding: utf-8 --
from kafka import SimpleClient,SimpleProducer
import json

send_message={'a':1,'b':2}
client=SimpleClient("192.168.0.202:1936")
print client.topics

# producer=SimpleProducer(client)
# for i in range(2):
#     s=json.dumps(send_message).encode()
#     response=producer.send_messages("news", s)
#     print response[0].offset