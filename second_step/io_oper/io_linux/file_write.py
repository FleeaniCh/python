"""
    file_write.py
"""

# 打开文件
# f = open('test.py','w')
# f = open(r'E:\03-Python_Note\home\tarena\second_step\io_linux\img.jpg', 'wb')
f = open('test.py','a')    # 追加

# # 写操作
# f.write("hello 死鬼\n".encode())
# f.write("哎呀，干啥".encode())

# 将列表写入     需要人为添加换行
l = ['hello world\n','啊哈哈哈']
f.writelines(l)

# 关闭
f.close()
