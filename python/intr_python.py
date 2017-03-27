#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

#字符串
type("abc")
type(99.9)
int(True)
int(False)
"snap"

print "a\tbc"
print "a\nb\nc"

letters="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
letters[0]
letters[1]
name="henny"
name.replace("h","o")

letters[:]
letters[1:]
letters[1:2]
letters[:-(5+1):-1]
letters[:-(5+1):1]

letters.split(",")
todos="get gloves,get mask,get cat vitamins,call ambulance"
todos.split(",")
todos.split()
todo_list=todos.split(",")
todo_list
bodo_list_join=",".join(todo_list)
bodo_list_join


#list and tuple
empty_list=[]
empty_list.append("aadv")
empty_list
list("cat")






