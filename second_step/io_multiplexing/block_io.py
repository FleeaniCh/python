"""
block_io.py
socket  套接字非阻塞示例
"""

from socket import *
from time import ctime,sleep

# 日志文件
f = open('log.txt','a+',encoding='utf-8')

# tcp套接字
sockfd = socket()
sockfd.bind(('192.168.0.199',8888))
sockfd.listen(5)

# 设置套接字为非阻塞
# sockfd.setblocking(False)

# 设置超时检测
sockfd.settimeout(3)

while True:
    print("Wating for the connect...")
    # 没有客户端连接时每隔3秒写一条日志
    try:
        connfd,addr = sockfd.accept()
    except (BlockingIOError,timeout) as e:  # 同时捕获多个异常
        sleep(3)
        f.write("%s: %s\n"%(ctime(),e))
        f.flush()
    else:
        print("Connect from ",addr)
        data = connfd.recv(1024).decode()
        print(data)