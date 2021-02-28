"""
event   线程互斥方法演示
"""
from threading import Thread,Event

s = None    # 用于通信
e = Event() # 事件对象

def Yangzir():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set() # 操作完共享资源   e   设置

t = Thread(target=Yangzir)
t.start()   # 运行子线程

# 运行主线程
print("说对口令就是自己人")
e.wait()
if s == '天王盖地虎':
    print('宝塔镇河妖')
    print("确认过眼神，你是对的人")
else:
    print("打死他")

t.join()
