#!/usr/bin/env python
# -- coding: utf-8 --
import requests
import torndb
import time
import re

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
areas = ['大同市', '秦皇岛市', '阳泉市', '乌海市', '邯郸市',
         '长治市', '赤峰市', '邢台市', '晋城市', '呼伦贝尔市', '保定市', '朔州市', '通辽市', '张家口市', '忻州市', '乌兰察布市', '承德市', '吕梁市', '鄂尔多斯市', '沧州市',
         '晋中市', '巴彦淖尔市', '廊坊市', '临汾市', '衡水市', '运城市', '四平市', '牡丹江市',
         '辽源市', '佳木斯市', '通化市', '大庆市', '白山市', '伊春市', '白城市', '鸡西市', '松原市', '鹤岗市',
         '双鸭山市', '七台河市', '绥化市', '黑河市',
         '无锡市', '芜湖市', '赣州市', '温州市', '蚌埠市', '泉州市', '宜春市', '常州市', '绍兴市', '淮南市',
         '莆田市', '吉安市', '枣庄市', '苏州市', '湖州市', '马鞍山市', '漳州市', '上饶市', '东营市', '南通市', '嘉兴市', '淮北市', '抚州市', '烟台市',
         '连云港市', '金华市', '铜陵市', '三明市', '九江市', '潍坊市', '淮安市', '衢州市', '安庆市', '南平市', '景德镇市', '济宁市', '盐城市', '台州市', '黄山市',
         '宁德市', '萍乡市', '泰安市', '扬州市', '丽水市', '阜阳市', '新余市', '威海市', '镇江市', '舟山市', '宿州市', '鹰潭市', '日照市', '泰州市', '滁州市', '滨州市',
         '宿迁市', '六安市', '德州市', '宣城市', '聊城市', '池州市', '临沂市', '亳州市', '菏泽市', '莱芜市', '开封市', '黄石市', '株洲市',
         '洛阳市', '十堰市', '湘潭市', '平顶山市', '荆州市', '衡阳市', '安阳市', '宜昌市', '邵阳市', '鹤壁市', '襄阳市', '岳阳市', '新乡市', '鄂州市', '张家界市',
         '焦作市', '荆门市', '益阳市', '濮阳市', '黄冈市', '常德市', '许昌市', '孝感市', '娄底市', '漯河市', '咸宁市', '郴州市', '三门峡市', '随州市', '永州市',
         '商丘市', '怀化市', '周口市', '驻马店市', '南阳市', '信阳市', '深圳市', '柳州市', '三亚市', '珠海市', '桂林市', '儋州市', '汕头市',
         '梧州市', '三沙市', '佛山市', '北海市', '韶关市', '崇左市', '湛江市', '来宾市', '肇庆市', '贺州市', '江门市', '玉林市', '茂名市', '百色市', '惠州市', '河池市',
         '梅州市', '钦州市', '汕尾市', '防城港市', '河源市', '贵港市', '阳江市', '清远市', '东莞市', '中山市', '潮州市', '揭阳市', '云浮市',
         '拉萨市', '绵阳市', '六盘水市', '昭通市', '昌都市', '自贡市', '遵义市', '曲靖市', '山南市', '攀枝花市', '铜仁市', '玉溪市', '日喀则市', '泸州市',
         '毕节市', '普洱市', '林芝市', '德阳市', '安顺市', '保山市', '广元市', '丽江市', '遂宁市', '临沧市', '内江市', '乐山市', '资阳市', '宜宾市', '南充市', '达州市',
         '雅安市', '广安市', '巴中市', '眉山市', '铜川市', '嘉峪关市', '海东市', '石嘴山市', '克拉玛依市', '宝鸡市',
         '金昌市', '吴忠市', '吐鲁番市', '咸阳市', '白银市', '固原市', '哈密市', '渭南市', '天水市', '中卫市', '汉中市', '酒泉市', '安康市', '张掖市', '商洛市',
         '武威市', '延安市', '定西市', '榆林市', '陇南市', '平凉市', '庆阳市', '湘西土家族苗族自治州', '神农架林区', '天门市', '潜江市', '仙桃市', '积石山保安族东乡族撒拉族自治县',
         '广河县', '永靖县', '东乡族自治县', '和政县', '康乐县', '临夏县',
         '临夏市', '日喀则地区', '黔南布依族苗族自治州', '临高县', '澄迈县', '屯昌县', '定安县', '迪庆藏族自治州', '中沙群岛的岛礁及其海域', '南沙群岛', '西沙群岛',
         '琼中黎族苗族自治县', '保亭黎族苗族自治县', '陵水黎族自治县', '乐东黎族自治县', '昌江黎族自治县', '白沙黎族自治县', '万宁市', '文昌市', '琼海市', '五指山市', '东方市',
         '大理白族自治州', '海北藏族自治州', '黔东南苗族侗族自治州', '山南地区', '怒江傈僳族自治州', '兴安盟', '西双版纳傣族自治州', '海东地区', '德宏傣族景颇族自治州', '昌都地区',
         '桐乡市', '海西蒙古族藏族自治州', '锡林郭勒盟', '黔西南布依族苗族自治州', '凉山彝族自治州', '双阳区', '南关区', '朝阳区', '宽城区', '绿园区', '二道区',
         '农安县', '毕节地区', '榆树市', '九台市', '高新技术产业开发区', '德惠市', '经济技术开发区', '汽车产业开发区', '甘南藏族自治州', '净月旅游开发区', '文山壮族苗族自治州',
         '玉树藏族自治州', '铜仁地区', '济源市', '甘孜藏族自治州', '恩施土家族苗族自治州', '红河哈尼族彝族自治州', '阿坝藏族羌族自治州', '果洛藏族自治州', '大兴安岭地区', '荷泽市',
         '林芝地区', '海南藏族自治州', '楚雄彝族自治州', '延边朝鲜族自治州', '阿里地区', '阿拉善盟', '黄南藏族自治州', '那曲地区', '阳朔', '乌鲁木齐', '昌吉回族自治州']
