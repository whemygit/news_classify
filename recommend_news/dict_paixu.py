#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import heapq
from operator import itemgetter
import operator

reload(sys)
sys.setdefaultencoding("utf-8")
def generate_dict_test():
    for i in [1,2,3]:
        yield {
            'item_id': i,
            'average': i,
            'rating_num': i,
            'category_id': i
        }

def top(n,dict_sort):
    print heapq.nlargest(n, dict_sort, key=itemgetter(3))

qw=[{'item_id': 5, 'rating_num': 3, 'average': 1, 'category_id': 1},{'item_id': 1, 'rating_num': 1, 'average': 1, 'category_id': 1},{'item_id': 1, 'rating_num': 7, 'average': 1, 'category_id': 1}]
print heapq.nlargest(1,qw,key=itemgetter('rating_num'))


www={'item_id': 5, 'rating_num': 3, 'average': 1, 'category_id': 1}
sortedwww=sorted(www.iteritems(),key=operator.itemgetter(1),reverse=False)
print sortedwww
for i in sortedwww:
    print i,type(i),i[0],i[1]

if __name__ == '__main__':
    ss=generate_dict_test()
    # for i in ss:
    #     print i
    #     top(1,i)