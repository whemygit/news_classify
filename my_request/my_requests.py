#!/usr/bin/env python
# -- coding: utf-8 --
import requests
import torndb
import time
import re
import json

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
areas = ['大同', '秦皇岛', '阳泉', '乌海', '邯郸',
         '长治', '赤峰', '邢台', '晋城', '呼伦贝尔', '保定', '朔州', '通辽', '忻州', '乌兰察布', '承德', '吕梁', '鄂尔多斯', '沧州',
         '晋中', '巴彦淖尔', '廊坊', '临汾', '衡水', '运城', '四平', '牡丹江',
         '辽源', '佳木斯', '通化', '大庆', '白山', '伊春', '白城', '鸡西', '松原', '鹤岗',
         '双鸭山', '七台河', '绥化', '黑河',
         '无锡', '芜湖', '温州', '蚌埠', '泉州', '常州', '绍兴', '淮南',
         '莆田', '枣庄', '苏州', '湖州', '马鞍山', '漳州', '东营', '南通', '嘉兴', '淮北', '烟台',
         '连云港', '金华', '铜陵', '三明', '潍坊', '淮安', '衢州', '安庆', '南平', '济宁', '盐城', '台州', '黄山',
         '宁德', '泰安', '扬州', '丽水', '阜阳', '威海', '镇江', '舟山', '宿州', '日照', '泰州', '滁州', '滨州',
         '宿迁', '六安', '德州', '宣城', '聊城', '池州', '临沂', '亳州', '菏泽', '莱芜', '开封', '黄石', '株洲',
         '洛阳', '十堰', '湘潭', '平顶山', '荆州', '衡阳', '安阳', '宜昌', '邵阳', '鹤壁', '襄阳', '岳阳', '新乡', '鄂州', '张家界',
         '焦作', '荆门', '益阳', '濮阳', '黄冈', '常德', '许昌', '孝感', '娄底', '漯河', '咸宁', '郴州', '三门峡', '随州', '永州',
         '商丘', '怀化', '周口', '驻马店', '南阳', '信阳', '深圳', '柳州', '珠海', '桂林', '儋州', '汕头',
         '梧州', '三沙', '佛山', '北海', '韶关', '崇左', '湛江', '来宾', '肇庆', '贺州', '江门', '玉林', '茂名', '百色', '惠州', '河池',
         '梅州', '钦州', '汕尾', '防城港', '河源', '贵港', '阳江', '清远', '东莞', '中山', '潮州', '揭阳', '云浮',
         '拉萨', '绵阳', '六盘水', '昭通', '昌都', '自贡', '遵义', '曲靖', '山南', '攀枝花', '铜仁', '玉溪', '日喀则', '泸州',
         '毕节', '普洱', '林芝', '德阳', '安顺', '保山', '广元', '丽江', '遂宁', '临沧', '内江', '乐山', '资阳', '宜宾', '南充', '达州',
         '雅安', '广安', '巴中', '眉山', '铜川', '嘉峪关', '海东', '石嘴山', '克拉玛依', '宝鸡',
         '金昌', '吴忠', '吐鲁番', '咸阳', '白银', '固原', '哈密', '渭南', '天水', '中卫', '汉中', '酒泉', '安康', '张掖', '商洛',
         '武威', '延安', '定西', '榆林', '陇南', '平凉', '庆阳', '湘西土家族苗族自治州', '神农架林区', '天门', '潜江', '仙桃', '积石山保安族东乡族撒拉族自治县',
         '广河县', '永靖县', '东乡族自治县', '和政县', '康乐县', '临夏县',
         '临夏', '日喀则地区', '黔南布依族苗族自治州', '临高县', '澄迈县', '屯昌县', '定安县', '迪庆藏族自治州', '中沙群岛的岛礁及其海域', '南沙群岛', '西沙群岛',
         '琼中黎族苗族自治县', '保亭黎族苗族自治县', '陵水黎族自治县', '乐东黎族自治县', '昌江黎族自治县', '白沙黎族自治县', '万宁', '文昌', '琼海', '五指山', '东方',
         '大理白族自治州', '海北藏族自治州', '黔东南苗族侗族自治州', '山南地区', '怒江傈僳族自治州', '兴安盟', '西双版纳傣族自治州', '海东地区', '德宏傣族景颇族自治州', '昌都地区',
         '桐乡', '海西蒙古族藏族自治州', '锡林郭勒盟', '黔西南布依族苗族自治州', '凉山彝族自治州', '双阳区', '南关区', '朝阳区', '宽城区', '绿园区', '二道区',
         '农安县', '毕节地区', '榆树', '九台', '高新技术产业开发区', '德惠', '经济技术开发区', '汽车产业开发区', '甘南藏族自治州', '净月旅游开发区', '文山壮族苗族自治州',
         '玉树藏族自治州', '铜仁地区', '济源', '甘孜藏族自治州', '恩施土家族苗族自治州', '红河哈尼族彝族自治州', '阿坝藏族羌族自治州', '果洛藏族自治州', '大兴安岭地区', '荷泽',
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
    resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data,
                         headers=headers)  # 服务器
    # resp = requests.post('http://117.78.41.235:8080/cityparlor-web/cityparlor/cityparlor/top/news/save', data=data, headers=headers)         #本地
    return resp


def change_is_resp():
    change_sql = '''update _news_data set is_resp=1 where is_resp=0'''
    res = db.execute(change_sql)
    print res


def requests_post_shouye(data):
    resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/index/add', data=data,
                         headers=headers)
    return resp


def get_info(city):
    sql = '''select * from _news_data where area like "{city}%%" AND news_date="{date_n}" AND is_resp=0'''.format(
        city=city, date_n=date_n)
    # sql='''select * from _news_data where area area="北京"AND img_show is not NULL ORDER BY news_date DESC LIMIT 1;'''
    rec_newsid_sql = '''select newsid from _news_data where area like "{city}%%" AND news_date="{date_n}" AND is_resp=0 LIMIT 5;'''.format(
        city=city, date_n=date_n)
    res = db.query(sql)
    res_rec = db.query(rec_newsid_sql)
    newsid_rec_list = []
    for i in res_rec:
        newsid_rec_list.append(i.get('newsid'))
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
        d['area'] = get_area_code(city)
        d['content'] = text
        d['counts'] = '0'
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
        d['source'] = r.get('text_f')
        d['title'] = r.get('title')
        d['isTop'] = 0
        d['isEssential'] = 0
        d['typeId'] = '1708161038001960000'
        d['isRecommend'] = 0
        d['languageVersion'] = 'ZH'
        resp = requests_post(d)
        print r.get('area'), resp.content

        # 推荐到首页
        if r.get('newsid') in newsid_rec_list:
            rec_data = {}
            rec_data['area'] = d.get('area')
            rec_data['title'] = d.get('title')
            rec_data['source'] = d.get('source')
            rec_data['isTop'] = 0
            rec_data['isEssential'] = 0
            rec_data['classify'] = d.get('classify')
            rec_data['objId'] = json.loads(resp.content).get('retObj')
            rec_data['objType'] = 'news'
            rec_data['imageUrl'] = d.get('pics')
            rec_data['languageVersion'] = d.get('languageVersion')
            resp_shouye = requests_post_shouye(rec_data)
            print resp_shouye.content, d.get('title'), 'shouyetuijian', rec_data.get('languageVersion')


def get_area_code(city):
    sql = """select name, code from t_area where IsEnable=1"""
    res = db.query(sql)
    for r in res:
        area = r.get('name')
        if city in area:
            return r.get('code')


if __name__ == '__main__':
    for _city in areas:
        get_info(_city)
    change_is_resp()
