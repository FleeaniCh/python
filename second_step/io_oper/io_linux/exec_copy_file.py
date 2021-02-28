# coding=utf-8
"""
    1.编写一个文件拷贝程序，从终端输入一个文件，将文件保存在当前目录下
    *文件类型不确定（可能是文本文件，可能是二进制文件）

    2
"""

'''
ori_file = open('test.py','rb')
data = ori_file.read()  #文件特别大，就不适合一次性读取
print(data)

des_file = open('test_1.txt','wb')
des_file.write(data)

ori_file.close()
des_file.close()
'''

# 输入文件名
filename = input("File: ")
try:
    fr = open(filename, 'rb')   # 二进制打开
except FileNotFoundError as e:
    print(e)
else:
    fw = open('file.jpg','wb')  # 二进制写入
    # 循环读取文件直到最后
    while True:
        data = fr.read(1024)
        if not data:    # 文件读取结束
            break
        fw.write(data)  #将读取内容写入
    fr.close()
    fw.close()