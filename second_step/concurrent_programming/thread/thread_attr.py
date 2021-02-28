"""
thread_attr.py   线程属性演示
"""
from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun,name='tarena')
# t.setDaemon(True)   # 主线程退出，分支线程也退出
t.setName('Tedu')
print(t.getName())

t.start()   # 启动子线程

print("is_alive:",t.is_alive()) # True
print("daemon:",t.isDaemon())   #True