"""
    IO与字节串
     所有字符串都可以转化成字节串，但是并不是所有的字节串都能转换成字符串(如音频、图片等)
"""
s = 'hello'  # 字符串
print(s)

s = b"hello"  # 字节串
print(s)

s = "你好".encode()  # 将字符串转换为字节串
print(s)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'

# 字节串   转化为 字符串
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode())
