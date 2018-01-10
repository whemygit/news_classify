#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
# with open('index_rec_classify_corpus','r') as fr,open('classify_machine_1','wb') as fw1,open('classify_machine_0','wb') as fw2:
#     lines=fr.readlines()
#     first_line=True
#     for line in lines:
#         if first_line:
#             fw1.write(line)
#             fw2.write(line)
#             first_line=False
#         else:
#             line_list=line.split('\x01')
#             print line_list[-1].strip(),len(line_list[-1].strip())
#
#             new_line_list=line_list
#             if len(line_list[-1].strip()) > 40 or '会议' in line_list[-1] or '开幕' in line_list[-1] or '停电' in line_list[-1] or '召开' in line_list[-1] or '启动' in line_list[-1] or '发布' in line_list[-1] or '调研' in line_list[-1] or '预警' in line_list[-1] or '成立' in line_list[-1] or '举行' in line_list[-1] or '访问' in line_list[-1] or '会见' in line_list[-1]:
#                 new_line_list[5] = '1'
#                 str = '\x01'.join(new_line_list)
#                 fw1.write(str)
#             elif len(line_list[-1].strip()) <= 40 or '元' in line_list[-1] or '「' in line_list[-1]:
#                 new_line_list[5] = '0'
#                 str = '\x01'.join(new_line_list)
#                 fw2.write(str)

with open('classify_machine_1_3','r') as fr,open('classify_machine_1_4','wb') as fw1,open('classify_machine_0_4','wb') as fw2:
    lines=fr.readlines()
    first_line=True
    for line in lines:
        if first_line:
            fw1.write(line)
            fw2.write(line)
            first_line=False
        else:
            line_list=line.split('\x01')
            print line_list[-1].strip(),len(line_list[-1].strip())

            new_line_list=line_list
            if new_line_list[5] == '0':
                new_line_list[5] = '0'
                str = '\x01'.join(new_line_list)
                fw2.write(str)
            else:
                new_line_list[5] = '1'
                str = '\x01'.join(new_line_list)
                fw1.write(str)


            # new_line_list[5]='0'
            # if float(line_list[0])>=0.5:
            #     new_line_list[5]='1'
            #
            # if line_list[1]=='0' or new_line_list[5]=='1':
            #     new_line_list[5]='1'
            #
            # if line_list[2]=='1' or new_line_list[5]=='1':
            #     new_line_list[5]='1'
            #
            # if line_list[3]=='1' or new_line_list[5]=='1':
            #     new_line_list[5]='1'
            #
            # if line_list[4]=='1' or new_line_list[5]=='1':
            #     new_line_list[5]='1'
            #
            # str='\x01'.join(new_line_list)
            # fw.write(str)

if __name__ == '__main__':
    pass