#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
with open('local_rec_classify_corpus','r') as fr,open('local_recommend_classify_machine','wb') as fw:
    lines=fr.readlines()
    first_line=True
    for line in lines:
        if first_line:
            fw.write(line)
            first_line=False
        else:
            line_list=line.split('\x01')
            print line_list[0]
            new_line_list=line_list
            new_line_list[5]='0'
            if float(line_list[0])>=0.5:
                new_line_list[5]='1'

            if line_list[1]=='0' or new_line_list[5]=='1':
                new_line_list[5]='1'

            if line_list[2]=='1' or new_line_list[5]=='1':
                new_line_list[5]='1'

            if line_list[3]=='1' or new_line_list[5]=='1':
                new_line_list[5]='1'

            if line_list[4]=='1' or new_line_list[5]=='1':
                new_line_list[5]='1'

            str='\x01'.join(new_line_list)
            fw.write(str)

if __name__ == '__main__':
    pass