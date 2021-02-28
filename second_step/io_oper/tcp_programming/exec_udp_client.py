"""
    使用udp客户端查询单词，得到单词的解释，如果没有该单词，则得到
    “没有单词”，客户端可以循环输入单词，直到输入空退出。
"""
from socket import *

ADDR = ('192.168.0.199',8887)

sockfd = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Please input the word: ")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print(msg.decode())

sockfd.close()