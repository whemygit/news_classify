#!/usr/bin/env python
# -- coding: utf-8 --
import requests
import pymysql
import  re
import  datetime
from config import collect
from classi import business_predict
import time
import json

date_n = time.strftime("%Y-%m-%d", time.localtime(time.time()))
now = datetime.datetime.now()
date = now + datetime.timedelta(days = 30)
date = date.strftime('%Y-%m-%d')
mysql = {
    "host": collect['host'],
    "port": "3306",
    "database": collect['db'],
    "password": collect['passwd'],
    "user": collect['user'],
    "charset": "utf8"
}

areas = ['北京市', '天津市', '上海市', '广州市', '深圳市', '石家庄市', '太原市', '呼和浩特市', '唐山市', '大同市', '包头市', '秦皇岛市', '阳泉市', '乌海市', '邯郸市',
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


db = pymysql.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))
cur = db.cursor()

my_pid = {
    '1': '金融',
    '2': '农业',
    '3': '城镇建设',
    '4': '工业',
    '5': '服务业',
    '6': '文旅业',
    '7': '互联网',
    '8': '环保',
    '9': '土地出让'
}

def filter_tags(htmlstr):
    """
    清洗和过滤标签
    :param htmlstr: 页面筛选后的html代码块
    :return: 返回处理后的带标签内容
    """
    # 替换p标签
    s = re.sub(r'<p.*?>', '<p>', htmlstr)
    s = re.sub(r'<td.*?>', '<td>', s)
    s = re.sub(r'<strong.*?>', '<strong>', s)
    s = re.sub(r'<span.*?>', '<span>', s)
    s = re.sub(r'<font.*?>', '<font>', s)
    s = re.sub(r'<h2.*?>', '<h2>', s)
    s = re.sub(r'<style>[\s.\S]*?</style>', '', s)
    s = re.sub(r'<div.*?>', '<div>', s)
    s = re.sub(r'<img .*?>', '', s)
    s = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', '', s)
    s = re.sub(r'<\s*script[^>]*>', '', s)
    s = re.sub(r'<a.*?>', '', s)
    s = re.sub(r'</a>', '', s)
    s = re.sub(r'<input.*?>', '', s)
    # s = re.sub(r'<section[\s|\S]*?</section>','',s)

    return s

def rep_tags(htmlstr):
    """
    清洗和过滤标签
    :param htmlstr: 页面筛选后的html代码块
    :return: 返回处理后的带标签内容
    """
    # 替换p标签
    s = re.sub(r'<p.*?>', '<p>', htmlstr)
    s = re.sub(r'<td.*?>', '<td>', s)

    return s

def get_title_area(title):
    for area in areas:
        if area in title:
            return area

def get_info():

    for city, code in get_area_code():
        sql = '''select * from business_opportunity_chinabs where city="{city}" and startDate like "{date}" ORDER BY startDate DESC'''.format(
        city=city, date=date_n)
        # sql = '''select * from business_opportunity_chinabs where startDate like "{date}"'''.format(date='2017-09-18')
        cur.execute(sql)
        res = cur.fetchall()
        for bid,title,text_f,text,city, city_code , handling,tel , startDate, endDate,businessId,businessPid in res:
            try:
                businessPid = business_predict(title, text)['business_pid_1']
                d = dict()
                d['isNewRecord'] = 'true'
                d['recommend'] = '0'
                d['businessPid'] = businessPid
                d['cityCode'] = code
                d['content'] = filter_tags(text)
                d['businessName'] = ''
                d['linkurl'] = handling
                d['company'] = text_f
                d['startDate'] = str(startDate)
                
                d['endDate'] = endDate
                d['tel'] = tel
                d['title'] = title
                get_up_resp(d)
                print (d['title'])
                print (d['businessPid'])

                
            except Exception as e:
                raise e
                print(123)


#获取城市状态码
def get_area_code():
    sql1 = r"""select name, code from t_area where name in (SELECT DISTINCT(city) from """+collect['table']+""")"""
    cur.execute(sql1)
    res = cur.fetchall()
    return res


def get_up_resp(data):
    headers = {
        'accept': 'textml,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.8',
        'cookie': '_user_id=1708281259017703024; _user_account=suqi;',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'

    }
    resp = requests.post('http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/opportunity/project/save', data=data, headers = headers)
    print(resp.content.decode())



if __name__ == '__main__':
    sq = r'''DELETE FROM ''' + collect['table'] + ''' WHERE title IN (SELECT title from (SELECT title FROM '''+collect['table']+''' GROUP BY title HAVING count(bid) > 1) as a) AND bid NOT IN (SELECT * from (SELECT min(bid) FROM '''+collect['table']+''' GROUP BY title HAVING count(title) > 1) as b)'''
    #sq1 = r"""UPDATE """ + collect['table'] + """ set endDate = '"""+date+ """'where opp = 0 """
    #try:
    cur.execute(sq)
    db.commit()
        #cur.execute(sq1)
        #db.commit()
        # with open('/home/spider/zhangxiaodai/KTspider/set_pid_id', 'r', encoding='utf-8') as f:
        #     a = f.readlines()
        # for i in a:
        #     b = re.sub(r'\n', '', i)
        #     cur.execute(b)
        #     db.commit()
    get_info()
    print ('Yes !')
    #except:
    #    print('cuo')
    #finally:
    #    cur.close()
    #    db.close()
