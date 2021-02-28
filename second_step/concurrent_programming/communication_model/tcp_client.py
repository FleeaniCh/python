"""
    粘包(快)
"""

from socket import *

# 创建tcp套接字
sockfd = socket()    # 默认创建流式套接字

# 连接服务器
server_addr = ('192.168.0.199',8888)
sockfd.connect(server_addr)

while True:
    # 发送消息
    data = input("Msg>>")
    if not data:
        break
    sockfd.send(data.encode())  # 传输必须是字节串
    data = sockfd.recv(1024)
    print("Sever: ",data.decode())   # 打印接收到内容

# 关闭套接字
sockfd.close()