# mysql = {
#     "host": "192.168.0.202",
#     "port": "3306",
#     "database": "spider",
#     "password": "123456",
#     "user": "suqi",
#     "charset": "utf8"
# }

mysql = {
    "host": "119.57.93.42",
    "port": "3306",
    "database": "spider",
    "password": "zhongguangzhangshi",
    "user": "bigdata",
    "charset": "utf8"
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
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
    # resp = requests.post('http://192.168.0.225:8080/cityparlor-web/cityparlor/cityparlor/index/save', data=data)
    resp = requests.post('http://117.78.41.235:8080/cityparlor-web/cityparlor/cityparlor/index/save', data=data)
    return resp


def change_is_resp():
    change_sql = '''update _news_data set is_resp=1 where is_resp=0'''
    res = db.execute(change_sql)
    print res


def requests_post_1(data):
    resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data,headers=headers)
    # resp = requests.post('http://117.78.41.235:8080/cityparlor-web/cityparlor/cityparlor/top/news/add', data=data, headers=headers)
    return resp


def get_info(city):
    # sql = """select * from news_data where area="%s" AND img_show is not NULL ORDER BY news_date DESC limit 1""" % city
    sql = '''select * from _news_data where area="%s" AND news_date="%s" AND img_show is not NULL ORDER BY news_date DESC''' % (
    city, date_n)
    # sql = '''select * from _news_data where area="%s" AND news_date="2017-06-03" AND img_show is not NULL ORDER BY news_date DESC''' % city
    res = db.query(sql)
    for r in res:
        d = dict()
        text = str(r.get('text')).replace(r'\n', '').replace('\\', '').replace('http', 'https').replace(
            '<style>.*?</style>', '')
        imgs = re.findall(r'<img.+?src="(.*?)"', text)
        if imgs:
            for img in imgs:
                _img = '<img src="' + img + '">'
                reg = '<img src="%s".*?/>' % img
                text = re.sub(reg, _img, text)
        d['area'] = get_area_code(r.get('area'))
        d['content'] = text
        d['counts'] = '0'
        # d['createDate'] = str(r.get('news_date'))
        d['newsDesc'] = r.get('title')
        d['newsType'] = '1'
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
        # d['pics'] = ','.join([img for img in imgs])
        d['source'] = r.get('text_f')
        d['title'] = r.get('title')
        d['isTop'] = 0
        d['isEssential'] = 0
        d['typeId'] = '1708161038001960000'
        d['isRecommend'] = 0
        resp = requests_post_1(d)
        print r.get('area'), resp.content
        # retObj = json.loads(resp.content).get('retObj')
        # d_1 = dict()
        # d_1['area'] = get_area_code(r.get('area'))
        # d_1['imageUrl'] = r.get('img_show')
        # d_1['number'] = 3
        # d_1['objId'] = retObj
        # d_1['objType'] = 'news'
        # d_1['title'] = r.get('title')
        # resp = requests_post(d_1)
        # print d_1['area'], r.get('area'), resp.content


def get_area_code(city):
    sql = """select name, code from t_area"""
    res = db.query(sql)
    for r in res:
        area = r.get('name')
        if city in area:
            return r.get('code')


if __name__ == '__main__':
    for _city in areas:
        get_info(_city)
        # requests_post(data)
        # get_area_code(_city)
    change_is_resp()
