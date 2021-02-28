"""
    lqueque.py  链式队列
    重点代码

    思路分析：
    1.基于链表构建队列模型
    2.链表的开端作为队头，结尾位置作为队尾
    3.单独定义队尾标记，避免每次插入数据遍历
    4.队头和队尾重叠认为队列为空
"""


# 自定义队列异常
class QueueError(Exception):
    pass


# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 队列操作
class LQueue:
    def __init__(self):
        # 定义队头和队尾的属性变量
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front == self.rear
 
    def enqueue(self, val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
        self.front = self.front.next
        return self.front.val


if __name__ == '__main__':
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    print(lq.dequeue())