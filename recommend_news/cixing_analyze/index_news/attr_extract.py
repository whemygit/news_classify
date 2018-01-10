#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb
from snownlp import SnowNLP

reload(sys)
sys.setdefaultencoding("utf-8")

mysql = {
    "host": "117.78.60.108",
    "port": "3306",
    "database": "cityparlor",
    "password": "123456",
    "user": "es",
    "charset": "utf8"
}

db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                       user=mysql.get('user'),
                       password=mysql.get('password'), charset=mysql.get('charset'))


# query_sql='''SELECT title,source,content FROM t_top_news WHERE create_date LIKE '%%{date}%%' AND language_version='ZH' AND type_id ='1708161038001960000';'''.format(date='2017-12-27')
query_sql='''select a.title,b.content from
(select title ,obj_id from cityparlor.t_index_setting where language_version='ZH') a
join (select id ,content from cityparlor.t_top_news ) b on a.obj_id = b.id limit 10000;'''
res_sql=db.query(query_sql)


with open('test_index_news','w') as fw:
    for i in res_sql:
        try:
            title=i.get('title')
            content=i.get('content')
            title_s=SnowNLP(title)
            content_s=SnowNLP(content)
            t_tag= title_s.tags
            title_write=title.decode()
            print title_write
            n_len=0
            v_len=0
            title_list = []
            title_tag_list = []
            for i in t_tag:
                title_list.append(i[0]),title_tag_list.append(i[1])
                if str(i[1]).startswith('n'):
                    n_len+=1
                if str(i[1]).startswith('v'):
                    v_len+=1
            n_percent=n_len/float(len(title_tag_list))
            v_percent=v_len/float(len(title_tag_list))
            key_words=content_s.keywords(limit=10)

            k_n_len=0
            k_v_len=0
            keywords_tag_list = []
            for i in key_words:
                # print i,SnowNLP(i).tags[0][0],SnowNLP(i).tags[0][1]
                keywords_tag_list.append(SnowNLP(i).tags[0][1])
                if str(SnowNLP(i).tags[0][1]).startswith('n'):
                    k_n_len+=1
                if str(SnowNLP(i).tags[0][1]).startswith('v'):
                    k_v_len+=1
            k_n_percent=k_n_len/float(len(keywords_tag_list))
            k_v_percent=k_v_len/float(len(keywords_tag_list))
            fw.write(title_write+'\x01'+'source'+'\x01'+",".join(title_list)+'\x01'+','.join(title_tag_list)+'\x01'+str(n_percent)+'\x01'+str(v_percent)+'\x01'+",".join(key_words)+'\x01'+",".join(keywords_tag_list)+'\x01'+str(k_n_percent)+'\x01'+str(k_v_percent)+'\n')
        except:
            print "error:",title.decode()



if __name__ == '__main__':
    pass