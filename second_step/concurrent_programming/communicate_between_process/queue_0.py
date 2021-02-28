"""
queue_0.py    队列实现进程间通信
注意：
    1. 消息队列符合先进先出原则
"""
from multiprocessing import Process,Queue
from time import sleep
from random import randint

# 创建消息队列
q = Queue(5)    # 最大长度为5(多个进程同时存在读写行为，所以不会有影响)

def handle():
    for i in range(6):
        x = randint(1,33)
        q.put(x)    # 消息入队
    q.put(randint(1,16))

def request():
    # while True:
    #     print("摇啊摇...")
    #     sleep(0)
    #     try:
    #         print(q.get(3)) # 消息出队
    #     except:
    #         break
    l = []
    for i in range(6):
        l.append(q.get())
    l.sort()
    l.append(q.get())
    print(l)

p1 = Process(target=handle)
p2 = Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()

