"""
    pipe.py     管道通信
    注意：
        1. multiprocessing 中管道通信只能用于有亲缘关系的进程中
        2. 管道对象在父进程中创建，子进程通过父进程获取
"""
from multiprocessing import Process, Pipe
from time import sleep

# 创建管道(默认双向)
fd1,fd2 = Pipe()
# 单向管道：fd1 --> recv,    fd2 --> send
# fd1, fd2 = Pipe(duplex=False)


def app1():
    print("启动app1，请登录")
    print("请求app2授权")
    fd1.send("app1 请求登录")  # 写入管道
    data = fd1.recv()
    if data:
        print("登录成功", data)


def app2():
    sleep(0.2)
    data = fd2.recv()  # 阻塞等待读取管道内容
    print(data)
    fd2.send(('Dave', '123'))  # 可以发送任意Python数据类型


if __name__ == '__main__':
    p1 = Process(target=app1)
    p1.start()
    p2 = Process(target=app2)
    p2.start()
    p1.join()
    p2.join()
