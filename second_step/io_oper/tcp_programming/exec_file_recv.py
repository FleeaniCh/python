"""
    服务端：接收文件
"""
from socket import socket

sockfd = socket()

sockfd.bind(('192.168.0.199', 8888))
sockfd.listen(5)
print("Waiting for connect...")
connfd, addr = sockfd.accept()
print("Connect from ", addr)

fw = open('img.png', 'wb')
while True:
    data = connfd.recv(1024)
    if not data:
        break
    fw.write(data)

connfd.close()
sockfd.close()
fw.close()