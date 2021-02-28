"""
    file_read.py
    文件读取演示
"""

# 打开文件
f = open('test.py', 'r')  # #打开图片(字节串)

# # read循环读取指定的字符个数（不指定会读取全部内容）
# while True:
#     # 读到文件结尾，返回空字符串
#     data = f.read(50)  # 每次最多读100字符
#     if not data:  # 读到结尾跳出循环
#         break
#     print(data)


# # readline读取
# # 读取一行内容
# data = f.readline(10)  # 读取前10个字符
# print("一行内容：", data)
# data = f.readline()
# print("一行内容：", data)  # 读完第一行剩余内容


# readlines读取：将读取的内容形成列表
# 将内容读取为列表
data = f.readlines(18)  #前18个字符所在的行作为读取对象
print(data)


# f为可迭代对象
# for line in f:
#     print(line)    # 每次迭代到一行内容

# 关闭
f.close()
