"""
    服务端
"""
from socket import *
import struct

# 和客户端一致
st = struct.Struct('i5sif')

sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.bind(('192.168.0.199', 8888))

while True:
    with open('data.txt', 'a+') as f:
        data, addr = sockfd.recvfrom(4096)
        if not data:
            break
        data = st.unpack(data)  # 解包
        data = "%d  %-5s  %d  %.1f" % (data)  # 格式化
        # print(data)
        f.write(str(data) + '\n')
        f.flush()
