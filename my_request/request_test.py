#!/usr/bin/env python
# -- coding: utf-8 --
import requests
import torndb
import time
import re
import json
from similarity_demo import similarityDemo
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

AREA_DICT = {
    '黄冈市': '421100',
    '鄂尔多斯市': '150600',
    '常州市': '320400',
    '宿州市': '341300',
    '湘西土家族苗族自治州': '433100',
    '神农架林区': '429021',
    '平顶山市': '410400',
    '中山市': '442000',
    '潍坊市': '370700',
    '营口市': '210800',
    '鹤岗市': '230400',
    '娄底市': '431300',
    '金昌市': '620300',
    '绍兴市': '330600',
    '驻马店市': '411700',
    '长治市': '140400',
    '天门市': '429006',
    '潜江市': '429005',
    '仙桃市': '429004',
    '积石山保安族东乡族撒拉族自治县': '622927',
    '广河县': '622924',
    '永靖县': '622923',
    '东乡族自治县': '622926',
    '和政县': '622925',
    '康乐县': '622922',
    '临夏县': '622921',
    '乐山市': '511100',
    '襄阳市': '420600',
    '韶关市': '440200',
    '临夏市': '622901',
    '新余市': '360500',
    '安康市': '610900',
    '吉林市': '220200',
    '汕尾市': '441500',
    '日喀则地区': '542300',
    '石家庄市': '130100',
    '黔南布依族苗族自治州': '522700',
    '朝阳市': '211300',
    '贵阳市': '520100',
    '日照市': '371100',
    '张家界市': '430800',
    '梧州市': '450400',
    '嘉峪关市': '620200',
    '临高县': '469028',
    '澄迈县': '469027',
    '屯昌县': '469026',
    '定安县': '469025',
    '迪庆藏族自治州': '533400',
    '厦门市': '350200',
    '中沙群岛的岛礁及其海域': '469039',
    '南沙群岛': '469038',
    '西沙群岛': '469037',
    '琼中黎族苗族自治县': '469036',
    '保亭黎族苗族自治县': '469035',
    '陵水黎族自治县': '469034',
    '乐东黎族自治县': '469033',
    '昌江黎族自治县': '469031',
    '白沙黎族自治县': '469030',
    '万宁市': '469006',
    '文昌市': '469005',
    '儋州市': '469003',
    '琼海市': '469002',
    '五指山市': '469001',
    '东方市': '469007',
    '丽水市': '331100',
    '大理白族自治州': '532900',
    '海北藏族自治州': '632200',
    '曲靖市': '530300',
    '绵阳市': '510700',
    '济宁市': '370800',
    '合肥市': '340100',
    '沧州市': '130900',
    '揭阳市': '445200',
    '通辽市': '150500',
    '苏州市': '320500',
    '阜新市': '210900',
    '双鸭山市': '230500',
    '咸宁市': '421200',
    '安阳市': '410500',
    '金华市': '330700',
    '长沙市': '430100',
    '阳泉市': '140300',
    '鹰潭市': '360600',
    '四平市': '220300',
    '榆林市': '610800',
    '内江市': '511000',
    '百色市': '451000',
    '牡丹江市': '231000',
    '德阳市': '510600',
    '黔东南苗族侗族自治州': '522600',
    '葫芦岛市': '211400',
    '山南地区': '542200',
    '鄂州市': '420700',
    '莱芜市': '371200',
    '深圳市': '440300',
    '兰州市': '620100',
    '沈阳市': '210100',
    '怒江傈僳族自治州': '533300',
    '莆田市': '350300',
    '大同市': '140200',
    '河源市': '441600',
    '扬州市': '321000',
    '兴安盟': '152200',
    '西双版纳傣族自治州': '532800',
    '抚州市': '361000',
    '益阳市': '430900',
    '北海市': '450500',
    '潮州市': '445100',
    '海东地区': '632100',
    '巴中市': '511900',
    '临沧市': '530900',
    '白城市': '220800',
    '酒泉市': '620900',
    '嘉兴市': '330400',
    '信阳市': '411500',
    '巴彦淖尔市': '150800',
    '永州市': '431100',
    '开封市': '410200',
    '东营市': '370500',
    '宁德市': '350900',
    '德宏傣族景颇族自治州': '533100',
    '丹东市': '210600',
    '汉中市': '610700',
    '齐齐哈尔市': '230200',
    '惠州市': '441300',
    '淮北市': '340600',
    '朔州市': '140600',
    '昆明市': '530100',
    '岳阳市': '430600',
    '雅安市': '511800',
    '柳州市': '450200',
    '泸州市': '510500',
    '景德镇市': '360200',
    '盘锦市': '211100',
    '秦皇岛市': '130300',
    '昌都地区': '542100',
    '天津市': '120100',
    '湛江市': '440800',
    '临汾市': '141000',
    '桐乡市': '330483',
    '无锡市': '320200',
    '滁州市': '341100',
    '海西蒙古族藏族自治州': '632800',
    '阜阳市': '341200',
    '平凉市': '620800',
    '荆州市': '421000',
    '洛阳市': '410300',
    '湖州市': '330500',
    '烟台市': '370600',
    '普洱市': '530800',
    '呼伦贝尔市': '150700',
    '锦州市': '210700',
    '延安市': '610600',
    '鸡西市': '230300',
    '锡林郭勒盟': '152500',
    '怀化市': '431200',
    '黔西南布依族苗族自治州': '522300',
    '周口市': '411600',
    '凉山彝族自治州': '513400',
    '宜昌市': '420500',
    '铜陵市': '340700',
    '广州市': '440100',
    '九江市': '360400',
    '重庆市': '500100',
    '晋城市': '140500',
    '双阳区': '220112',
    '安庆市': '340800',
    '唐山市': '130200',
    '长春市': '220100',
    '南关区': '220102',
    '朝阳区': '220104',
    '宽城区': '220103',
    '绿园区': '220106',
    '二道区': '220105',
    '萍乡市': '360300',
    '梅州市': '441400',
    '陇南市': '621200',
    '农安县': '220122',
    '达州市': '511700',
    '毕节地区': '522400',
    '攀枝花市': '510400',
    '铁岭市': '211200',
    '上海市': '310100',
    '榆树市': '220182',
    '九台市': '220181',
    '高新技术产业开发区': '220184',
    '德惠市': '220183',
    '经济技术开发区': '220186',
    '汽车产业开发区': '220185',
    '威海市': '371000',
    '常德市': '430700',
    '渭南市': '610500',
    '桂林市': '450300',
    '甘南藏族自治州': '623000',
    '净月旅游开发区': '220187',
    '福州市': '350100',
    '台州市': '331000',
    '商洛市': '611000',
    '文山壮族苗族自治州': '532600',
    '茂名市': '440900',
    '徐州市': '320300',
    '宁波市': '330200',
    '南阳市': '411300',
    '运城市': '140800',
    '玉树藏族自治州': '632700',
    '资阳市': '512000',
    '玉林市': '450900',
    '黄石市': '420200',
    '丽江市': '530700',
    '宜春市': '360900',
    '白山市': '220600',
    '西宁市': '630100',
    '铜仁地区': '522200',
    '淮南市': '340400',
    '保定市': '130600',
    '包头市': '150200',
    '淮安市': '320800',
    '滨州市': '371600',
    '济源市': '410881',
    '池州市': '341700',
    '焦作市': '410800',
    '淄博市': '370300',
    '南平市': '350700',
    '衡阳市': '430400',
    '甘孜藏族自治州': '513300',
    '恩施土家族苗族自治州': '422800',
    '抚顺市': '210400',
    '张掖市': '620700',
    '来宾市': '451300',
    '定西市': '621100',
    '红河哈尼族彝族自治州': '532500',
    '佛山市': '440600',
    '广安市': '511600',
    '三亚市': '460200',
    '咸阳市': '610400',
    '自贡市': '510300',
    '廊坊市': '131000',
    '东莞市': '441900',
    '宿迁市': '321300',
    '拉萨市': '540100',
    '北京市': '110100',
    '贵港市': '450800',
    '七台河市': '230900',
    '阿坝藏族羌族自治州': '513200',
    '郑州市': '410100',
    '温州市': '330300',
    '晋中市': '140700',
    '果洛藏族自治州': '632600',
    '松原市': '220700',
    '商丘市': '411400',
    '大兴安岭地区': '232700',
    '郴州市': '431000',
    '荷泽市': '371700',
    '枣庄市': '370400',
    '十堰市': '420300',
    '马鞍山市': '340500',
    '龙岩市': '350800',
    '成都市': '510100',
    '邢台市': '130500',
    '盐城市': '320900',
    '呼和浩特市': '150100',
    '本溪市': '210500',
    '宣城市': '341800',
    '哈尔滨市': '230100',
    '武威市': '620600',
    '肇庆市': '441200',
    '濮阳市': '410900',
    '吕梁市': '141100',
    '邵阳市': '430500',
    '安顺市': '520400',
    '南宁市': '450100',
    '宝鸡市': '610300',
    '邯郸市': '130400',
    '南昌市': '360100',
    '崇左市': '451400',
    '宜宾市': '511500',
    '辽阳市': '211000',
    '林芝地区': '542600',
    '江门市': '440700',
    '乌兰察布市': '150900',
    '昭通市': '530600',
    '南京市': '320100',
    '黄山市': '341000',
    '庆阳市': '621000',
    '泰安市': '370900',
    '云浮市': '445300',
    '大庆市': '230600',
    '芜湖市': '340200',
    '随州市': '421300',
    '南通市': '320600',
    '海南藏族自治州': '632500',
    '六安市': '341500',
    '南充市': '511300',
    '鹤壁市': '410600',
    '株洲市': '430200',
    '赣州市': '360700',
    '辽源市': '220400',
    '天水市': '620500',
    '衢州市': '330800',
    '贺州市': '451100',
    '承德市': '130800',
    '赤峰市': '150400',
    '黑河市': '231100',
    '德州市': '371400',
    '荆门市': '420800',
    '临沂市': '371300',
    '遵义市': '520300',
    '珠海市': '440400',
    '铜川市': '610200',
    '大连市': '210200',
    '三明市': '350400',
    '阳江市': '441700',
    '眉山市': '511400',
    '楚雄彝族自治州': '532300',
    '太原市': '140100',
    '上饶市': '361100',
    '镇江市': '321100',
    '保山市': '530500',
    '防城港市': '450600',
    '遂宁市': '510900',
    '延边朝鲜族自治州': '224000',
    '阿里地区': '542500',
    '许昌市': '411000',
    '阿拉善盟': '152900',
    '伊春市': '230700',
    '三门峡市': '411200',
    '武汉市': '420100',
    '蚌埠市': '340300',
    '连云港市': '320700',
    '忻州市': '140900',
    '吉安市': '360800',
    '白银市': '620400',
    '亳州市': '341600',
    '绥化市': '231200',
    '聊城市': '371500',
    '新乡市': '410700',
    '青岛市': '370200',
    '舟山市': '330900',
    '漳州市': '350600',
    '湘潭市': '430300',
    '张家口市': '130700',
    '乌海市': '150300',
    '济南市': '370100',
    '西安市': '610100',
    '鞍山市': '210300',
    '泉州市': '350500',
    '河池市': '451200',
    '海口市': '460100',
    '孝感市': '420900',
    '六盘水市': '520200',
    '汕头市': '440500',
    '泰州市': '321200',
    '黄南藏族自治州': '632300',
    '清远市': '441800',
    '那曲地区': '542400',
    '漯河市': '411100',
    '广元市': '510800',
    '衡水市': '131100',
    '杭州市': '330100',
    '玉溪市': '530400',
    '钦州市': '450700',
    '佳木斯市': '230800',
    '银川': '640100',
    '阳朔': '450321',
    '乌鲁木齐': '650100',
    '昌吉回族自治州': '652300',
    '中卫市': '640500',
    '吴忠市': '640300',
}

