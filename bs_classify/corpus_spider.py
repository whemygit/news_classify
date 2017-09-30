#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from lxml import etree
import requests
import json
reload(sys)
sys.setdefaultencoding("utf-8")

data={
    "fullText":"",
    "pubDate":"",
    "infoClassCodes":"0105",
    "normIndustry":"01",
    "zoneCode":"",
    "fundSourceCodes":"",
    "poClass":"",
    "rangeType":"",
    "currentPage":"2"
}

headers={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"115",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie":"JSESSIONID=F7E37C53F942773E7AFEBD5615AB1DA8; Hm_lvt_5e642b7ea86f82ce1f7baa021d9b8809=1504602605; Hm_lpvt_5e642b7ea86f82ce1f7baa021d9b8809=1504602677",
    "Host":"www.chinabidding.com",
    "Origin":"http://www.chinabidding.com",
    "Referer":"http://www.chinabidding.com/search/proj.htm",
    # "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
}

def get_proxies():
    r = requests.get('http://127.0.0.1:8000/?types=0&count=5&country=国内')
    ip_ports = json.loads(r.text)
    import random
    size = random.randint(0, len(ip_ports) - 1)
    ip_ports_random = ip_ports[size]
    ip = ip_ports_random[0]
    port = ip_ports_random[1]
    proxies = {
        'http': 'http://%s:%s' % (ip, port),
        'https': 'http://%s:%s' % (ip, port)
    }
    return proxies


url="http://www.chinabidding.com/search/proj.htm"
def title_spider(industy_code,pagesize):
    resp=requests.post(url=url,data=get_data(industy_code,pagesize),headers=headers,proxies=get_proxies())
    # print resp.content
    detail=etree.HTML(resp.content)
    title_list=detail.xpath('//h5[@class="as-p-tit"]/span[2]/text()')
    with open('title_corpus','w') as fw:
        for i in title_list:
            print industy_code,i
            fw.write(industy_code+':'+i+'\n')


def get_data(industry_code,page_size):
    data_1 = {
        "fullText": "",
        "pubDate": "",
        "infoClassCodes": "0105",
        "normIndustry": str(industry_code),
        "zoneCode": "",
        "fundSourceCodes": "",
        "poClass": "",
        "rangeType": "",
        "currentPage":str(page_size)
    }
    # print data_1
    return data_1


industry_codes=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50']

if __name__ == '__main__':
    for i in industry_codes:
        for j in range(101):
            title_spider(i,j)

