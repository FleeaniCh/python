"""
IO并发模型——select
    select tcp  服务
    重点代码

    思路分析：
    1. 将关注的IO放入到监控列表
    2. 当IO就绪时会通过select返回（注意：IO就绪状态）
    3. 遍历返回值列表，得知哪个IO就绪进行处理

    注：select最多监控1024个IO
"""
from select import select
from socket import *

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 设置关注列表
rlist = [s]  # s用于等待处理连接
wlist = []
xlist = []

# 循环监控IO
while True:
    rs, ws, xs = select(rlist, wlist, xlist)    # 多个IO同时就绪，需要等待

    # 遍历返回值列表，处理就绪的IO
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("Connect from ", addr)
            rlist.append(c)  # 增加新的IO关注
        else:
            # 有客户端发消息
            data = r.recv(1024).decode()
            if not data:    # 客户端退出
                rlist.remove(r) # 取消对客户端关注
                r.close()
                continue
            print(data)
            # r.send(b'OK')
            wlist.append(r) #给我发消息的客户端

    for w in ws:
        w.send(b'OK')
        wlist.remove(w) # 发完消息移除

    for x in xs:
        pass
