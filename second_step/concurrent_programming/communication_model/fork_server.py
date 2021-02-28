"""
    fork_server.py      基于fork的多进程并发
    重点代码
"""
from socket import *
import os
import signal

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


# 具体处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("Listen the port 8888...")

while True:
    try:
        c, addr = s.accept()  # 父进程阻塞等待客户端连接
        print("Connect from ", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端事物
    pid = os.fork()
    if pid == 0:
        s.close()
        handle(c)  # 处理具体事物
        os._exit(0)  # 子进程销毁
    else:
        c.close()  # 父进程不需要和客户端通信
