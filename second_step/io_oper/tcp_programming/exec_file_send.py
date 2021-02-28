"""
    将一个文件从客户端发送端服务端保存
    文件可能是文本类型也可能是二进制文件
"""
from socket import socket

sockfd = socket()
server_addr = ('192.168.0.199', 8888)
sockfd.connect(server_addr)

fr = open('image.jpeg', 'rb')
while True:
    data = fr.read(1024)
    if not data:
        break
    sockfd.send(data)   # 已经是字节串

sockfd.close()
fr.close()
