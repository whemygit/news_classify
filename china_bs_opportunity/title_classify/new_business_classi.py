#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import json

import MySQLdb
import datetime

reload(sys)
sys.setdefaultencoding('utf8')



jsonstr="""
[
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "其它类食品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "仪表配附件",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "便携式超声诊断设备",
        "id": ""
    },
     {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "型材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "分析仪",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "食用菌",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "醛类",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "衡器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "实验室用品",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "其他污水处理设备",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_1",
        "pid_title": "文化创意",
        "key_words": "舞台设备",
        "id": ""
    }, {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_1",
        "pid_title": "文化创意",
        "key_words": "工艺品",
        "id": ""
    }, {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_1",
        "pid_title": "文化创意",
        "key_words": "美术品",
        "id": ""
    },{
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_1",
        "pid_title": "文化创意",
        "key_words": "影视",
        "id": ""
    },
    {
        "mypid": "6",
        "id_title": "",
        "pid": "1708271201536210151",
        "myid": "6_1",
        "pid_title": "知识产权",
        "key_words": "教学专用仪器",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_6",
        "pid_title": "文化创意",
        "key_words": "书画工艺",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "冶金专用设备",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_1",
        "pid_title": "文化创意",
        "key_words": "音乐厅",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_3",
        "pid_title": "农业水利",
        "key_words": "干果",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_1",
        "pid_title": "文化创意",
        "key_words": "广播电台",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "地质地震仪器",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_4",
        "pid_title": "网络电信",
        "key_words": "交换设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "办公用纸",
        "id": ""
    },
    {
        "mypid": "15",
        "id_title": "",
        "pid": "1708271201536210157",
        "myid": "15",
        "pid_title": "其他",
        "key_words": "其它设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "聚合物",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_2",
        "pid_title": "医疗康养",
        "key_words": "维生素及营养药",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "压缩分离设备",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_1",
        "pid_title": "文化创意",
        "key_words": "图书音像",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "网络通信",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用离心机",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "电化学仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "天然纺织原料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "气体检测仪",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "刀具夹具",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "床上用品",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "制药用水设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "复合包装制品",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_2",
        "pid_title": "农业水利",
        "key_words": "乳制品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "气动单元组合仪表",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "包装专用设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "磨抛光电动工具",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_1",
        "pid_title": "矿产能源",
        "key_words": "铜",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "粉碎设备",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_1",
        "pid_title": "矿产能源",
        "key_words": "金属粉末",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "污泥",
        "id": ""
    }, 
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "大街",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "印刷耗材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "酒类",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "起重运输设备",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "出入境检验检疫局",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "软件维护",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "电子材料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "醇类",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "无机盐",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "耐火防火材料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "纺织皮革机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_9",
        "pid_title": "工业制造",
        "key_words": "诊断图象处理软件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "休闲食品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "传动系统",
        "id": ""
    },
    {
        "mypid": "14",
        "id_title": "",
        "pid": "1708271201536210156",
        "myid": "14_4",
        "pid_title": "旅游开发",
        "key_words": "游艺设施",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "绝缘材料",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "输液辅助装置",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "无缝管",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "行政服务中心",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "数控车床",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "超声辅助材料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "出版印刷",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "路面设备",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "系统集成",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "药物检测专用仪器",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_1",
        "pid_title": "矿产能源",
        "key_words": "黑色金属矿产",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_2",
        "pid_title": "农业水利",
        "key_words": "蛋肉类及制品、乳制品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "包装绳",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_1",
        "pid_title": "网络电信",
        "key_words": "安全检测设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "鞋",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "专科用制剂",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "润滑油",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "血流量测定装置及血容量测定装置",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "低温治疗仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "调味品",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_4",
        "pid_title": "农业水利",
        "key_words": "收获机械",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "DPU",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "黄油枪",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_6",
        "pid_title": "文化创意",
        "key_words": "中国美术馆",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "烯烃",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "内窥镜",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "空气净化成套设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "劳保用品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "成像系统",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "塑料加工专用设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "超声手术及聚焦治疗设备",
        "id": ""
    },
    {
        "mypid": "14",
        "id_title": "",
        "pid": "1708271201536210156",
        "myid": "14_4",
        "pid_title": "旅游开发",
        "key_words": "娱乐服务",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "音响",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "网络工程",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_1",
        "pid_title": "矿产能源",
        "key_words": "选矿设备",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "牲畜",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "心电诊断仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "体育用品",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_1",
        "pid_title": "医疗康养",
        "key_words": "感染类药",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "电子垃圾处理设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "计量、标准器具",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "无机碱",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_6",
        "pid_title": "文化创意",
        "key_words": "民间工艺品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "印花布",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "绘图计算测量仪器",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "茶叶",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "起重装卸设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_9",
        "pid_title": "工业制造",
        "key_words": "智慧教室",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "数据中心",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "软饮料",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_5",
        "pid_title": "市政建设",
        "key_words": "绿化苗木",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "食品加工设备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "半导体材料",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "数据采集",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "烟",
        "id": ""
    },{
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "酒",
        "id": ""
    },{
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "农业水利",
        "key_words": "茶",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "维护清洗",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "生化",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "其他机械五金类",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_5",
        "pid_title": "市政建设",
        "key_words": "花卉",
        "id": ""
    },
    {
        "mypid": "14",
        "id_title": "",
        "pid": "1708271201536210156",
        "myid": "14_4",
        "pid_title": "旅游开发",
        "key_words": "体育",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "催化剂",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "凿岩机",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "设备采购",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "非织造设备",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_3",
        "pid_title": "矿产能源",
        "key_words": "中国石油",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_3",
        "pid_title": "矿产能源",
        "key_words": "煤",
        "id": ""
    },{
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_3",
        "pid_title": "矿产能源",
        "key_words": "金属",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "胶辊",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用超声仪器及有关设备",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_1",
        "pid_title": "矿产能源",
        "key_words": "铁合金",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用电子仪器设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "电工仪表",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "清洗设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "石油专用分析仪器",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "眼科手术用其他器械",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "高频手术",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "化工",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "日用化学品",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_2",
        "pid_title": "网络电信",
        "key_words": "传输设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "基础外科用剪",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "印刷加工服务",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "编辑制作设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "印后设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "听诊器",
        "id": ""
    },
    {
        "mypid": "15",
        "id_title": "",
        "pid": "1708271201536210157",
        "myid": "15",
        "pid_title": "其他",
        "key_words": "租赁和商务服务",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_9",
        "pid_title": "工业制造",
        "key_words": "自动化成套控制系统",
        "id": ""
    },
    {
        "mypid": "15",
        "id_title": "",
        "pid": "1708271201536210157",
        "myid": "15",
        "pid_title": "其他",
        "key_words": "展示用品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "水分测定仪",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "健身器材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "制药生产设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "X射线诊断设备及高压发生装置",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_4",
        "pid_title": "矿产能源",
        "key_words": "能源工程",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "桌面用品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "反渗透设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "土地耕整机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "原水处理设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "电子测量仪器",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "消毒灭菌设备及器具",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_4",
        "pid_title": "网络电信",
        "key_words": "通信线缆",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "血压计",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "中盐",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "电凝设备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "建筑用粘合剂",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "呼吸设备",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "救生器材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "电容器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "印刷用纸",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "石油钻采专用设备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "石材石料",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "扶贫基金",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "X射线计算机断层摄影设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "高纯水制取设备",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_1",
        "pid_title": "矿产能源",
        "key_words": "钢铁",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "含油子仁、果仁、籽",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_4",
        "pid_title": "矿产能源",
        "key_words": "水电",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_4",
        "pid_title": "矿产能源",
        "key_words": "新能源",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "胶粘剂",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "胸腔心血管外科用钳",
        "id": ""
    },
    {
        "mypid": "6",
        "id_title": "",
        "pid": "1708271201536210151",
        "myid": "6_1",
        "pid_title": "知识产权",
        "key_words": "专利",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "乐器",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "防雷避雷产品",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "金属制品",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_5",
        "pid_title": "交通运输",
        "key_words": "物流运输",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "玻璃纤维",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "机械零部件加工 ",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用磁共振设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "中药制药设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "血管内导管",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "竹木包装制品",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_5",
        "pid_title": "市政建设",
        "key_words": "公园",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "办公本册",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "橡胶制品",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "覆铜板材料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "摄像器材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "手动轮椅车",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "药用包装机械",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用制气设备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "木材板材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "纱线丝",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "液压工具",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_2",
        "pid_title": "网络电信",
        "key_words": "电信工程",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_5",
        "pid_title": "市政建设",
        "key_words": "园林绿化",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "锁具",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_5",
        "pid_title": "交通运输",
        "key_words": "储运设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "车辆",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "电线电缆",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "厨卫家电",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "基础外科用镊夹",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "矿石分选设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "涂装设备",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_5",
        "pid_title": "交通运输",
        "key_words": "产品运输",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "发电机",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "停车场设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "眼科光学仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "烷烃",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "光学仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "无机化工原料 ",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "建筑玻璃",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "造纸设备及配件",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "电焊",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "分析仪器",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "药包材检测设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_5",
        "pid_title": "医疗康养",
        "key_words": "免疫分析系统",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "传动件",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_2",
        "pid_title": "矿产能源",
        "key_words": "电力供应",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "机械五金",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "监控设备器材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "血液分析系统",
        "id": ""
    },
    {
        "mypid": "3",
        "id_title": "",
        "pid": "1708271201504590140",
        "myid": "3_5",
        "pid_title": "土地开发",
        "key_words": "宾馆招租",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "其他通用分析仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "半导体分立器件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "防护保养品",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "信息安全设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "炉用燃烧器",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "胸腔心血管外科用镊夹",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "橡胶片",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "非织造及工业用布",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "教学模型",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "血液净化设备和血液净化器具",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "海洋技术中心",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "插头插座",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "发电机组",
        "id": ""
    },
    {
        "mypid": "14",
        "id_title": "",
        "pid": "1708271201536210156",
        "myid": "14_1",
        "pid_title": "旅游开发",
        "key_words": "电动观光车",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_1",
        "pid_title": "建筑建材",
        "key_words": "隔断吊顶 ",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "临床检验仪器设备",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_5",
        "pid_title": "交通运输",
        "key_words": "集装箱",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "氧化物",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "整流器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "生物工程设备",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "文物局",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "禽类",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "集成电路",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_1",
        "pid_title": "网络电信",
        "key_words": "防伪技术产品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "电动机",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "染整设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "床检验分析仪器",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_1",
        "pid_title": "交通运输",
        "key_words": "运输搬运设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "诊察治疗设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "电动车",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "专用仪表",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "基因和生命科学仪器",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "门窗",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "国税",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "光谱仪",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "过滤设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_5",
        "pid_title": "医疗康养",
        "key_words": "供氧系统",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_2",
        "pid_title": "矿产能源",
        "key_words": "低压电器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "礼品饰品",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "接插件(连接器)",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "水泥砖瓦",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "其他印刷机械专用配件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "芳香烃",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用刺激器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "服装",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "建筑设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "视力诊察器具",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "纺织面料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "挖掘机械",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "手动手术台床",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "制剂",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "其它消毒灭菌设备",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_4",
        "pid_title": "农业水利",
        "key_words": "种植机械",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "消防器材",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "弹簧",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "妇科检查器械",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "地税",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "刷",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "生态监测",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "其它仪器仪表",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "电工电器成套设备",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "禽蛋",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医疗设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "自动化设备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "刀",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "胺类",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "办公笔类",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "钳子 ",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "商务部",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "生物制品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "家纺",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "农林牧渔专用机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "频率元件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "天然橡胶",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_1",
        "pid_title": "医疗康养",
        "key_words": "兽用药品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_9",
        "pid_title": "工业制造",
        "key_words": "工业机器人",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "皮革助剂",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "其他玩具",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_4",
        "pid_title": "矿产能源",
        "key_words": "气体",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用材料",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "空气净化设备 ",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "金属加工机床",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_1",
        "pid_title": "矿产能源",
        "key_words": "其他钢铁产品",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "电子内窥镜",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "纺织加工",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用缝合针",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "起钉器",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "丝锥、板牙",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_4",
        "pid_title": "医疗康养",
        "key_words": "标牌",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "鼻腔止血器（清洗器）",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "印刷机",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "化纤处理机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "产品印刷加工",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用光学器具",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "光学内窥镜及冷光源",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "筛分设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "包装配套制品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "包装用纸",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_2",
        "pid_title": "矿产能源",
        "key_words": "发电",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "风机排风设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "饮料加工设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "注射穿刺器械",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "物理治疗设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "继电器",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "橡胶板",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "餐厨用具",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "防护帽",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "建材",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "超声治疗设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "礼品包装",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_4",
        "pid_title": "农业水利",
        "key_words": "农用物资",
        "id": "shui"
    },
     {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_4",
        "pid_title": "农业水利",
        "key_words": "天然林",
        "id": "shui"
    }, 
     {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_4",
        "pid_title": "农业水利",
        "key_words": "苗木",
        "id": "shui"
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_4",
        "pid_title": "农业水利",
        "key_words": "药材",
        "id": "shui"
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "反应设备 ",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "板材",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_3",
        "pid_title": "矿产能源",
        "key_words": "煤制品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "橡胶助剂",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "牙科椅",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_3",
        "pid_title": "矿产能源",
        "key_words": "石油设备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "建筑陶瓷",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "毯子",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "日用五金",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "磁性材料",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_1",
        "pid_title": "医疗康养",
        "key_words": "抗肿癌药",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "高压电器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "人造革",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_2",
        "pid_title": "交通运输",
        "key_words": "轨道交通设备器材 ",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "塑胶片 ",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "生命科学仪器及设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "计算机周边",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "计算机及配件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "冰箱",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "塑料包装制品",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "装配电动工具",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_4",
        "pid_title": "矿产能源",
        "key_words": "超声换能器",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "生活饮用水处理设备",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_1",
        "pid_title": "交通运输",
        "key_words": "商用车",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "鲜活水产品",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_5",
        "pid_title": "医疗康养",
        "key_words": "血站",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "门窗五金",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "压力仪表",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "交通安全设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "紧固件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "胶带",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "化学试剂",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "塑料管",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "羧酸",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_4",
        "pid_title": "矿产能源",
        "key_words": "太阳能设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "生化分析系统",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "泌尿肛肠科用钳",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "出入境边防检查站",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "部队",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "办公文具",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "电声器件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "沥青",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "实验室仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "焊接材料与附件",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用化验和基础设备器具",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "国家机关",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_3",
        "pid_title": "矿产能源",
        "key_words": "采煤机",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_5",
        "pid_title": "市政建设",
        "key_words": "园艺机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "色织",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "软件开发",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_1",
        "pid_title": "网络电信",
        "key_words": "门禁考勤对讲",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "小家电",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "环境",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "米面油及调味品类",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "管件",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "矫形（骨科）外科用剪",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_4",
        "pid_title": "矿产能源",
        "key_words": "其它能源",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "金属包装制品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "其他自动化类仪表装置",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "撬棍",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "防护服",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "化学助剂",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_6",
        "pid_title": "文化创意",
        "key_words": "雕刻工艺品 ",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "其它家用电器类",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "防盗报警器材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "传质设备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_1",
        "pid_title": "建筑建材",
        "key_words": "建筑工程",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "其他电子产品",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_1",
        "pid_title": "医疗康养",
        "key_words": "植物原药材",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_3",
        "pid_title": "文化创意",
        "key_words": "广告展览器材",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_3",
        "pid_title": "农业水利",
        "key_words": "坚果",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "软件服务",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "配电输电设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "一般医疗用品",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "信息化建设",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_1",
        "pid_title": "文化创意",
        "key_words": "摄影器材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "塑胶制品",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "农药",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "输液、输血器具及管路",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "非金属加工机床",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "开关",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_2",
        "pid_title": "网络电信",
        "key_words": "通讯产品",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用培养箱",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "汽摩及配件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "车用仪表",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "印刷设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "光学测量仪",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "手机及配件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "橡胶棒",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "电源及电池",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "电子显微镜",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用X线影像系统及成像器件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "专项化学品",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "紫外线灭菌灯",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "呼吸麻醉设备",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "财政部",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "楼梯电梯",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "臭氧消毒机",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "物理研究所",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "纺机设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "汽摩产品制造设备",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_5",
        "pid_title": "农业水利",
        "key_words": "水利水文用仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "光电与显示器件",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "用于心脏的治疗、急救装置",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_1",
        "pid_title": "医疗康养",
        "key_words": "中成药",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "日用百货",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "箱、包、皮具",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "生理研究实验仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "三轮车",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "传感器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "清洗剂",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "电动汽车",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "米面",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_1",
        "pid_title": "医疗康养",
        "key_words": "保健食品",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_2",
        "pid_title": "文化创意",
        "key_words": "代理经营",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_6",
        "pid_title": "文化创意",
        "key_words": "文物",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "测绘仪器及器材",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "压力蒸汽灭菌设备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "水暖五金 ",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "数据库",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_1",
        "pid_title": "网络电信",
        "key_words": "其它安全防护类",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "财务用品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "其他电动车",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_4",
        "pid_title": "医疗康养",
        "key_words": "标签",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_5",
        "pid_title": "医疗康养",
        "key_words": "病床",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "防护眼镜",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "量仪",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "办公用品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "减速机变速机",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "有色金属加工材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "腈类",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "建材涂料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "终端设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "混合设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "口腔综合治疗设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "酚类",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_4",
        "pid_title": "农业水利",
        "key_words": "农林牧渔仪器仪表",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "装饰五金",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "生物反馈仪",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "专利局",
        "id": ""
    },{
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "高新区",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "接入设备",
        "id": ""
    },
     {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "管理平台",
        "id": ""
    },
    {
        "mypid": "15",
        "id_title": "",
        "pid": "1708271201536210157",
        "myid": "15",
        "pid_title": "其他",
        "key_words": "其它工具",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "管材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "电风扇",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_2",
        "pid_title": "文化创意",
        "key_words": "会展服务",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "其他电子材料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_9",
        "pid_title": "工业制造",
        "key_words": "前端设备",
        "id": ""
    },
    {
        "mypid": "3",
        "id_title": "",
        "pid": "1708271201504590140",
        "myid": "3_6",
        "pid_title": "土地开发",
        "key_words": "经济适用住房",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "螺丝刀 ",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_6",
        "pid_title": "文化创意",
        "key_words": "其他工艺品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "其它运动休闲类",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4",
        "pid_title": "医疗康养",
        "key_words": "医院",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "金属成型机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "轮胎",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "保温隔热材料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "采矿采石设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "流量仪表",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_1",
        "pid_title": "网络电信",
        "key_words": "警用装备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_3",
        "pid_title": "建筑建材",
        "key_words": "涂料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "包装材料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "掘进机",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "袜",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "电子",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_1",
        "pid_title": "医疗康养",
        "key_words": "消化系统药物",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_2",
        "pid_title": "网络电信",
        "key_words": "电话机系列",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "电疗仪器",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "心电电极",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "布料包装制品",
        "id": ""
    },
    {
        "mypid": "6",
        "id_title": "",
        "pid": "1708271201536210151",
        "myid": "6_2",
        "pid_title": "知识产权",
        "key_words": "咨询培训",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "耳鼻喉科用其他器械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "固化剂",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_3",
        "pid_title": "建筑建材",
        "key_words": "地板",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "化学纤维",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "检测设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_9",
        "pid_title": "工业制造",
        "key_words": "工业自动化仪表",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_6",
        "pid_title": "文化创意",
        "key_words": "纪念收藏品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "扎染",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "调节器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "化工设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "电动、液压手术台",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_4",
        "pid_title": "网络电信",
        "key_words": "网络设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "自行车",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "羧酸衍生物 ",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "粮食",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "液压气动元件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "电感器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "塑料包装",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "制剂辅料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "变压器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "节电设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "针织设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "周转箱",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_1",
        "pid_title": "医疗康养",
        "key_words": "医药包装",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "水质分析仪",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "其它金属加工机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "乘用车",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "肌电诊断仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "防护手套",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "其他化学原料药",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "其他环保设备",
        "id": ""
    }, 
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "办事处",
        "id": ""
    },{
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "工业园区",
        "id": ""
    },{
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "产业园区",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "科技园区",
        "id": ""
    }, 
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "科创园区",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "产业园",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "轮式拖拉机",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "无机酸",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "添加剂",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "提升设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "原料药机械设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "塑料助剂",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "发动系统",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "植物提取物",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "波谱仪",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "食品药品检定研究院",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "中国疾病预防控制中心",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "考试系统",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "元素分析仪",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "机房",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "生物分离系统",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "仪器及内窥镜设备",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_6",
        "pid_title": "文化创意",
        "key_words": "工艺品",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用X射线管、管组件或源组件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "飞机及配件",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "建筑管材",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用高能射线治疗设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "内燃机及配件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "广告促销礼品 ",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "通用塑胶",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "节庆用品",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "公路工程",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "支护机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "工业安全仪器",
        "id": ""
    },
    {
        "mypid": "8",
        "id_title": "",
        "pid": "1708271201536210153",
        "myid": "8_5",
        "pid_title": "金融投资",
        "key_words": "金融保险",
        "id": ""
    },
    {
        "mypid": "8",
        "id_title": "",
        "pid": "1708271201536210153",
        "myid": "8_5",
        "pid_title": "金融投资",
        "key_words": "招商",
        "id": ""
    },
    {
        "mypid": "8",
        "id_title": "",
        "pid": "1708271201536210153",
        "myid": "8_5",
        "pid_title": "金融投资",
        "key_words": "PPP",
        "id": ""
    }, {
        "mypid": "8",
        "id_title": "",
        "pid": "1708271201536210153",
        "myid": "8_5",
        "pid_title": "金融投资",
        "key_words": "ppp",
        "id": ""
    },
    {
        "mypid": "3",
        "id_title": "",
        "pid": "1708271201504590140",
        "myid": "3_6",
        "pid_title": "土地开发",
        "key_words": "房产物业",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_2",
        "pid_title": "医疗康养",
        "key_words": "调节水盐",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_1",
        "pid_title": "网络电信",
        "key_words": "软件",
        "id": ""
    }, 
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_1",
        "pid_title": "网络电信",
        "key_words": "笔记本",
        "id": ""
    }, 
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_1",
        "pid_title": "网络电信",
        "key_words": "采集系统",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_1",
        "pid_title": "医疗康养",
        "key_words": "外科用药及消毒防腐",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "X射线仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "合成橡胶",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "金属制品加工设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "药用粉碎机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "办公家具",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "美容化妆",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_2",
        "pid_title": "矿产能源",
        "key_words": "电气",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "锅炉及原动机",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "煤炭行业专用仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "橡胶加工专用设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_2",
        "pid_title": "医疗康养",
        "key_words": "消化系统用制剂",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_2",
        "pid_title": "矿产能源",
        "key_words": "电位器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "检测仪",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "天线",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "办公耗材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "玩具",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_1",
        "pid_title": "医疗康养",
        "key_words": "血液系统药物",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_3",
        "pid_title": "建筑建材",
        "key_words": "装饰装修",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "仪表",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "工程建筑专用机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "机床及其附件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "地质勘查设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "理疗仪器",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "五金工具",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_2",
        "pid_title": "农业水利",
        "key_words": "豆制品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "机械量仪表",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "船用发动机配件",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "不锈钢材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "脑电诊断仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "质谱仪",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "畜牧机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "包装制品",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "政府采购",
        "id": ""
    },  
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "预警信息发布中心",
        "id": ""
    }, 
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "经济开发区",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_4",
        "pid_title": "农业水利",
        "key_words": "农用工具",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_1",
        "pid_title": "矿产能源",
        "key_words": "常用有色金属",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "电热材料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "橡胶管",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "疾病预防控制中心",
        "id": ""
    },{
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "水资源局",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "核辐射测量仪器",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "病理分析前处理设备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "家具五金",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "普通诊察器械",
        "id": ""
    },
    {
        "mypid": "14",
        "id_title": "",
        "pid": "1708271201536210156",
        "myid": "14_4",
        "pid_title": "旅游开发",
        "key_words": "教育",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "泵",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "建筑钢材",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "市政工程",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "水厂",
        "id": ""
    }, 
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "停车场",
        "id": ""
    },{
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "收容所",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "注油枪",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "常委",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "钟表计时仪器",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "手术灯",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_3",
        "pid_title": "矿产能源",
        "key_words": "热力生产及供应",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "警察",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_1",
        "pid_title": "文化创意",
        "key_words": "央视",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_6",
        "pid_title": "文化创意",
        "key_words": "金属工艺品 ",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "五金锁具",
        "id": ""
    }, {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "办公楼",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "方便食品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "物位仪表",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "婴儿保育设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "光学显微镜",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "电视机",
        "id": ""
    },
    {
        "mypid": "14",
        "id_title": "",
        "pid": "1708271201536210156",
        "myid": "14_4",
        "pid_title": "旅游开发",
        "key_words": "文化",
        "id": ""
    },
     {
        "mypid": "14",
        "id_title": "",
        "pid": "1708271201536210156",
        "myid": "14_4",
        "pid_title": "旅游开发",
        "key_words": "游乐园",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "外科用",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_2",
        "pid_title": "矿产能源",
        "key_words": "国家电网",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "扳手 ",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_1",
        "pid_title": "网络电信",
        "key_words": "医用软件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "空调设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "压力机",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "导航气象天文海洋仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "传热设备",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "民政部",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_1",
        "pid_title": "交通运输",
        "key_words": "运输 ",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_2",
        "pid_title": "矿产能源",
        "key_words": "天然气",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_2",
        "pid_title": "矿产能源",
        "key_words": "送变电",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "管道系统",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "机械设备",
        "id": ""
    },
     {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "机电",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "面具",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "机床",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "试验机",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "温度仪表",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "水处理",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "吸附剂",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "基础外科用钳",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "色谱仪",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "信号发生器",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_6",
        "pid_title": "文化创意",
        "key_words": "陶瓷工艺品",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_5",
        "pid_title": "交通运输",
        "key_words": "物流服务",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "转向系统",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_5",
        "pid_title": "市政建设",
        "key_words": "林木园艺",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "放射性核素诊断设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "印刷",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "反光器具",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "口腔用钳",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "光谱诊断设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "无创监护仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "食品饮料烟草加工设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "装饰用纺织品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "工程塑胶",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "集中控制装置",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "肉制品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "电子电工制造设备",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_1",
        "pid_title": "网络电信",
        "key_words": "科研技术和地质勘查",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_2",
        "pid_title": "网络电信",
        "key_words": "通信辅助",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_5",
        "pid_title": "医疗康养",
        "key_words": "血气分析系统",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "金属加工机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "家用电器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "量具",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "呼吸护具",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "公共环卫设施",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "通用五金配件",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "铁路工程",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "纺织配套器材",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "油墨",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_4",
        "pid_title": "农业水利",
        "key_words": "化学肥料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "饮片机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "生物识别设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "制冷",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "IT",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "织机设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "服装机械",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "软化水设备",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "污水处理成套设备",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_5",
        "pid_title": "市政建设",
        "key_words": "林木",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_3",
        "pid_title": "矿产能源",
        "key_words": "煤矿",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用射线防护用品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "物性测试仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "食品包装",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "纸包装制品",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_1",
        "pid_title": "矿产能源",
        "key_words": "优特钢",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "地质科学院",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "其它服装",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "水利",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "X射线手术影像设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "其它非机动车",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_5",
        "pid_title": "医疗康养",
        "key_words": "尿液分析系统",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "固体废弃物处理设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "干燥设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "显示仪表",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "脱硫除尘设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "娱乐视听设备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "涂料乳液及成膜物质",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "导丝和管鞘",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "锅炉及辅助设备",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_3",
        "pid_title": "农业水利",
        "key_words": "农产品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "铲运机械",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "血液化验设备和器具",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "公共设施管理",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "洗衣机",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "工程施工",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "激光手术和治疗设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "有机化工原料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "农副食品加工设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_2",
        "pid_title": "医疗康养",
        "key_words": "电解质及酸碱平衡药",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "维修设备",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "公安局",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_3",
        "pid_title": "建筑建材",
        "key_words": "灯具",
        "id": ""
    },
    {
        "mypid": "14",
        "id_title": "",
        "pid": "1708271201536210156",
        "myid": "14_4",
        "pid_title": "旅游开发",
        "key_words": "户外用品",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "互联网",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_2",
        "pid_title": "农业水利",
        "key_words": "饲料加工设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "齿轮",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "热水器",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "心血管系统药物",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_1",
        "pid_title": "建筑建材",
        "key_words": "沼气设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用光学仪器配件及附件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "酯类",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "工控系统及装置",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "钢管",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "道路工程",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "药物检测设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "手术用及诊断用显微设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "造纸用助剂",
        "id": ""
    },
    {
        "mypid": "7",
        "id_title": "",
        "pid": "1708271201536210152",
        "myid": "7_1",
        "pid_title": "文化创意",
        "key_words": "传媒广电",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医用X射线设备",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_1",
        "pid_title": "交通运输",
        "key_words": "输送设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "医疗器械设备",
        "id": ""
    },
    {
        "mypid": "1",
        "id_title": "",
        "pid": "1708271201504590139",
        "myid": "1",
        "pid_title": "政府招标",
        "key_words": "国土资源部",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "彩色超声成像设备及超声介入",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "阀门",
        "id": ""
    },
     {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "大厦",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_3",
        "pid_title": "网络电信",
        "key_words": "计算机",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "体温计",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_1",
        "pid_title": "市政建设",
        "key_words": "其他劳保用品",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "保险元器件",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "电工陶瓷材料",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "腔内诊断设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "其它家居类",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_10",
        "pid_title": "工业制造",
        "key_words": "光电子、激光仪器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "塑料模具",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "矫形（骨科）外科用钳",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_3",
        "pid_title": "交通运输",
        "key_words": "水运工程",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "电阻器",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "非机动车",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "色标、色卡 ",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_3",
        "pid_title": "矿产能源",
        "key_words": "石油焦",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "空调",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "其他医用设备",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "手术及急救装置",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_13",
        "pid_title": "工业制造",
        "key_words": "办公设备",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_3",
        "pid_title": "农业水利",
        "key_words": "生鲜水果",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "轴承",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "船舶",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_5",
        "pid_title": "交通运输",
        "key_words": "仓储设备 ",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_5",
        "pid_title": "农业水利",
        "key_words": "水利工程",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_12",
        "pid_title": "工业制造",
        "key_words": "家具",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "密封件、连接件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_3",
        "pid_title": "工业制造",
        "key_words": "数码产品",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "中医器具",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "基础外科用刀",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "制剂机械",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_1",
        "pid_title": "农业水利",
        "key_words": "甜味剂",
        "id": ""
    },
    {
        "mypid": "9",
        "id_title": "",
        "pid": "1706231226562740018",
        "myid": "9_1",
        "pid_title": "交通运输",
        "key_words": "其他专用汽车",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_4",
        "pid_title": "建筑建材",
        "key_words": "五金其他",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_1",
        "pid_title": "网络电信",
        "key_words": "物探遥感",
        "id": ""
    },
    {
        "mypid": "11",
        "id_title": "",
        "pid": "1708271201536210154",
        "myid": "11_2",
        "pid_title": "网络电信",
        "key_words": "移动通信设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_11",
        "pid_title": "工业制造",
        "key_words": "其他包装材料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "有色金属合金",
        "id": ""
    },
    {
        "mypid": "10",
        "id_title": "",
        "pid": "1708271201504590143",
        "myid": "10_2",
        "pid_title": "农业水利",
        "key_words": "肉类",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "睡眠呼吸治疗系统",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_1",
        "pid_title": "矿产能源",
        "key_words": "有色金属矿产",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "合成树脂",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "防护鞋",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_1",
        "pid_title": "矿产能源",
        "key_words": "工业电炉",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "汽轮机及辅机",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_4",
        "pid_title": "工业制造",
        "key_words": "模具",
        "id": ""
    },
    {
        "mypid": "2",
        "id_title": "",
        "pid": "1708271201536210150",
        "myid": "2_3",
        "pid_title": "市政建设",
        "key_words": "环境监测仪器仪表",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_5",
        "pid_title": "工业制造",
        "key_words": "分子生物",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "运动服装",
        "id": ""
    },
    {
        "mypid": "5",
        "id_title": "",
        "pid": "1708271201504590142",
        "myid": "5_3",
        "pid_title": "矿产能源",
        "key_words": "石油燃料",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_1",
        "pid_title": "工业制造",
        "key_words": "烟草加工设备",
        "id": ""
    },
    {
        "mypid": "13",
        "id_title": "",
        "pid": "1708271201536210155",
        "myid": "13_2",
        "pid_title": "建筑建材",
        "key_words": "切割设备",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_8",
        "pid_title": "工业制造",
        "key_words": "摩托车",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_6",
        "pid_title": "工业制造",
        "key_words": "机床附件",
        "id": ""
    },
    {
        "mypid": "12",
        "id_title": "",
        "pid": "1708271201504590144",
        "myid": "12_2",
        "pid_title": "工业制造",
        "key_words": "针织面料 ",
        "id": ""
    },
    {
        "mypid": "4",
        "id_title": "",
        "pid": "1708271201504590141",
        "myid": "4_3",
        "pid_title": "医疗康养",
        "key_words": "诊断仪器",
        "id": ""
    },
    
    
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "制服订制",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "地块",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "金融",
        "pid": "1708271201536210153",
        "id": ""
    },
     {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "融资",
        "pid": "1708271201536210153",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "彩票",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "液压",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "草籽",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "能源",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "畜牧",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "退耕",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "草原",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "化肥",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "制钠",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "液钠罐",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "液晶",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "液晶屏",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "变电站",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "自动化系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "高速公路",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "公路",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "铁路",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "航道",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "收费站",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "扫描仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "生产线",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "电磁阀",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "辊筒",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "焦化",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "混凝剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "活动承办",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "应急灯",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "大学",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "工服",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "宾馆",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "研究中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "商用飞机",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "验证系统",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "飞机",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "铁路局",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "混凝土",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "科研楼",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "碎石",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "运营服务",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "监理",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "媒体",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "宣传",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "媒体宣传",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "电影",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "电视",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "自控系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "油库",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "石油",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "中煤",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "电厂",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "信息系统",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "桥",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "包装",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "红外热像仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "公共服务中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "激光切割机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "激光",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "切割机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "中国航天",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "能源站",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "燃气",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "微生物研究所",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "核酸",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "提取系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "色谱系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "装修",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "改造装修",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "风电",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "配电工程",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "基地建设",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "码头",
        "pid": "1708271201536210150",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "环卫",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "海事局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "中国外文局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "装饰",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "酒店",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "客房",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "水库",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "灌区",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "干渠",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "灌区干渠",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "玻璃钢",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "砂管",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "中核",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "电缆",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "集控中心",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "电力公司",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "博物馆",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "产权房",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "全国代表大会",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "管理系统",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "楼内改造",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "压力表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "人行道",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "城墙维修",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "人民政府",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "政务服务",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "业务系统",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "速凝剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "货梯",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "电梯",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "扶梯",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "升降机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "插座",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "芯片",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "热电",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "精密仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "光明日报",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "日报",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "网络安全",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "无线网络",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "海岸",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "显微镜",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "绿化补植",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "绿化",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "运输",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "南水北调",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "商铺",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "镀膜系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "发动机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "电机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "税务局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "液氧药剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "防洪",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "城市管理局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "汽车租赁",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "汽车制造",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "机场",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "光缆",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "包装线",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "有线电视",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "地铁",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "飞机制造",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "电线",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "不锈钢",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "除锈机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "治疗仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "周转用房",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "煤电",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "饭店",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "宗教事务局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "煤炭",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "道路建设",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "湿地",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "河段",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "学校",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "迁建",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "监狱",
        "pid": "1708271201504590139",
        "id": ""
    },
     {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "林管局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "租用土地",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "复垦施工",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "搬迁安置",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "退耕还林",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "河道",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "广播电视",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "高压线路",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "公路局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "公安厅",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "交通管理局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "活性炭",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "大坝",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "学院",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "净水设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "物业",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "社区管理服务中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "楼工程总承包",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "交通运输局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "公路建设",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "看守所",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "物资采购所",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "甲醇",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "垃圾处理厂",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "工商和质量监督管理局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "造林",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "学校",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "烈士陵园",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "烈士纪念馆",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "林业",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "旱地",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "水田",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "住房公积金",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "博物院",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "道路改造",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "科学技术馆",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "城中村改造",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "供水",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "监测监控设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "监测设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "监控设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "农业委员会",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "民政局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "国道",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "保险",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "垃圾清运",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "旅游区",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "林场",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "运动管理中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农田建设",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "财政局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "物流",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "蔬菜",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "种植",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "街道办事处",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "国家城市能源计量中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "棚户区改造",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "GPS",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "市政",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "语言文字",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "音频",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "视频",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "出版物",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "视频",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "建筑物施工",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "房屋管理局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "大桥改造",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "宿舍",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "城乡建设委员会",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "戒毒所",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "有机",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "扶贫搬迁",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "房屋交易权属登记管理中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "城墙管理处",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "车辆管理所",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "征地",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "国土资源局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "机关事务管理服务中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "供电局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "处司法",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "中科院",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "垃圾站",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "基础设施",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "烟草公司",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "配电设施",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "商务厅",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "旅游",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "购物节",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "酒店",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "联通",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "营业厅",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "基建",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "药品",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "药品检验所",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "土地局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "规划局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "建设局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公寓",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "房屋设施",
        "pid": "1708271201536210155",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "五金",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "棚户区",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "电梯",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "司法厅",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "文艺",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "演出",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "民政厅",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "公众号",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "查询服务",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "小学",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "实验室",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "货运部",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "身份证",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "公共服务",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "检验试剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "大学",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "草皮",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "烟草总公司",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "移动应用",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "绿化",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "绿化树池",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "国土资源局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "建设用地",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "商业用地",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "挂牌出让",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "财政局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "幼儿园",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "中学",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "宿舍",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "人民政府",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "道路",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "供热",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "热力站",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "玻璃钢水",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "绿地",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "教学楼",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "山林",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "吃水",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "河道",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "河道治理",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "养殖",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公交车站",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "档案馆",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "生态旅游",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "学校",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "大棚",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "观光道路",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "园林景观",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "事务管理局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "机关",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农业",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "轨道交通",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "福利院",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "换热站",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "税务局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "会议室",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "职场装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "职业装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "轻轨站台",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "火车站",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "物流园",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "药品检验",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "仪器设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "森林",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "火险区",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "公务用车",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "防汛",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "秋冬播",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "种子",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "装修",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农业",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "精神病院",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "疗养",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "病房",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "运动场",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "会展中心",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "配电",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "制服",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "路灯",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "住房保障局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "垃圾车",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "垃圾箱",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "城市规划",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "大道",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "制胶厂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "经济技术开发区",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "科技创业园",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "公积金",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "面貌提升",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "河道护岸",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "垃圾清运",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农田",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "城中村改造",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "保障房",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "交通安全",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "中心城区",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "消防车",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "财政局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农民",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "综合楼",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "绿色食品产业园",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "房屋拆除",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "妇幼保健",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "眼底筛查仪",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "公路",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "学院",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "供暖",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "矿产",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "古窑址保护",
        "pid": "1708271201536210152",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "剧本",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "文物",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "文体活动",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "校园硬化",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "科技园",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "武警",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "疫情",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "铁路局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "防洪",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "公车",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "产业服务中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "物流产业园",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "街路",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "收割机",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "插秧机",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "避险安置",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "网络教室",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建筑石料",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "活动中心",
        "pid": "1708271201536210152",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "健身",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "厂房",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "管理局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "智慧",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "殡葬管理所",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "电力",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "路面",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "联合国",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "养老",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "水泥路",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "残疾人联合会",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "农业局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "检察院",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "市政设施",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "供水",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "扶贫",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "治疗仪",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "真空镀膜机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "林荫道",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "河道整治",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "纹饰仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "景观",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "科技创新中心",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "特别保护区",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "修缮保护",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公墓",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "新闻出版广电局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "公安消防大队",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "视频会议系统",
        "pid": "1708271201536210154",
        "id": ""
    },
     {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "电脑",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "服务器",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "法院",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "演播室",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "水泥路",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "柏油路",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "安置房",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "商业中心",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "生态绿化",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "新能源汽车",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "康复中心",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "污水设施",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "羊",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "硬化路",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "敬老院",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "救助",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "活动场所",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "公共卫生服务中心",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "饮水",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "立交桥",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "林场",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "办公用房",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "消防",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "农牧局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "教学设备",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "数字化",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "学生",
        "pid": "1708271201536210150",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "城管",
        "pid": "1708271201536210150",
        "id": ""
    },
    
    
    
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "自来水",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "绿道",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "周转房",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "数控",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "船",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "铝合金",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "支队",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "司法局",
        "pid": "1708271201504590139",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "拘留所",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建设项目",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "景区",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "硬化",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "电杆",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "蓄滞洪区",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "大数据",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "地下通道",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "小区",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "土地整治",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "水务局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "健身中心",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "草坪",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "耕地",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "红十字会",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "锅炉",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "污水",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "排水",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "五保",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "支付",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "行政执法",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "执法局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "新农村",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "委员会",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "廉租房",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "市委",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "州委",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "县委",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "渔业",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "河治理",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "河道治理",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "土地",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "业务用房",
        "pid": "1708271201536210155",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "铁管",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "发展和改革委员会",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "发改委",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "水系",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "废旧物资",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "农村综合服务平台",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "工商局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "菜",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "托养",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "安置住宅",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "智能化",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "重点段治理",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "童装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "示范村",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "取暖煤",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "堤防",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "就业服务中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "卫生院",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "电信",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "钢柱",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "钢梁",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公交中心",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "商务中心",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "城市绿墙",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "管廊",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "风沙",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "灌溉",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "山洪",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "游客",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "观景平台",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "户外运动",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "用房",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "河流",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "水土保持",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "通村路",
        "pid": "1706231226562740018",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "航空",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "水治理",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "树木移植",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "乔木移植",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "生活垃圾",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "人力资源和社会保障局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "饮用水",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "人社局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "网站",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "流域",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医疗",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "鱼种",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "疾控中心",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "涝点",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "遗址",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "综合服务平台",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农牧业",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "干线",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "交通枢纽",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "广场",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "汽车",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "电车",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "驾驶系统",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "政府购买",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "煤厂",
        "pid": "1708271201504590142",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "成品油",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "铁",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "剧院",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "体彩网",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "苗木移植",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "生产调度",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "医疗",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "园林管理中心",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "采暖系统",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "炼铁",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "炼刚",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "钢铁",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "污水再生",
        "pid": "1708271201536210150",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "工业区",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "污水处理",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "废水",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "数控",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "房屋征收",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "工业制造",
        "key_words": "显示屏",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "监察委员会",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "地质灾害",
        "pid": "1708271201504590139",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "恢复重建",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "烟叶公司",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "污水",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "高铁",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "林业局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "社会保障局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "电业局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "菜市场",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "垃圾中转站",
        "pid": "1708271201536210150",
        "id": ""
    }
]


"""

"""
bussiness 商机分类关键字字典
title  商机文章标题
context 商机文章内容

返回字典{
business_pid_1："12,4", 商机分类的大类
business_id_1:"12_1,4_2" 商机分类的小类

}
"""

def business_predict(jsonstr,title,default_pid='1708271201536210157'):

    predict_pid =set()
    predict_id =set()
    json_ob=json.loads(jsonstr)
    # print len(json_ob)
    if title ==None:
        title=""

    for jsob in json_ob:
        if jsob['key_words'] in title:
             # print jsob['key_words']
             pid= jsob['pid']
             # pid= jsob['pid_title']
             id= jsob['id']
             predict_pid.add(pid)
             predict_id.add(id)

    # print  len(predict_pid)
    if len(predict_pid)==0:
        predict_pid.add(default_pid)
        # print title


    # if len(predict_id) == 0:
    #     predict_id.add(default_pid)
    pid_str=','.join(predict_pid)
    id_str=','.join(predict_id)
    predict_dic={"business_pid_1":pid_str,"business_id_1":id_str}

    # print  title,pid_str


    return predict_dic

# 链接数据库







