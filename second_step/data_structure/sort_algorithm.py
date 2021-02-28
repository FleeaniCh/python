"""
    sort.py 排序算法训练

    (常识性代码)
"""


# 冒泡·：每次取相邻的两个元素比较，不合适就交换，依次向后
def bubble(list_):
    n = len(list_)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]  # 两两比较，每轮都会将最大的排至末尾
        # print(list_)


# l = [4, 9, 3, 1, 2, 5, 8, 4]
# bubble(l)
# print(l)


# 选择排序：取出第一个元素，依次与后面的元素进行比较，不合适交换位置，直至比较结束，
# 一轮可以确定开头一个，每轮确定一个元素，依次向后，n个元素需要n-1轮比较
def selection_sort(list_):
    # 每轮选出一个最小值
    for i in range(len(list_) - 1):
        for j in range(i + 1, len(list_)):
            if list_[i] > list_[j]:  # 假设list[i]为最小值(假设不正确进行交换)
                list_[i], list_[j] = list_[j], list_[i]


# 插入排序
def insert_sort(list_):
    # 外层循环用来控制比较的数是谁，从第二个数开始
    for i in range(1,len(list_)):
        x = list_[i]     #空出list_[i]的位置
        j = i-1
        while j>=0 and list_[j]>x:
            list_[j+1] = list_[j]
            j -= 1
        list_[j+1] = x


# 快速排序
# 完成一轮交换
def sub_sort(list_, low, high):
    # 选定基准
    x = list_[low]
    # low向后，high向前
    while low < high:
        # 后面的数往前放
        while list_[high] >= x and high > low:
            high -= 1
        list_[low] = list_[high]
        # 前面的数往后放
        while list_[low] < x and low < high:
            low += 1
        list_[high] = list_[low]
    list_[low] = x
    return low


def quick_sort(list_, low, high):
    if low < high:
        key = sub_sort(list_, low, high)
        quick_sort(list_, low, key - 1)
        quick_sort(list_, key + 1, high)


l = [4, 9, 3, 1, 2, 5, 8, 4]
quick_sort(l, 0, len(l) - 1)
print(l)
