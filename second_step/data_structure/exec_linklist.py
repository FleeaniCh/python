# coding=utf-8
"""
    创建两个链表，两个链表中的值均为有序值
    将两个链表合并成一个，合并后要求值仍为有序值
"""
from linklist import *

l1 = LinkList()
l2 = LinkList()
l1.init_list([1, 5, 7, 8, 10, 12, 13, 19])
l2.init_list([2, 3, 4, 9, 16, 17, 20])
l1.show()
l2.show()


def merge(l1, l2):
    # 将l2合并到l1中
    p = l1.head
    q = l2.head.next
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            p = p.next
            q = tmp
    p.next = q


merge(l1, l2)
l1.show()
