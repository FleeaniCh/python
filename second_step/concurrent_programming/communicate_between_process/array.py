"""
array.py    共享内存存放一组数据
"""

from multiprocessing import Process, Array

# 创建共享内存，初始包含[1, 2, 3, 4]
# shm = Array('i', [1, 2, 3, 4])
# shm = Array('i',5)  # 初始开辟5个整型空间，默认为0
shm = Array('c',b'hello')   # 字节串

def fun():
    # Array创建的共享内存对象可迭代
    shm[1] = b'H'   # 修改共享内存
    for i in shm:
        print(i)


if __name__ == '__main__':

    p = Process(target=fun)
    p.start()
    p.join()
    for i in shm:
        print(i)
    print(shm.value)    # 只能用于打印字节串