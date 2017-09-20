#!/usr/bin/env python
# -- coding: utf-8 --
import requests
from lxml import etree
import time
import MySQLdb
import torndb
import re

import sys
import json

reload(sys)
sys.setdefaultencoding("utf-8")
areas_in = ['北京市', '天津市', '上海市', '广州市', '深圳市', '石家庄市', '太原市', '呼和浩特市', '唐山市', '大同市', '包头市', '秦皇岛市', '阳泉市', '乌海市', '邯郸市',
            '长治市', '赤峰市', '邢台市', '晋城市', '呼伦贝尔市', '保定市', '朔州市', '通辽市', '张家口市', '忻州市', '乌兰察布市', '承德市', '吕梁市', '鄂尔多斯市',
            '沧州市',
            '晋中市', '巴彦淖尔市', '廊坊市', '临汾市', '衡水市', '运城市', '沈阳市', '长春市', '哈尔滨市', '大连市', '吉林市', '齐齐哈尔市', '鞍山市', '四平市',
            '牡丹江市',
            '抚顺市', '辽源市', '佳木斯市', '本溪市', '通化市', '大庆市', '丹东市', '白山市', '伊春市', '锦州市', '白城市', '鸡西市', '营口市', '松原市', '鹤岗市',
            '阜新市', '双鸭山市', '辽阳市', '七台河市', '盘锦市', '绥化市', '铁岭市', '黑河市', '朝阳市', '葫芦岛市', '南京市', '杭州市', '合肥市', '福州市', '南昌市',
            '济南市', '无锡市', '宁波市', '芜湖市', '厦门市', '赣州市', '青岛市', '徐州市', '温州市', '蚌埠市', '泉州市', '宜春市', '淄博市', '常州市', '绍兴市',
            '淮南市',
            '莆田市', '吉安市', '枣庄市', '苏州市', '湖州市', '马鞍山市', '漳州市', '上饶市', '东营市', '南通市', '嘉兴市', '淮北市', '龙岩市', '抚州市', '烟台市',
            '连云港市', '金华市', '铜陵市', '三明市', '九江市', '潍坊市', '淮安市', '衢州市', '安庆市', '南平市', '景德镇市', '济宁市', '盐城市', '台州市', '黄山市',
            '宁德市', '萍乡市', '泰安市', '扬州市', '丽水市', '阜阳市', '新余市', '威海市', '镇江市', '舟山市', '宿州市', '鹰潭市', '日照市', '泰州市', '滁州市',
            '滨州市',
            '宿迁市', '六安市', '德州市', '宣城市', '聊城市', '池州市', '临沂市', '亳州市', '菏泽市', '莱芜市', '郑州市', '武汉市', '长沙市', '开封市', '黄石市',
            '株洲市',
            '洛阳市', '十堰市', '湘潭市', '平顶山市', '荆州市', '衡阳市', '安阳市', '宜昌市', '邵阳市', '鹤壁市', '襄阳市', '岳阳市', '新乡市', '鄂州市', '张家界市',
            '焦作市', '荆门市', '益阳市', '濮阳市', '黄冈市', '常德市', '许昌市', '孝感市', '娄底市', '漯河市', '咸宁市', '郴州市', '三门峡市', '随州市', '永州市',
            '商丘市', '怀化市', '周口市', '驻马店市', '南阳市', '信阳市', '南宁市', '海口市', '深圳市', '柳州市', '三亚市', '珠海市', '桂林市', '儋州市', '汕头市',
            '梧州市', '三沙市', '佛山市', '北海市', '韶关市', '崇左市', '湛江市', '来宾市', '肇庆市', '贺州市', '江门市', '玉林市', '茂名市', '百色市', '惠州市',
            '河池市',
            '梅州市', '钦州市', '汕尾市', '防城港市', '河源市', '贵港市', '阳江市', '清远市', '东莞市', '中山市', '潮州市', '揭阳市', '云浮市', '成都市', '贵阳市',
            '昆明市', '拉萨市', '绵阳市', '六盘水市', '昭通市', '昌都市', '自贡市', '遵义市', '曲靖市', '山南市', '攀枝花市', '铜仁市', '玉溪市', '日喀则市', '泸州市',
            '毕节市', '普洱市', '林芝市', '德阳市', '安顺市', '保山市', '广元市', '丽江市', '遂宁市', '临沧市', '内江市', '乐山市', '资阳市', '宜宾市', '南充市',
            '达州市',
            '雅安市', '广安市', '巴中市', '眉山市', '西安市', '兰州市', '西宁市','乌鲁木齐市', '铜川市', '嘉峪关市', '海东市', '石嘴山市', '克拉玛依市',
            '宝鸡市',
            '金昌市', '吴忠市', '吐鲁番市', '咸阳市', '白银市', '固原市', '哈密市', '渭南市', '天水市', '中卫市', '汉中市', '酒泉市', '安康市', '张掖市', '商洛市',
            '武威市', '延安市', '定西市', '榆林市', '陇南市', '平凉市', '庆阳市', '湘西土家族苗族自治州', '神农架林区', '天门市', '潜江市', '仙桃市',
            '积石山保安族东乡族撒拉族自治县', '广河县', '永靖县', '东乡族自治县', '和政县', '康乐县', '临夏县',
            '临夏市', '日喀则地区', '黔南布依族苗族自治州', '临高县', '澄迈县', '屯昌县', '定安县', '迪庆藏族自治州', '中沙群岛的岛礁及其海域', '南沙群岛', '西沙群岛',
            '琼中黎族苗族自治县', '保亭黎族苗族自治县', '陵水黎族自治县', '乐东黎族自治县', '昌江黎族自治县', '白沙黎族自治县', '万宁市', '文昌市', '琼海市', '五指山市', '东方市',
            '大理白族自治州', '海北藏族自治州', '黔东南苗族侗族自治州', '山南地区', '怒江傈僳族自治州', '兴安盟', '西双版纳傣族自治州', '海东地区', '德宏傣族景颇族自治州', '昌都地区',
            '桐乡市', '海西蒙古族藏族自治州', '锡林郭勒盟', '黔西南布依族苗族自治州', '凉山彝族自治州', '重庆市', '双阳区', '南关区', '朝阳区', '宽城区', '绿园区', '二道区',
            '农安县', '毕节地区', '榆树市', '九台市', '高新技术产业开发区', '德惠市', '经济技术开发区', '汽车产业开发区', '甘南藏族自治州', '净月旅游开发区', '文山壮族苗族自治州',
            '玉树藏族自治州', '铜仁地区', '济源市', '甘孜藏族自治州', '恩施土家族苗族自治州', '红河哈尼族彝族自治州', '阿坝藏族羌族自治州', '果洛藏族自治州', '大兴安岭地区', '荷泽市',
            '林芝地区', '海南藏族自治州', '楚雄彝族自治州', '延边朝鲜族自治州', '阿里地区', '阿拉善盟', '黄南藏族自治州', '那曲地区', '银川', '阳朔', '乌鲁木齐', '昌吉回族自治州']
