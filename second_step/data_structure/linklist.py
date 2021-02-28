"""
    linklist.py
    功能：实现单链表的构建和功能操作
    重点代码
"""


# 创建节点类
class Node:
    def __init__(self, val, next=None):
        """
            思路：将自己定义的类视为节点的生成类，实例对象中
                      包含数据部分和指向下一节点的next
        """
        self.val = val  # 有用的数据
        self.next = next  # 寻找下一个节点关系


class LinkList:
    """
        思路：单链表类，生成对象后可以进行增删改查操作
                   具体操作通过调用具体方法完成
    """

    def __init__(self):
        """
            初始化链表，标记一个链表的开端，以便于获取后续的节点
        """
        self.head = Node(None)

    # 通过list_为链表添加一组节点
    def init_list(self, list_):
        p = self.head  # p作为移动变量
        for item in list_:
            p.next = Node(item)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.val, end=" ")
            p = p.next
        print()

    #  判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def append(self, val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 头部插入节点
    def head_insert(self, val):
        node = Node(val)  # 生成节点
        node.next = self.head.next  # 先连后面的节点
        self.head.next = node  # 再连头结点

    # 指定插入位置
    def insert(self, index, val):
        p = self.head
        for i in range(index):
            # 超出位置最大范围，结束循环
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除节点
    def delete(self, x):
        p = self.head
        # 结束循环必然两个条件其一为假
        while p.next and p.next.val != x:
            p = p.next
        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next

    # 获取某个节点值
    def get_index(self, index):
        p = self.head.next
        for i in range(index):
            if p.index is None:
                raise IndexError("list index out of range")
            p = p.next
        return p.val


if __name__ == '__main__':
    # node1 = Node(1)
    # node2 = Node(2, node1)  # node2.next == node1
    # node3 = Node(3, node2)
    l = LinkList()
    l.init_list([1, 2, 3, 4, 5])
    l.show()
