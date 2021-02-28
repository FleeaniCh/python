"""
    udp_recv.py   udp套接字服务端流程
    重点代码
"""

from socket import *

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ('192.168.0.199', 8880)
sockfd.bind(server_addr)

# 循环收发消息
while True:
    data, addr = sockfd.recvfrom(5)
    # OSError: [WinError 10040] 一个在数据报套接字上发送的消息大于内部消息缓冲区
    # 或其他一些网络限制，或该用户用于接收数据报的缓冲区比数据报小。
    print("Receive massage from ：", addr, data.decode())
    sockfd.sendto(b'Thanks', addr)

# 关闭套接字
sockfd.close()
