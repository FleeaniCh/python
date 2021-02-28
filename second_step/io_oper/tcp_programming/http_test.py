"""
    http 请求响应测试
"""
from socket import *

# http使用tcp传输
s = socket()
s.bind(('192.168.0.199',8000))
s.listen(3)
c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096)
print(data)

# 将数据组织为响应格式
response = """
    HTTP/1.1 200 OK
    Content-Type:text/html
    
    <h1>Hello World</h1>
"""
c.send(response.encode())


c.close()
s.close()