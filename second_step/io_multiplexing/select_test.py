"""
    select  函数示例
        理解准备就绪的概念
"""
from select import select
from socket import *

s = socket()
s.bind(('192.168.0.199', 8888))
s.listen(3)

f = open('log.txt', 'r+')

print("监控IO")
rs, ws, xs = select([s], [f], [])
print("rlist: ", rs)
print("wlist: ", ws)
print("xlist: ", xs)
