"""
    定义MyRange类，实现下列功能:
        for item in range(10):
            print(item)
"""

class MyRange:
    def __init__(self, stop_value):
        self.__stop_value = stop_value

    def __iter__(self):
        return MyRangeIterator(self.__stop_value)

class MyRangeIterator:
    def __init__(self, end_value):
        self.__end_value = end_value
        self.__number = 0

    def __next__(self):
        if self.__number >self.__end_value-1:
            raise StopIteration
        tmp = self.__number
        self.__number += 1
        return tmp

# next一次，计算一次，返回一次
for item in MyRange(7):
    print(item)

