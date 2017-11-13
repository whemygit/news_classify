#!/usr/bin/env python
# -- coding: utf-8 --
import HTMLParser
import re
import sys
import json
import time

import MySQLdb
import datetime

reload(sys)
sys.setdefaultencoding('utf8')



jsonstr="""

[
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "楼宇招租",
        "pid": "1708271201504590140",
        "id": ""
    },
    
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "地产",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "物业",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "房屋开发",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "经济适用",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "住房",
        "pid": "1708271201504590140",
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
        "pid_title": "土地开发",
        "key_words": "房产物业",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "地块出让",
        "pid": "1708271201504590140",
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
        "pid_title": "土地开发",
        "key_words": "廉租房",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "楼宇改造",
        "pid": "1708271201504590140",
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
        "pid_title": "市政建设",
        "key_words": "土地开发",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "路大修",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "植物园",
        "pid": "1708271201536210150",
        "id": ""
    },
    
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "专项整治",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "生态区建设",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "标段",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "移民安置",
        "pid": "1708271201536210150",
        "id": ""
    },
    
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "气源站",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "组委会",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "便民服务中心",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "商城",
        "pid": "1708271201536210150",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "索道",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "资源配置",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "特色小镇",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "美丽乡村",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "送气下乡",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "青少年宫",
        "pid": "1708271201536210150",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "树补植",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "足球场",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "园林管理所",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "厕所",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公共资源",
        "pid": "1708271201536210150",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "产业基地",
        "pid": "1708271201536210150",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "居民搬迁",
        "pid": "1708271201536210150",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "老城区",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "城乡一体化",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "文化中心",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "水生态",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "经济合作区",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "花园建设",
        "pid": "1708271201536210150",
        "id": ""
    },
    
     {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "环城林",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "图书馆",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "租用土地",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "建筑施工",
        "pid": "1708271201504590140",
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
        "key_words": "工业用地",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "旅游用地",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "划拨用地",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "军事用地",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "学校用地",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "学校建设",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "挂拍出让",
        "pid": "1708271201504590140",
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
        "pid_title": "土地开发",
        "key_words": "土地拍卖",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "军民融合",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "厂房招租",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "使用权转让",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "宅基地",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "红线图",
        "pid": "1708271201504590140",
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
        "key_words": "用地性质",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "土地招标",
        "pid": "1708271201504590140",
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
        "pid_title": "土地开发",
        "key_words": "工业园",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "土地流转",
        "pid": "1708271201504590140",
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
        "pid_title": "土地开发",
        "key_words": "土地填埋",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "垃圾场处理",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "挂拍",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "联合开发",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "房产管理",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "商业运营",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "使用年限",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "土地确权",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "土地使用许可证",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "房屋销售许可证",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "土地开发",
        "key_words": "建设许可证",
        "pid": "1708271201504590140",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "型材",
        "pid": "1708271201536210155",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "室内装饰",
        "pid": "1708271201536210155",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "钢丝绳",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "五金",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "五金",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建筑粘合剂",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "石材石料",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "金属制品",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "玻璃纤维",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "覆铜板材料",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "木材板材",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "锁具",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "电线电缆",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建筑玻璃",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "电焊",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "机械五金",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "橡胶片",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "隔断吊顶",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "门窗",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "接插件",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "水泥砖瓦",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建筑设备",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "弹簧",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "刀",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "钳子",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "起钉器",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "丝锥、板牙",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "橡胶板",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建材",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "板材",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建筑陶瓷",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "日用五金",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "装配电动工具",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "门窗五金",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "塑料管",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "管件",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "撬棍",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建筑工程",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "楼梯电梯",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "水暖五金",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建材涂料",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "装饰五金",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "管材",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "螺丝刀",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "涂料",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "地板",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建筑管材",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "装饰装修",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "五金工具",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "不锈钢材",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "电热材料",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "家具五金",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建筑钢材",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "五金锁具",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "办公楼",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "扳手",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "通用五金配件",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "涂料乳液及成膜物质",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "导丝和管鞘",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "灯具",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "沼气设备",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "钢管",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "阀门",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "大厦",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "电工陶瓷材料",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "五金其他",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "切割设备",
        "pid": "1708271201536210155",
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
        "pid_title": "建筑建材",
        "key_words": "基地建设",
        "pid": "1708271201536210155",
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
        "pid_title": "建筑建材",
        "key_words": "电缆",
        "pid": "1708271201536210155",
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
        "pid_title": "建筑建材",
        "key_words": "楼工程",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "房屋设施",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "五金",
        "pid": "1708271201536210155",
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
        "pid_title": "建筑建材",
        "key_words": "宿舍",
        "pid": "1708271201536210155",
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
        "pid_title": "建筑建材",
        "key_words": "装修",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "装潢",
        "pid": "1708271201536210155",
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
        "pid_title": "建筑建材",
        "key_words": "房屋拆除",
        "pid": "1708271201536210155",
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
        "pid_title": "建筑建材",
        "key_words": "厂房",
        "pid": "1708271201536210155",
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
        "pid_title": "建筑建材",
        "key_words": "周转房",
        "pid": "1708271201536210155",
        "id": ""
    },
   
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "业务用房",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "铁管",
        "pid": "1708271201536210155",
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
        "pid_title": "建筑建材",
        "key_words": "管廊",
        "pid": "1708271201536210155",
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
        "pid_title": "建筑建材",
        "key_words": "采暖系统",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "砂石",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "空调",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "石材",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "大理石",
        "pid": "1708271201536210155",
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
        "pid_title": "建筑建材",
        "key_words": "建筑材料",
        "pid": "1708271201536210155",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "筑屋",
        "pid": "1708271201536210155",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "建筑建材",
        "key_words": "建筑",
        "pid": "1708271201536210155",
        "id": ""
    },
  
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "隧道",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "物流运输",
        "pid": "1706231226562740018",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "交通",
        "pid": "1706231226562740018",
        "id": ""
    },
    
     {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "直升机",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "储运设备",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "产品运输",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "集装箱",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "运输搬运设备",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "轨道交通设备器材",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "公交车",
        "pid": "1706231226562740018",
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
        "key_words": "火车",
        "pid": "1706231226562740018",
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
        "key_words": "商用车",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "运载车",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "救火车",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "消防车",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "物流服务",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "输送设备",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "水运工程",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "仓储设备",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "其他专用汽车",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "商用飞机",
        "pid": "1706231226562740018",
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
        "key_words": "航空",
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
        "pid_title": "交通运输",
        "key_words": "桥梁",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "涵洞",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "人行道",
        "pid": "1706231226562740018",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "人行步道",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "汽车租赁",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "地铁",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "路建设",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "物流",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "仓库",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "仓储",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "货运",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "道路",
        "pid": "1706231226562740018",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "省道",
        "pid": "1706231226562740018",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "乡道",
        "pid": "1706231226562740018",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "县道",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "大道",
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
        "key_words": "街路",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "林荫道",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "硬化路",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "船",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "通村路",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "航空",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "汽车",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "公交车",
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
        "pid_title": "交通运输",
        "key_words": "高铁",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "磁悬浮",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "列车",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "动车",
        "pid": "1706231226562740018",
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
        "pid_title": "交通运输",
        "key_words": "航道",
        "pid": "1706231226562740018",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "交通运输",
        "key_words": "口岸",
        "pid": "1706231226562740018",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "城市建设",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "应急中心",
        "pid": "1708271201536210150",
        "id": ""
    },
     {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "社区服务中心",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "搅拌站",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公共空间建设",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "生态社区",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "卫生站",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "灭火系统",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "两河水网",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "弱电改移",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "校区建设",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "防雷",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "大气治理",
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
        "key_words": "公共服务",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "卫生城市",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "园博园",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "污泥",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "大街",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "耐火防火材料",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "无缝管",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "空气净化",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "垃圾处理",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "绿化苗木",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "维护清洗",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "花卉",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "清洗设备",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "救生器材",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "防雷避雷",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公园",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "园林绿化",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "停车场设备",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "消防器材",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "生态监测",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "空气净化设备",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "生活饮用水处理设备",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "交通安全设备",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "园艺机械",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "环境",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "其他环保设备",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "工业园区",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "产业园区",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "科技园区",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "科创园区",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "产业园",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公路工程",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "市政工程",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "自来水厂",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "水厂",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "停车场",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "收容所",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "管道系统",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "水处理",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "林木园艺",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公共环卫设施",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "铁路工程",
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
        "key_words": "林木",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "水利",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "固体废弃物处理",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公共设施管理",
        "pid": "1708271201536210150",
        "id": ""
    },
   
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "道路工程",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "其他劳保用品",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "环境监测仪器仪表",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "博物馆",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "防洪",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "道路建设",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "搬迁安置",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "垃圾清运",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "配电设施",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "基建",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "棚户区",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "吃水",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "学校",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "运动场",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "路灯",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "面貌提升",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "城中村改造",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "消防车",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "避险安置",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "污水设施",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "消防",
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
        "pid_title": "市政建设",
        "key_words": "电杆",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "草坪",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "废旧物资",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "旧城改造",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "教育中心",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "托养",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "照明工程",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "群众服务",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "饮用水",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "政府购买",
        "pid": "1708271201536210150",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "路提级",
        "pid": "1708271201536210150",
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
        "pid_title": "市政建设",
        "key_words": "医疗",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "医院",
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
        "pid_title": "市政建设",
        "key_words": "房屋征收",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "恢复重建",
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
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "排污",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "无害化处理",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "节能",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "环保中心",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "发电厂",
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
        "pid_title": "市政建设",
        "key_words": "城市建设",
        "pid": "1708271201536210150",
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
        "key_words": "文化馆",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "体育馆",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "剧场",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "文化广场",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "卫星转播",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "批发市场",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "农贸市场",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "生态林",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "电视塔",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "汽车站",
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
        "key_words": "码头",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "机场",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "人行道",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "步行道",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "景观道",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "地下管廊",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "海绵城市",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "智慧城市",
        "pid": "1708271201536210150",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "污染防治",
        "pid": "1708271201536210150",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "政府招标",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "行政审批局",
        "pid": "1708271201504590139",
        "id": ""
    },
    
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "试点村",
        "pid": "1708271201504590139",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "反腐倡廉",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "空管站",
        "pid": "1708271201504590139",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "安全生产科学研究院",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "国家发展改革委价监局",
        "pid": "1708271201504590139",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "财政",
        "pid": "1708271201504590139",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "城镇化",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "政务中心",
        "pid": "1708271201504590139",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "体育局",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "保税区",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "农林局",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "房产信息中心",
        "pid": "1708271201504590139",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "执法",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "文化局",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "教育局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "地震局",
        "pid": "1708271201504590139",
        "id": ""
    },
   
   

    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "出入境检验检疫局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "行政服务中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "扶贫基金",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "海洋技术中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "文物局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "国税",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "地税",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "商务部",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "出入境",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "边防检查站",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "部队",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "国家机关",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "财政部",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "研究所",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "专利局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "高新区",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "食品药品检定研究院",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "中国疾病预防控制中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "政府采购",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "预警信息发布中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "经济开发区",
        "pid": "1708271201504590139",
        "id": ""
    }, 
      {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "应急指挥中心",
        "pid": "1708271201504590139",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "经济区",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "疾病预防控制中心",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "水资源局",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "常委",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "警察",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "民政部",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "地质科学院",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "公安",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "国土资源部",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "研究中心",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "微生物研究所",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "中核",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "政务服务",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "城市管理局",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "学院",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "交通运输局",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "交通局",
        "pid": "1708271201504590139",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "气象局",
        "pid": "1708271201504590139",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "档案局",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "博物院",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "运动管理中心",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "市政",
        "pid": "1708271201504590139",
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
        "key_words": "司法",
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
        "pid_title": "政府招标",
        "key_words": "烟草公司",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "司法厅",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "烟草总公司",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "人民政府",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "税务局",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "住房保障局",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "保障房",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "财政局",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "管理局",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "联合国",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "扶贫",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "法院",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "扶贫",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "水务局",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "五保",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "行政执法",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "执法局",
        "pid": "1708271201504590139",
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
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "发改局",
        "pid": "1708271201504590139",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "发展和改革局",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "安置住宅",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "就业服务中心",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "人力资源和社会保障局",
        "pid": "1708271201504590139",
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
        "pid_title": "政府招标",
        "key_words": "综合服务平台",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "监察委员会",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "地质灾害",
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
        "pid_title": "政府招标",
        "key_words": "幼儿园",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "信号灯",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "指挥系统",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "维修",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "信息系统",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "家具采购",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "电脑",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "显示屏",
        "pid": "1708271201504590139",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "交换设备",
        "pid": "1708271201536210154",
        "id": ""
    },   {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "导视系统",
        "pid": "1708271201536210154",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "通信系统",
        "pid": "1708271201536210154",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "信息化",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "网络通信",
        "pid": "1708271201536210154",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "网络通信",
        "pid": "1708271201536210154",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "视联网",
        "pid": "1708271201536210154",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "数据整合",
        "pid": "1708271201536210154",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "硬件",
        "pid": "1708271201536210154",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "城域网",
        "pid": "1708271201536210154",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "数据处理",
        "pid": "1708271201536210154",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "地理信息",
        "pid": "1708271201536210154",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "物联网",
        "pid": "1708271201536210154",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "信息平台",
        "pid": "1708271201536210154",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "预检系统",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "识别系统",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "智慧城市",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "半导体材料",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "软件",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "系统集成",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "安全检测设备",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "DPU",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "网络工程",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "数据中心",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "数据采集",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "传输设备",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "通信线缆",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "电信工程",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "信息安全设备",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "防伪技术产品",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "软件开发",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "门禁考勤对讲",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "软件服务",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "信息化建设",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "通讯产品",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "手机及配件",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "数据库",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "其它安全防护类",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "接入设备",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "管理平台",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "警用装备",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "电话机系列",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "网络设备",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "考试系统",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "机房",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "软件",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "笔记本电脑",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "采集系统",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "天线",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "软件",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "科研技术和地质勘查",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "通信辅助",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "互联网",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "计算机",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "物探遥感",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "移动通信设备",
        "pid": "1708271201536210154",
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
        "pid_title": "网络电信",
        "key_words": "信息系统",
        "pid": "1708271201536210154",
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
        "pid_title": "网络电信",
        "key_words": "业务系统",
        "pid": "1708271201536210154",
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
        "pid_title": "网络电信",
        "key_words": "GPS",
        "pid": "1708271201536210154",
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
        "pid_title": "网络电信",
        "key_words": "移动应用",
        "pid": "1708271201536210154",
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
        "pid_title": "网络电信",
        "key_words": "智慧",
        "pid": "1708271201536210154",
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
        "pid_title": "网络电信",
        "key_words": "数字化",
        "pid": "1708271201536210154",
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
        "pid_title": "网络电信",
        "key_words": "大数据",
        "pid": "1708271201536210154",
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
        "pid_title": "网络电信",
        "key_words": "电信",
        "pid": "1708271201536210154",
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
        "pid_title": "网络电信",
        "key_words": "体彩网",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "防火墙",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "空间一体化",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "北斗",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "卫星应用",
        "pid": "1708271201536210154",
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
        "key_words": "网络病毒",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "互联网",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "移动网络",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "网络电信",
        "key_words": "APP",
        "pid": "1708271201536210154",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "铜",
        "pid": "1708271201504590142",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "矿业",
        "pid": "1708271201504590142",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "千伏",
        "pid": "1708271201504590142",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "采砂场",
        "pid": "1708271201504590142",
        "id": ""
    },  
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "电力",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "加油站",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "采矿",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "金属粉末",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "黑色金属矿产",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "选矿设备",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "中国石油",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "煤",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "金属",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "铁合金",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "能源工程",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "钢",
        "pid": "1708271201504590142",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "铁",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "水电",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "新能源",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "电力供应",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "低压电器",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "气体",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "其他钢铁产品",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "发电",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "煤制品",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "石油设备",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "超声换能器",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "太阳能设备",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "采煤机",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "其它能源",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "电气",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "电位器",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "常用有色金属",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "热力生产及供应",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "国家电网",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "天然气",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "送变电",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "煤矿",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "优特钢",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "石油焦",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "有色金属矿产",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "工业电炉",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "石油燃料",
        "pid": "1708271201504590142",
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
        "pid_title": "矿产能源",
        "key_words": "变电站",
        "pid": "1708271201504590142",
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
        "pid_title": "矿产能源",
        "key_words": "电力公司",
        "pid": "1708271201504590142",
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
        "pid_title": "矿产能源",
        "key_words": "煤电",
        "pid": "1708271201504590142",
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
        "pid_title": "矿产能源",
        "key_words": "高压线路",
        "pid": "1708271201504590142",
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
        "pid_title": "矿产能源",
        "key_words": "炼铁",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "炼钢",
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
        "pid_title": "矿产能源",
        "key_words": "不锈钢",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "玉石",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "宝石",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "稀有金属",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "贵金属",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "钻石",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "翡翠",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "玛瑙",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "海底能源",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "干冰",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "天然气",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "新能源",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "太阳能",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "风能",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "地热",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "潮汐能",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "矿产设备",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "开采机械",
        "pid": "1708271201504590142",
        "id": ""
    },
           { "id_title": "",
        "pid_title": "矿产能源",
        "key_words": "冶炼",
        "pid": "1708271201504590142",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "新药开发",
        "pid": "1708271201504590141",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "超声诊断仪",
        "pid": "1708271201504590141",
        "id": ""
    },
      {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "生物医药",
        "pid": "1708271201504590141",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "制药",
        "pid": "1708271201504590141",
        "id": ""
    },  
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "度假村",
        "pid": "1708271201504590141",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "康养",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "养生",
        "pid": "1708271201504590141",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "藏药",
        "pid": "1708271201504590141",
        "id": ""
    },
     {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "救护车",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "新药批号",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医疗器械",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "执业牌照",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医养",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "便携式超声诊断设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "维生素及营养药",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用离心机",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "制药用水设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "输液辅助装置",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "超声辅助材料",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "药物检测专用仪器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "血流量测定装置及血容量测定装置",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "低温治疗仪器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "内窥镜",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "手术",
        "pid": "1708271201504590141",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "外科",
        "pid": "1708271201504590141",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "内科",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "心电诊断仪器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "感染类",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用超声仪器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用电子",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "眼科手术用其他器械",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "高频手术",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "基础外科用剪",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "听诊器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "X射线诊",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "消毒灭菌",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "血压计",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "电凝设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "呼吸设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "X射线计算机断层摄影设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "胸腔心血管外科用钳",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用磁共振设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "血管内导管",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "药用包装机械",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用制气设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "基础外科用镊夹",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "眼科光学仪器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "药包材检测设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "免疫分析系统",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "胸腔心血管外科用镊夹",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "血液净化设备和血液净化器具",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "临床检验仪器设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "床检验分析仪器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "诊察治疗设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "基因和生命科学仪器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "供氧系统",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用刺激器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "视力诊察器具",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "手动手术台床",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "其它消毒灭菌设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "妇科检查器械",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医疗设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "兽用药品",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用材料",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "电子内窥镜",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用缝合针",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "标牌",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "鼻腔止血器（清洗器）  医用光学器具",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "光学内窥镜及冷光源",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "注射穿刺器械",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "物理治疗设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "超声治疗设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "反应设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "牙科椅",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "抗肿癌药",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "血站",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "泌尿肛肠科用钳",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用化验和基础设备器具",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "矫形（骨科）外科用剪",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "植物原药材",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "一般医疗用品",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "输液、输血器具及管路",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用培养箱",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用X线影像系统及成像器件",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "紫外线灭菌灯",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "呼吸麻醉设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "臭氧消毒机",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "用于心脏的治疗、急救装置",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "中成药",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "保健食品",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "压力蒸汽灭菌设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "标签",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "病床",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "口腔综合治疗设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医院",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "消化系统药物",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "电疗仪器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "心电电极",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "耳鼻喉科用其他器械",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "检测设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "电动、液压手术台",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医药",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "肌电诊断仪器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "生物分离系统",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "仪器及内窥镜设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用X射线",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用高能射线治疗",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "调节水盐",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "外科用药及消毒防腐",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "X射线仪器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "药用粉碎机械",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "消化系统用制剂",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "血液系统药物",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "理疗仪器",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "病理分析前处理设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "普通诊察器械",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "手术灯",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "婴儿保育设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "光学显微镜",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "外科用",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "基础外科用钳",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "反光器具",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "口腔用钳",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "血气分析系统",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "呼吸护具",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用射线防护用品",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "X射线手术影像设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "尿液分析系统",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "血液化验设备和器具",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "激光手术和治疗设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "电解质及酸碱平衡药",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "心血管系统药物",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用光学仪器配件及附件",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "药物检测设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "手术用及诊断用显微设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医用X射线设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "医疗器械设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "彩色超声成像设备及超声介入",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "体温计",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "腔内诊断设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "矫形（骨科）外科用钳",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "其他医用设备",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "手术及急救装置",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "中医器具",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "基础外科用刀",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "睡眠呼吸治疗系统",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "诊断仪器",
        "pid": "1708271201504590141",
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
        "pid_title": "医疗康养",
        "key_words": "疫情",
        "pid": "1708271201504590141",
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
        "pid_title": "医疗康养",
        "key_words": "老年社区",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "残疾",
        "pid": "1708271201504590141",
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
        "pid_title": "医疗康养",
        "key_words": "康复中心",
        "pid": "1708271201504590141",
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
        "pid_title": "医疗康养",
        "key_words": "公共卫生服务中心",
        "pid": "1708271201504590141",
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
        "pid_title": "医疗康养",
        "key_words": "医疗",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "诊疗",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "灭菌器",
        "pid": "1708271201504590141",
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
        "pid_title": "医疗康养",
        "key_words": "干细胞",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "基因",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "转基因",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "疗养院",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "社保",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "医疗康养",
        "key_words": "影像",
        "pid": "1708271201504590141",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "教学专用仪器",
        "pid": "1708271201536210151",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "水产技术",
        "pid": "1708271201536210151",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "培育技术",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "注册专利",
        "pid": "1708271201536210151",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "图书",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "注册商标",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "专利",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "版权",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "转让专利",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "知识产权",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "著作权",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "版权转让",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "小说出版",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "影视制作",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "电影",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "影视发行",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "肖像权",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "出版",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "电子出版",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "培训",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "品牌转让",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "专利交易",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "国际专利",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "专利侵权",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "商标",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "商标转让",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "国际注册",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "管理系统",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "外观专利",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "外观设计",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "专利服务",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "注册服务",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "知识产权",
        "key_words": "注册代理",
        "pid": "1708271201536210151",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "其他类别",
        "key_words": "火葬",
        "pid": "1708271201536210157",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "其他类别",
        "key_words": "殡葬",
        "pid": "1708271201536210157",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "其他类别",
        "key_words": "墓地",
        "pid": "1708271201536210157",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "其他类别",
        "key_words": "公墓",
        "pid": "1708271201536210157",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "其他类别",
        "key_words": "租赁",
        "pid": "1708271201536210157",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "其他类别",
        "key_words": "展览展示",
        "pid": "1708271201536210157",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "其他类别",
        "key_words": "航空航天",
        "pid": "1708271201536210157",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "食用菌",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "茉莉花",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "香菇",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "蜜柚",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "麻竹",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "养殖",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "猪",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "小龙虾",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "山药",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "灌渠",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "草场",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "桃",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "果林",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "蚕",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "血橙",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "桐子",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "畜产品",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "屠宰场",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "槟郎",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "食用油",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "植物资源",
        "pid": "1708271201504590143",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "青稞",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "果园",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农副产品",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "沟渠",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "疏浚",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "清淤",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "塘坝",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农作物",
        "pid": "1708271201504590143",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "湖段治理",
        "pid": "1708271201504590143",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "水稻",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "牛",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "果蔬",
        "pid": "1708271201504590143",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "牡丹",
        "pid": "1708271201504590143",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "蚕桑",
        "pid": "1708271201504590143",
        "id": ""
    }, 
     {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "栽培",
        "pid": "1708271201504590143",
        "id": ""
    },  
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "育苗",
        "pid": "1708271201504590143",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "马铃薯",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "干果",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "乳制品",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "蛋肉类及制品、乳制品",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "收获机械",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "牲畜",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "茶叶",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "茶",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "果仁、籽",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "禽类",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "种植机械",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "禽蛋",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农用物资",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "天然林",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "苗木",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "药材",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "鲜活水产品",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "坚果",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农药",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "水利水文用仪器",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农林牧渔",
        "pid": "1708271201504590143",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "鱼塘",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "粮食",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "豆制品",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "畜牧机械",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农用工具",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农机",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农用机械",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "肉制品",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "化学肥料",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农产品",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "饲料加工设备",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "生鲜水果",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "水利工程",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "灌溉工程",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "甜味剂",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "肉类",
        "pid": "1708271201504590143",
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
    },{
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "肥料",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "海岸",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "复垦",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "大坝",
        "pid": "1708271201504590143",
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
        "key_words": "造林",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "林场",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "蔬菜",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "山林保护",
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
        "pid_title": "农业水利",
        "key_words": "大棚",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "农业",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "农田",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "羊",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "蓄滞洪区",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "灌溉区",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "新农村",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "水系",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "示范村",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "水治理",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "鱼种",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "农牧业",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "基本农田",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农保地",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "深加工",
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
        "pid_title": "农业水利",
        "key_words": "食用菌",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "物流园",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "有机蔬菜",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "水产养殖",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "竹林",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "竹加工",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "休闲农业",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "观赏农业",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "湿地保护",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "海塘",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "江塘",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "河塘",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "田间工程",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "有机肥",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "水土保护",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农业补偿",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "饮水",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "水文监测",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农业招商",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农业招标",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "绿色食品交易",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "防洪",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "泥石流",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "山体滑坡",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "围堰",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "节水",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "自来水",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "污水处理",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "流域治理",
        "pid": "1708271201504590143",
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
        "pid_title": "农业水利",
        "key_words": "水利整治",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "标准农田",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "示范农业",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "沙漠治理",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "经济作物",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "饮水",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "饮水工程",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "管涌",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "溃坝",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "干旱",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "特色农业",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "农业旅游",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "雨污合流",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "农业水利",
        "key_words": "排污管囊",
        "pid": "1708271201504590143",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "游艺设备",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "风景名胜区",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "风景区",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "名胜区",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "观光区",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "观光带",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "餐饮",
        "pid": "1708271201536210156",
        "id": ""
    },
     {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "主题乐园",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "游艺机",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "娱乐服务",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "体育中心",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "防护林",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "体育中心",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "辅道",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "综合整治",
        "pid": "1708271201536210156",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公共卫生",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "农民社区",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "围堤",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "路段",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "净化美化",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "治安",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "臭水",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公交",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "殡仪馆",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "卫生和计划生育",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "自然保护区",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "风景保护区",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "国土资源规划测绘院",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "水产科学研究院",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "计划建设部",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "计划建设局",
        "pid": "1708271201536210156",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "政府招标",
        "key_words": "国土资源厅",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公益林",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "大桥施工",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "棚户片区改造",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "产业区",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "路改造",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "活动室",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公共信息服务",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "综合治理",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "城乡规划",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "服务设施",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "村路工程",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "网球中心",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "国防教育",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "村落改造",
        "pid": "1708271201536210156",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "救护队",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "禁毒",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "区段治理",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "村庄规划",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "广电中心",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "公租房",
        "pid": "1708271201536210156",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "区域改造",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "电网",
        "pid": "1708271201536210156",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "创业园",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "创新园区",
        "pid": "1708271201536210156",
        "id": ""
    },
     {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "体育场",
        "pid": "1708271201536210156",
        "id": ""
    },
     {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "露营基地",
        "pid": "1708271201536210156",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "市政建设",
        "key_words": "垃圾分类",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "电动观光车",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "缆车",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "旅游山道",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "游乐园",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "游乐设备",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "过山车",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "户外用品",
        "pid": "1708271201536210156",
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
        "pid_title": "旅游开发",
        "key_words": "酒店",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "客栈",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "客房率",
        "pid": "1708271201536210156",
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
        "pid_title": "旅游开发",
        "key_words": "旅游区",
        "pid": "1708271201536210156",
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
        "pid_title": "旅游开发",
        "key_words": "组团旅游",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "自驾游",
        "pid": "1708271201536210156",
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
        "pid_title": "旅游开发",
        "key_words": "景观",
        "pid": "1708271201536210156",
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
        "pid_title": "旅游开发",
        "key_words": "景区开发",
        "pid": "1708271201536210156",
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
        "pid_title": "旅游开发",
        "key_words": "主题公园",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "博物馆",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "景观设计",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "农家乐",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "俱乐部",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "全域旅游",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "旅游线路",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "旅行社",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "极限运动",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "跑马运动",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "徒步运动自行车",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "滑翔",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "自驾营地",
        "pid": "1708271201536210156",
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
        "pid_title": "旅游开发",
        "key_words": "岛屿旅游",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "互动旅游",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "民俗",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "特色餐饮",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "迪斯尼",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "环球乐园",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "电影乐园",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "庙宇",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "环山公路",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "网络订票",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "旅游投诉",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "国际线路",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "旅游交通",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "收费站",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "旅游卡",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "电话亭",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "杂技表演",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "驻演",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "验票闸机",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "救援组织",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "退税机构",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "教堂",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "旅游大巴",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "公务飞机",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "私人飞机",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "旅游开发",
        "key_words": "歌厅",
        "pid": "1708271201536210156",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "金融保险",
        "pid": "1708271201536210153",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "资产评估",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "股权",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "增资",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "投资",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "理财",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "贷款",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "招商",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "PPP",
        "pid": "1708271201536210153",
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
        "key_words": "保险",
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
        "pid_title": "金融投资",
        "key_words": "住房公积金",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "基金",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "银行贷款",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "银行牌照",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "证券",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "一行三会",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "保监会",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "银监会",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "证监委",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "股权投资",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "债权",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "国际融资",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "招商",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "交易所",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "创业投资",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "上市",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "证券公司",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "保险公司",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "投资管理公司",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "牌照",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "信用卡",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "网络结算",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "跨境贸易",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "外汇结算",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "资产管理",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "基金管理",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "股权投资",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "债券投资",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "金融牌照合作",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "租赁",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "银行贷款",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "政策贷款",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "金融投资",
        "key_words": "扶持资金",
        "pid": "1708271201536210153",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "舞台设备",
        "pid": "1708271201536210152",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "红军",
        "pid": "1708271201536210152",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "新四军",
        "pid": "1708271201536210152",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "纪念馆",
        "pid": "1708271201536210152",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "文化礼堂",
        "pid": "1708271201536210152",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "广告",
        "pid": "1708271201536210152",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "新闻",
        "pid": "1708271201536210152",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "传统村落",
        "pid": "1708271201536210152",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "马拉松赛",
        "pid": "1708271201536210152",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "古文化",
        "pid": "1708271201536210152",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "古建筑",
        "pid": "1708271201536210152",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "古城",
        "pid": "1708271201536210152",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "电视转播",
        "pid": "1708271201536210152",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "文化陈列馆",
        "pid": "1708271201536210152",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "汉服",
        "pid": "1708271201536210152",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "影城",
        "pid": "1708271201536210152",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "艺术馆",
        "pid": "1708271201536210152",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "彩绘",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "工艺品",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "美术品",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "影视",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "书画工艺",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "音乐厅",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "广播电台",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "电视台设备",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "图书音像",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "美术馆",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "博物馆",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "民间工艺品",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "雕刻工艺品",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "广告展览器材",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "摄影器材",
        "pid": "1708271201536210152",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "展厅",
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
        "key_words": "会展服务",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "收藏品",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "金属工艺品",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "陶瓷工艺品",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "设计师",
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
        "key_words": "电视剧",
        "pid": "1708271201536210152",
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
        "pid_title": "文化创意",
        "key_words": "装修装饰",
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
        "pid_title": "文化创意",
        "key_words": "报纸",
        "pid": "1708271201536210152",
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
        "pid_title": "文化创意",
        "key_words": "广播电视",
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
        "key_words": "购物节",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "文艺演出",
        "pid": "1708271201536210152",
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
        "pid_title": "文化创意",
        "key_words": "古窑址保护",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
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
        "pid_title": "文化创意",
        "key_words": "活动中心",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "健身",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "文化科技中心",
        "pid": "1708271201536210152",
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
        "pid_title": "文化创意",
        "key_words": "活动场所",
        "pid": "1708271201536210152",
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
        "pid_title": "文化创意",
        "key_words": "健身中心",
        "pid": "1708271201536210152",
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
        "pid_title": "文化创意",
        "key_words": "遗址",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "非物质文化遗产",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "申遗",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "影视版权",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "媒介代理",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "广告资源",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "户外广告",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "游戏设备",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "电子竞技",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "玩具",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "雕刻工艺",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "出版",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "酒窖",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "雕刻",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "拍卖",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "文化创意",
        "key_words": "游戏",
        "pid": "1708271201536210152",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "食品机械",
        "pid": "1708271201504590144",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "装备制造",
        "pid": "1708271201504590144",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "腹腔镜系统",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "血滤机",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "车脱轨系统",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "喷涂系统",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "直线加速器",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "二极管",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "插头",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "LED",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "一汽大众",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "超声波诊断仪",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "王老吉",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "雨水箱",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "测功仪",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "零配件",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "机台设备",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "加工中心",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "络筒机",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "深硅刻蚀机",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "光刻机",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "屏蔽设备",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "加工机",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "脱硫装置",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "曲轴线",
        "pid": "1708271201504590144",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "离心机",
        "pid": "1708271201504590144",
        "id": ""
    },   {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "细胞仪",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "功能仪",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "检测装置",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "延膜机",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "成型机",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "曝光机",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "发射机",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "探针",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "测试机",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "骨密度仪",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "投影仪",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "专用设备",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "发卡机",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "分离机",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "服饰",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "纺织",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "弱电监控",
        "pid": "1708271201504590144",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "产品加工",
        "pid": "1708271201504590144",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "教育装备",
        "pid": "1708271201504590144",
        "id": ""
    },  {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "客车",
        "pid": "1708271201504590144",
        "id": ""
    },   {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "光伏",
        "pid": "1708271201504590144",
        "id": ""
    },   {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "监护仪",
        "pid": "1708271201504590144",
        "id": ""
    }, 
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "检测系统",
        "pid": "1708271201504590144",
        "id": ""
    },
   {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "工业加工",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电池",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "仪表配件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "分析仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "醛类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "衡器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "实验室用品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "冶金专用设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "地质地震仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "办公用纸",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "聚合物",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "压缩分离设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电化学仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "天然纺织原料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "气体检测仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "刀具夹具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "床上用品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "复合包装制品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "气动单元组合仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "包装专用设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "磨抛光电动工具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "粉碎设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "印刷耗材",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "酒类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "起重运输设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电子材料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "醇类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "无机盐",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "纺织皮革机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "诊断图象处理软件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "休闲食品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "传动系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "绝缘材料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "车床",
        "pid": "1708271201504590144",
        "id": ""
    }, {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "变送器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "出版印刷",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "路面设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "包装绳",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "鞋",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "专科用制剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "润滑油",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "调味品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "黄油枪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "烯烃",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "劳保用品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "成像系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "塑料加工专用设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "音响",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "体育用品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "计量、标准器具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "无机碱",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "印花布",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "绘图计算测量仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "起重装卸设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "智慧教室",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "软饮料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "食品加工",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "雷达",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "烟",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "酒",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "生化",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "催化剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "凿岩机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "设备采购",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "非织造设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "胶辊",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电工仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "石油专用分析仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "化工",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "日用化学品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "印刷加工服务",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "编辑制作设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "印后设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "自动化成套控制系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "水分测定仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "健身器材",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "制药生产设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "桌面用品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "反渗透设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "土地耕整机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "原水处理设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电子测量仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电容器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "印刷用纸",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "石油钻采专用设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "高纯水制取设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "胶粘剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "乐器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "机械零部件加工",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "中药制药设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "竹木包装制品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "办公本册",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "橡胶制品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "摄像器材",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "手动轮椅车",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "纱线丝",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "液压工具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "车辆",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "柴油车",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "厨卫家电",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "矿石分选设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "涂装设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "发电机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "烷烃",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "光学仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "无机化工原料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "造纸设备及配件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "分析仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "传动件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "监控设备器材",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "血液分析系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其他通用分析仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "半导体分立器件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "防护保养品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "炉用燃烧器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "非织造及工业用布",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "教学模型",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "插头插座",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "发电机组",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "氧化物",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "整流器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "生物工程设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "集成电路",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电动机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "染整设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电动车",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "专用仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "光谱仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "过滤设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "礼品饰品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其他印刷机械专用配件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "芳香烃",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "服装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "纺织面料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "挖掘机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "制剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "刷",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其它仪器仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电工电器成套设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "自动化设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "胺类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "办公笔类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "生物制品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "家纺",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "农林牧渔专用机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "频率元件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "天然橡胶",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "工业机器人",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "皮革助剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其他玩具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "金属加工机床",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "纺织加工",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "印刷机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "化纤处理机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "产品印刷加工",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "筛分设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "包装配套制品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "包装用纸",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "风机排风设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "加工设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "继电器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "餐厨用具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "防护帽",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "礼品包装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "橡胶助剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "毯子",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "磁性材料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "高压电器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "人造革",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "塑胶片",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "生命科学仪器及设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "计算机周边",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "计算机及配件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "冰箱",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "塑料包装制品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "压力仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "紧固件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "胶带",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "化学试剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "羧酸",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "生化分析系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "办公文具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电声器件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "沥青",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "实验室仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "焊接材料与附件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "色织",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "小家电",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "米面油及调味品类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "金属包装制品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其他自动化类仪表装置",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "防护服",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "化学助剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其它家用电器类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "防盗报警器材",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "传质设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其他电子产品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "配电输电设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "塑胶制品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "非金属加工机床",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "开关",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "汽摩及配件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "车用仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "印刷设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "光学测量仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "橡胶棒",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电源及电池",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电子显微镜",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "专项化学品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "纺机设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "汽摩产品制造设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "光电与显示器件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "日用百货",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "箱、包、皮具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "生理研究实验仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "三轮车",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "传感器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "清洗剂",
        "pid": "1708271201504590144",
        "id": ""
    },{
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "清洗机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电动汽车",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "米面",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "测绘仪器及器材",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "财务用品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其他电动车",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "防护眼镜",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "量仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "办公用品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "减速机变速机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "有色金属加工材",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "腈类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "终端设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "混合设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "酚类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "生物反馈仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电风扇",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其他电子材料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "前端设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其它运动休闲类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "金属成型机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "轮胎",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "保温隔热材料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "采矿采石设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "流量仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "包装材料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "掘进机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "袜",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电子",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "布料包装制品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "固化剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "化学纤维",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "工业自动化仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "扎染",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "调节器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "化工设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "自行车",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "羧酸衍生物",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "液压气动元件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电感器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "塑料包装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "制剂辅料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "变压器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "节电设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "针织设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "周转箱",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "水质分析仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其它金属加工机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "乘用车",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "防护手套",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其他化学原料药",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "轮式拖拉机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "无机酸",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "添加剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "提升设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "原料药机械设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "塑料助剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "发动系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "植物提取物",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "波谱仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "元素分析仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "飞机及配件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "内燃机及配件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "广告促销礼品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "通用塑胶",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "节庆用品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "支护机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "工业安全仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "合成橡胶",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "金属制品加工设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "办公家具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "美容化妆",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "锅炉",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "原动机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "煤炭行业专用仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "橡胶加工专用设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "检测仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "办公耗材",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "玩具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "工程建筑专用机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "机床及其附件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "地质勘查设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "机械量仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "船用发动机配件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "脑电诊断仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "质谱仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "包装制品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "橡胶管",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "核辐射测量仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "泵",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "注油枪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "钟表计时仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "方便食品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "物位仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电视机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "空调设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "压力机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "导航气象天文海洋仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "传热设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "机械设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "机电",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "面具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "机床",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "试验机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "温度仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "吸附剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "色谱仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "信号发生器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "转向系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "放射性核素诊断设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "印刷",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "光谱诊断设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "无创监护仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "食品饮料烟草加工设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "装饰用纺织品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "工程塑胶",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "集中控制装置",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电子电工制造设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "金属加工机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "家用电器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "量具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "纺织配套器材",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "油墨",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "饮片机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "生物识别设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "制冷",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "IT",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "织机设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "服装机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "软化水设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "物性测试仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "食品包装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "纸包装制品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其它服装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其它非机动车",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "干燥设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "显示仪表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "脱硫除尘设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "娱乐视听设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "锅炉及辅助设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "铲运机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "洗衣机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "有机化工原料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "农副食品加工设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "维修设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "齿轮",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "热水器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "酯类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "工控系统及装置",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "造纸用助剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "保险元器件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其它家居类",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "光电子、激光仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "塑料模具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电阻器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "非机动车",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "色标、色卡",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "空调",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "办公设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "轴承",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "船舶",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "家具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "密封件、连接件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "数码产品",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "制剂机械",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "其他包装材料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "有色金属合金",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "合成树脂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "防护鞋",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "汽轮机及辅机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "模具",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "分子生物",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "运动服装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "烟草加工设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "摩托车",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "机床附件",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "针织面料",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "制服订制",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "液压",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "制钠",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "液钠罐",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "液晶",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "液晶屏",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "自动化系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "扫描仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "生产线",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电磁阀",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "辊筒",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "焦化",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "混凝剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "应急灯",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "自控系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "红外热像仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "激光切割机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "激光",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "切割机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "核酸",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "提取系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "色谱系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "集控中心",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "压力表",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "速凝剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "货梯",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电梯",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "扶梯",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "升降机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "插座",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "芯片",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "精密仪器",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "显微镜",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "镀膜系统",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "发动机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "液氧药剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "汽车制造",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "飞机制造",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "除锈机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "治疗仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "活性炭",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "净水设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "甲醇",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "监测监控设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "监测设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "监控设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "检验试剂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "玻璃钢水",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "职场装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "职业装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "制服",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "制胶厂",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "绿色食品产业园",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "真空镀膜机",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "纹饰仪",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "铝合金",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "童装",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "生产调度",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "数控",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "显示屏",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "工业4.0",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "汽车摩托",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "人工智能",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "电脑",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "网络布网",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "家居生活",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "生物科技",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "造船",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "机器人",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "深加工",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "航空",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "航天",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "火箭",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "运载火箭",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "军工设备",
        "pid": "1708271201504590144",
        "id": ""
    },
    {
        "id_title": "",
        "pid_title": "先进制造",
        "key_words": "武器",
        "pid": "1708271201504590144",
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
             print  title ,"||关键词|",jsob['key_words'],"||分类|",jsob['pid_title']

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


# 获取商机的金额
unit_dict = {
    '万': '0000',
    '十万': '00000',
    '百万': '000000',
    '千万': '0000000',
    '亿': '00000000',
    '十亿': '000000000',
    '百亿': '0000000000',
    '千亿': '00000000000'
}

def get_money(content):
    if not content:
        return content
    html = HTMLParser.HTMLParser()
    content_html = html.unescape(content)
    content_html = html.unescape(content_html)
    unit_list = ['', '万', '十万', '百万', '千万', '亿', '十亿', '百亿', '千亿']
    regex_list = ['工程规模.*?(\d+){unit}元', '投资.*?(\d+){unit}元', '预算.*?(\d+){unit}元', '采购.*?(\d+){unit}元',
                  '项目.*?(\d+){unit}元', '总额.*?(\d+){unit}元', '金额.*?(\d+){unit}元', '概算.*?(\d+){unit}元']
    s = re.sub('<[^>]*>', '', content_html)
    is_match = False
    limit = 0
    for regex in regex_list:
        if is_match:
            break
        for unit in unit_list:
            reg = regex.format(unit=unit)
            res = re.findall(reg.decode(), s)
            if res:
                if not unit and int(res[0]) < 1000 or int(res[0]) == 0:
                    continue
                if unit:
                    limit = res[0] + unit_dict.get(unit)
                else:
                    limit = res[0]
                is_match = True
                break
    return limit




