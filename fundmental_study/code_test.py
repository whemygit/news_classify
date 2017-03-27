#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass



def unicode_test(value):
    import unicoedata
    name=unicodedata.name(value)
    value2=unicoedata.lookup(name)
    print 'value="%s",name="%s",value2="%s"' %(value,name,value2)
print unicode_test('ÏêÏ')