areas = []
text_f = '中国国际招标网'

data = {
    'fullText': '太原',
    'pubDate': 4,
    'infoClassCodes': '0105',
    'normIndustry': '',
    'zoneCode': '',
    'fundSourceCodes': '',
    'poClass': '',
    'rangeType': '',
    'currentPage': 1
}
mysql = {
    "host": "119.57.93.42",
    "port": "3306",
    "database": "spider",
    "password": "zhongguangzhangshi",
    "user": "bigdata",
    "charset": "utf8"
}
db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))
date_n = time.strftime("%Y-%m-%d", time.localtime(time.time()))


# resp = requests.post('http://www.chinabidding.com/search/proj.htm', data=data)
# print resp.content

def get_proxies():
    r = requests.get('http://127.0.0.1:8000/?types=0&count=5&country=国内')
    ip_ports = json.loads(r.text)
    print ip_ports
    ip = ip_ports[0][0]
    port = ip_ports[0][1]
    proxies = {
        'http': 'http://%s:%s' % (ip, port),
        'https': 'http://%s:%s' % (ip, port)
    }
    return proxies


def get_page_url(area):
    _fullText = area
    _currentPage = 1
    while True:
        data['currentPage'] = _currentPage
        data['fullText'] = _fullText
        try:
            resp = requests.post('http://www.chinabidding.com/search/proj.htm', data=data, timeout=5)
        except requests.ConnectionError:
            time.sleep(1)
            proxies = get_proxies()
            resp = requests.post('', data=data, timeout=5, proxies=proxies)
        except Exception as e:
            print e
            continue
        doc = etree.HTML(resp.content)
        page_doc = doc.xpath('//ul[@class="as-pager-body"]/li/a/@href')
        time.sleep(1)
        if len(page_doc) < 10 or _currentPage >= 3:
            print len(page_doc)
            break
        for d in page_doc:
            src = d
            res = get_page_info(area, src)
            if res == 'next':
                break
        _currentPage += 1


def get_page_info(area, src):
    time.sleep(1)
    try:
        resp = requests.get(src, timeout=5)
    except requests.ReadTimeout:
        return
    except Exception as e:
        return
    doc = etree.HTML(resp.content)
    title = doc.xpath('//active[@class="title"]/h1/text()')[0]
    date = doc.xpath('//active[@class="title"]/em/text()')[0].split(' ')[0]
    if date != date_n:
        return 'next'
    info = etree.tostring(doc.xpath('//section')[0], xml_declaration=True, encoding='utf-8')
    tel = re.findall(r'联系电话.*?(\d{11})', info)
    tel_z = re.findall(r'联系电话.*?(\d{3,4}-\d{7,8}[-\d{3,4}]?)', info)
    _tel = tel + tel_z
    if not tel and not tel_z:
        tel = re.findall(r'\d{11}', info)
        tel_z = re.findall(r'\d{3,4}-\d{7,8}', info)
        _tel = tel + tel_z
    call = ','.join(set([t for t in _tel]))
    _date = get_end_date(info)
    info = str(MySQLdb.escape_string(info))
    info = info.replace('\\n','')
    try:
        save_to_mysql(title, text_f, info, area, src, call, date, _date)
    except Exception as e:
        print e

def get_end_date(info):
    _date = re.findall(r'开标时间.*?(\d+)年(\d+)月(\d+)', info)
    if not _date:
        _date = re.findall(r'开标时间.*?(\d+)-(\d+)-(\d+)', info)
    if not _date:
        _date = re.findall(r'截止.*?(\d+)-(\d+)-(\d+)', info)
    if not _date:
        _date = re.findall(r'截止.*?(\d+)年(\d+)月(\d+)', info)
    if _date:
        _date = '-'.join(_date[0])
    else:
        _date = ''
    return _date


def save_to_mysql(title, text_f, text, city, handling, tel, startDate, endDate):
    sql = r"""insert into business_opportunity_chinabs (title, text_f, text, city, handling, tel, startDate, endDate) values (%s,%s,%s,%s,%s,%s,%s,%s)"""
    res = db.insert(sql, title, text_f, text, city, handling, tel, startDate, endDate)
    print res, city, handling


if __name__ == '__main__':
    # get_page_url('太原')
    for _area in areas_in:
        get_page_url(_area)
