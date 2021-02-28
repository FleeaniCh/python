"""
    定义MyRange类，实现下列功能:
        for item in range(10):
            print(item)
"""

class MyRange:
    def __init__(self, stop_value):
        self.__stop_value = stop_value

    def __iter__(self):
        # return MyRangeIterator(self.__stop_value)
        # yield作用：将下列代码改成迭代器模式的代码
        # 生成迭代器代码的大致规则：
        # 1.将yield以前的语句定义在__next__()中
        # 2.将yield后面的数据作为__next__()的返回值
        number = 0
        while number <self.__stop_value:
            yield number
            number += 1


"""
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
"""

# # next一次，计算一次，返回一次
# for item in MyRange(7):
#     print(item)

