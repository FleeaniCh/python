"""
    基于process的多进程并发
"""
from socket import *
import signal, os
from multiprocessing import Process

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


def handle(c):
    while True:
        data = c.recv(4096)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)

s.listen(5)
print("Listen the port 8888...")

while True:
    try:
        c, addr = s.accept()
        print("Connect from ", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    p = Process(target=handle, args=(c,))
    p.daemon = True # 父进程结束则所有服务终止
    p.start()