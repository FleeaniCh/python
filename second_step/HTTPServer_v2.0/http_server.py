"""
httpserver  v2.0
env: python3.7
IO多路服用 和 http训练
"""
from socket import *
from select import *


# 具体功能实现
class HTTPServer:
    def __init__(self, host='0.0.0.0', port=8000, dir='./static'):
        self.host = host
        self.port = port
        self.dir = dir
        # 多路复用列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.address = (host, port)
        # 实例化时直接创建套接字
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)

    # 启动服务函数
    def server_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d" % self.port)
        self.rlist.append(self.sockfd)
        # 循环监控IO
        while True:
            rs, ws, xs = select(self.rlist,
                                self.wlist,
                                self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("Connect from ", addr)
                    self.rlist.append(c)
                else:
                    # 处理请求
                    self.handle(r)
                    """
                    data = r.recv(4096).decode()
                    if not data:
                        self.rlist.remove(r)
                        r.close()
                        continue
                    if data.split()[1] == '/csdn':
                        response = self.get_resource(filepath='./static/csdn.html')
                    elif data.split()[1] == '/TestHome':
                        with open('./static/TestHome.html',encoding="utf-8") as f:
                            response = self.request_format()
                            response += f.read()
                    else:
                        response = self.request_format()
                        response += "<h>404, Sorry......</h1>"
                    r.send(response.encode())

            for w in ws:
                pass

            for x in xs:
                pass

    def get_resource(self,filepath):
        with open(filepath, encoding="utf-8") as f:
            response = self.request_format()
            response += f.read()
        return response

    def request_format(self):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        return response
                """

    def handle(self,connfd):
        # 接收HTTP请求
        request = connfd.recv(4096)
        # 客户端断开
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 提取请求内容(将字节串按行切割)
        request_lines = request.splitlines()[0]
        info = request_lines.decode().split(' ')[1]

        # 根据请求内容进行数据整理
        # 分为两类：1. 请求网页  2. 其他
        if info == '/' or info[-5:]=='.html':
            self.get_html(connfd,info)
        else:
            self.get_data(connfd,info)

    # 返回网页
    def get_html(self,connfd,info):
        # 请求主页
        if info == '/':
            # 请求主页
            filename = self.dir+"/index.html"
        else:
            filename = self.dir+info
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry......</h1>"
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += fd.read()
        finally:
            # 将响应发送给浏览器
            connfd.send(response.encode())

    # 其他数据
    def get_data(self,connfd,info):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Waiting for httpserver3.0</h1>"
        connfd.send(response.encode())


# 用户使用
if __name__ == '__main__':
    """
    通过HTTPServer类快速搭建服务，展示自己的网页
   """
    # 用户决定的参数
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = './static'  # 网页存储位置

    httpd = HTTPServer(HOST, PORT, DIR)  # 实例化对象
    httpd.server_forever()  # 启动服务
