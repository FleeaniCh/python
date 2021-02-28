"""
    UDP套接字广播发送方
    1.创建UDP套接字
    2.设置可以发送广播
    3.循环想广播地址发送
"""

# 广播地址
from socket import *
from time import sleep

dest = ('192.168.0.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

# 设置可以发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
data = """
    生活需要眼前的苟且，
    也需要诗一般的远方
"""

while True:
    sleep(2)
    s.sendto(data.encode(),dest)    #目标地址就是广播地址

