"""
chat room   客户端
发送请求，展示结果
"""
from socket import *
import os, sys

# 服务器地址
ADDR = ('192.168.0.199', 8888)


# 发送消息
def send_msg(s, name):
    while True:
        try:
            text = input("发言：")
        except KeyboardInterrupt:
            text = 'quit'
        if text.strip() == 'quit':
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = 'C %s %s' % (name, text)
        s.sendto(msg.encode(), ADDR)


# 接收消息
def recv_msg(s):
    while True:
        try:
            data, addr = s.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        # 从服务器收到EXIT进程退出
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode() + '\n发言:', end=' ')


# 客户端启动函数
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    # 进入聊天室
    while True:
        name = input("请输入姓名：")
        msg = 'L ' + name
        s.sendto(msg.encode(), ADDR)
        # 接收反馈
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":  # 协议规定
            print("您已进入聊天室")
            break
        else:
            print(data.decode())

    # 已经进入聊天室
    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:  # 子进程发送消息
        send_msg(s, name)
    else:  # 父进程接收消息
        recv_msg(s)


main()