mysql = {
    "host": "192.168.0.202",
    "port": "3306",
    "database": "spider",
    "password": "123456",
    "user": "suqi",
    "charset": "utf8"
}

# mysql = {
#     "host": "119.57.93.42",
#     "port": "3306",
#     "database": "spider",
#     "password": "zhongguangzhangshi",
#     "user": "bigdata",
#     "charset": "utf8"
# }

headers = {
    'accept': 'textml,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.8',
    'cookie': '_user_id=1708281259017703024; _user_account=suqi;',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))

date_n = time.strftime("%Y-%m-%d", time.localtime(time.time()))


def requests_post(data):
    # resp = requests.post('http://cms.loongscity.com/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data, headers=headers)
    # resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data,headers=headers)  # 服务器
    resp = requests.post('http://117.78.41.235:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data, headers=headers)         #本地
    return resp


def requests_post_shouye(data):
    resp = requests.post('http://117.78.41.235:8080//cityparlor-web/cityparlor/cityparlor/index/add', data=data,
                         headers=headers)  # 本地
    # # resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/index/add', data=data,
    #                      headers=headers)
    return resp


def change_is_resp(newsid):
    change_sql = '''update rec_news_data set is_resp=1 where newsid=%s''' % newsid
    res = db.execute(change_sql)
    print res


# def get_info():
#     sql = '''select * from rec_news_data where is_resp=0;'''
#     # sql = '''select * from rec_news_data where news_date='2017-10-31';'''
#     res = db.query(sql)
#     title_simi_test = similarityDemo()
#     for r in res:
#         # print r.get('title')
#         flag=title_simi_test.similarity(r.get('title'))
#         if flag is True:
#             print 'qqqqqqq:',r.get('title')
#         #     d=dict()
#         #     d['title']=r.get('title')
#         #     d['area'] = 0
#         #     for area in AREA_DICT.keys():
#         #         if '市' in area:
#         #             if area.encode('utf-8')[:-3] in r.get('title'):
#         #                 d['area'] = AREA_DICT.get(area)
#         #         if area in r.get('title'):
#         #             d['area'] = AREA_DICT.get(area)
#         #     d['newsDesc'] = r.get('title')
#         #     d['source'] = r.get('text_f')
#         #     d['content'] = r.get('text')
#         #     d['newsType'] = '1'
#         #     d['counts'] = '0'
#         #     d['languageVersion'] = 'ZH'
#         #     if u'十九大' in r.get('title'):
#         #         d['typeId'] = '1710230954253860000'
#         #     d['isRecommend'] = 1
#         #     img_show=r.get('img_show')
#         #     if img_show==None:
#         #         d['classify']=0
#         #     else:
#         #         img_show_len=len(img_show.split(','))
#         #         if img_show_len<=2:
#         #             d['classify']=2
#         #             d['pics']=img_show.split(',')[0]
#         #         else:
#         #             d['classify']=1
#         #             d['pics']=img_show
#         #     d['isTop'] = 0
#         #     d['isEssential'] = 0
#         #     resp = requests_post(d)
#         #     print resp.content,r.get('title')
#         #
#         #     #推荐到首页
#         #     rec_data={}
#         #     rec_data['area'] = d.get('area')
#         #     rec_data['title'] = d.get('title')
#         #     rec_data['source'] = d.get('source')
#         #     rec_data['isTop'] = 0
#         #     rec_data['isEssential'] = 0
#         #     rec_data['classify'] = d.get('classify')
#         #     try:
#         #         rec_data['objId'] = json.loads(resp.content).get('retObj')
#         #     except ValueError:
#         #         news_id = r.get('newsid')
#         #         change_is_resp(news_id)
#         #         continue
#         #     rec_data['objType'] = 'news'
#         #     rec_data['languageVersion'] = d.get('languageVersion')
#         #     rec_data['imageUrl'] = d.get('pics')
#         #     resp_shouye = requests_post_shouye(rec_data)
#         #     print resp_shouye.content,d.get('title'),'shouyetuijian',rec_data.get('area'),rec_data.get('languageVersion')
#         # else:
#         #     print 'replicate title:',d.get('title')
#
#         # news_id = r.get('newsid')
#         # change_is_resp(news_id)

def get_info():
    sql = '''select * from rec_news_data where is_resp=0;'''
    # sql = '''select * from rec_news_data where news_date='2017-10-31';'''
    res = db.query(sql)
    simi_cla = similarityDemo()
    for r in res:
        d=dict()
        d['title']=r.get('title')
        flag = simi_cla.similarity(d['title'])

        if flag is True:
            d['area'] = 0
            for area in AREA_DICT.keys():
                if '市' in area:
                    if area.encode('utf-8')[:-3] in r.get('title'):
                        d['area'] = AREA_DICT.get(area)
                if area in r.get('title'):
                    d['area'] = AREA_DICT.get(area)
            d['newsDesc'] = r.get('title')
            d['source'] = r.get('text_f')
            d['content'] = r.get('text')
            d['newsType'] = '1'
            d['counts'] = '0'
            d['languageVersion'] = 'ZH'
            if u'十九大' in r.get('title'):
                d['typeId'] = '1710230954253860000'
            d['isRecommend'] = 1
            img_show = r.get('img_show')
            if img_show == None:
                d['classify'] = 0
            else:
                img_show_len = len(img_show.split(','))
                if img_show_len <= 2:
                    d['classify'] = 2
                    d['pics'] = img_show.split(',')[0]
                else:
                    d['classify'] = 1
                    d['pics'] = img_show
            d['isTop'] = 0
            d['isEssential'] = 0
            # resp = requests_post(d)
            # print resp.content,r.get('title')

            # 推荐到首页
            rec_data = {}
            rec_data['area'] = d.get('area')
            rec_data['title'] = d.get('title')
            rec_data['source'] = d.get('source')
            rec_data['isTop'] = 0
            rec_data['isEssential'] = 0
            rec_data['classify'] = d.get('classify')
            try:
                " "
                # rec_data['objId'] = json.loads(resp.content).get('retObj')
            except ValueError:
                news_id = r.get('newsid')
                change_is_resp(news_id)
                continue
            rec_data['objType'] = 'news'
            rec_data['languageVersion'] = d.get('languageVersion')
            rec_data['imageUrl'] = d.get('pics')
            # resp_shouye = requests_post_shouye(rec_data)
            # print resp_shouye.content,d.get('title'),'shouyetuijian',rec_data.get('area'),rec_data.get('languageVersion')
        else:
            print "重复标题",r.get("title")

        # news_id = r.get('newsid')
        # change_is_resp(news_id)


if __name__ == '__main__':
    get_info()


