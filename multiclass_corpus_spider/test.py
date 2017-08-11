#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

category_dict={"cj":"caijing",
    "cul":"wenhua",
    "yl":"yule",
    "life":"shenghuo",
    "gn":"shizheng",
    "auto":"qiche",
    "ty":"tiyu",
    "sh":"shehui"}

def main():
    for item in category_dict:
        main_url='''http://channel.chinanews.com/cns/s/channel:%s.shtml?pager=%s&pagenum=20&_='''%(item,1)
        print main_url
        # for url, title in get_news_urllist(main_url):
        #     content=get_news_detail(url)
        #     news_info = dict()
        #     news_info['url']=url
        #     news_info['title'] = title
        #     news_info['content'] = content
        #     news_info=json.dumps(news_info)
        #     fw.write(news_info+'\n')
        #     print url, title

if __name__ == '__main__':
    main()
