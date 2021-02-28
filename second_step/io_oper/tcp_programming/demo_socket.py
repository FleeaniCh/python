"""
    socket服务端程序
"""
import socket

# 1. 创建套接字
sockfd = socket.socket(socket_family='AF_INET', socket_type='SOCK_STREAM', proto=0)
# socket_family：网络地址类型
# socket_type：套接字类型（流式/数据报）

# 2. 绑定(ip:port)
sockfd.bind(())

# 3. 设置监听
sockfd.listen()

# 4. 等待处理客户端连接请求
connfd,addr = sockfd.accept()
# connfd：客户端连接套接字
# addr：连接的客户端地址

# 5. 消息收发
data = connfd.recv(buffersize=1024) # 接收消息

n = connfd.send(data)   # 发送消息(bytes格式--字节串)，返回发送的字节数

# 6. 关闭套接字
sockfd.close()

