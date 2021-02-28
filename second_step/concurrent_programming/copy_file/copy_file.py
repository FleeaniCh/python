"""
    创建两个进程，分别复制一个文件的上下部分，将复制内容放到两个新的文件中,
    按字节数分文件
    进程数：父进程、子进程
"""
from multiprocessing import Process
import os

filename = r'./file.jpg'
size = os.path.getsize(filename)    # 获取文件大小
# 父进程创建fr   两个子进程使用这个fr会相互影响
# fr = open(filename,'rb')

# 复制上半部分
def top():
    fr = open(filename,'rb')
    fw = open('top.jpg','wb')
    n = size//2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open('bot.jpg', 'wb')
    fr.seek(size//2,0)  # 移动偏移量
    fw.write(fr.read())
    fr.close()
    fw.close()


if __name__ == '__main__':
    p1 = Process(target=top)
    p2 = Process(target=bot)
    p2.start()
    p1.start()
    p1.join()
    p2.join()




