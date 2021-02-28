"""
    文件偏移量
"""
f = open('test.py','w+')
f.write('hello world')  # 文件偏移量移到末尾(为空)
f.flush()

data = f.read() #接着(同一)文件偏移量位置读(写)
print(data)
f.close()