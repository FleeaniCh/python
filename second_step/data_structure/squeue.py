"""
    squeue.py   队列的顺序存储

    思路分析：
    1.基于列表完成数据存储
    2.通过封装规定数据操作
    3.先确定列表的哪一端作为队列头
"""


# 自定义队列异常
class QueueError(Exception):
    pass


# 队列
class SQueue:
    def __init__(self):
        self._elems = []

    # 判断队列是否为空
    def is_empty(self):
        return self._elems == []

    # 入队
    def enqueue(self, val):
        self._elems.append(val)

    # 出队
    def dequeue(self):
        if not self._elems:
            raise QueueError("Queue is empty")
        return self._elems.pop(0)

    def show(self):
        for item in self._elems:
            print(item, end=" ")
        print()


if __name__ == '__main__':
    sq = SQueue()
    # sq.enqueue(1)
    # sq.enqueue(3)
    # sq.enqueue(5)
    # sq.show()
    # print(sq.dequeue())
    for i in range(10):
        sq.enqueue(i)

    # #########将队列翻转##########
    from sstack import *
    ss = SStack()  # 栈
    # 循环出队入栈
    while not sq.is_empty():
        ss.push(sq.dequeue())
    # 循环出栈入队
    while not ss.is_empty():
        sq.enqueue(ss.pop())

    sq.show()
