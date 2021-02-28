"""
    udp客户端
"""
from socket import *
import struct

#  数据格式定义
st = struct.Struct('i5sif')

# udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
ADDR = ("192.168.0.199", 8888)

while True:
    print("=====================")
    id = int(input("Please input id: "))
    name = input("Please input name: ")
    age = int(input("Please input age: "))
    score = float(input("Please input score: "))
    data = st.pack(id, name.encode(), age, score)  # 数据打包
    sockfd.sendto(data, ADDR)
