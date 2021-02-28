"""
    search.py   二分查找方法训练
"""

# list_为有序数列，key为要查找的关键值，返回key在数列中的索引号
"""
# 垃圾代码：取不到最后一个数的索引  
def search(list_, key):
    mid_index = (len(list_) - 1) // 2
    while True:
        if key > list_[mid_index]:
            mid_index = mid_index + (len(list_) - 1 - mid_index) // 2
        elif key < list_[mid_index]:
            mid_index = mid_index // 2
        else:
            break
    return mid_index
"""


def search(list_, key):
    low, high = 0, len(list_) - 1
    while low <= high:
        mid_index = (low + high) // 2
        if list_[mid_index] < key:
            low = mid_index + 1
        elif list_[mid_index] > key:
            high = mid_index - 1
        else:
            return mid_index


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("key index: ", search(l, 9))
