"""
    httpserver v1.0
    基本要求：   1. 获取来自浏览器的请求
                        2. 判断如果请求内容是    /，将index.html返回个客户端
                        3. 如果请求的是其他内容，则返回404
"""

from socket import *


# 客户端(浏览器)处理
def request(connfd):
    # 获取请求，将请求内容提取出来
    data = connfd.recv(4069)  # 接收请求
    # 防止浏览器异常退出
    if not data:
        return
    path = data.decode().split()[1]
    # print(path)
    # 判断是/，则返回index.html，不是则返回404
    if path == "/":
        with open('index.html') as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h>404, Sorry......</h1>"
    # 发送给浏览器
    connfd.send(response.encode())


# 创建tcp套接字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重用
sockfd.bind(('192.168.0.199', 8000))
sockfd.listen(3)

while True:
    connfd, addr = sockfd.accept()
    request(connfd)  # 处理客户端请求
