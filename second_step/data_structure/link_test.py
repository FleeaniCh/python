"""
    比较链表与列表的遍历效率
"""
from linklist import *
import time

l = range(99999)
link = LinkList()
link.init_list(l)
s_time = time.time()
# for i in l:
#     print(i)
link.show()

print("time: ", time.time() - s_time)
