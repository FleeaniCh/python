"""
    粘包(慢)
    解决粘包：
        1.控制收发速度
        2.人为添加边界(如加“#“)
"""
from socket import *
from time import sleep

sockfd = socket()
sockfd.bind(('192.168.0.199', 8888))
sockfd.listen(5)
connfd,addr=sockfd.accept()

while True:
    sleep(1)
    data = connfd.recv(1024)
    print(data.decode())
