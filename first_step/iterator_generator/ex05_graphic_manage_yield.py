"""
    将迭代器版本的图形管理器改为yield方式实现
"""


class Graphic:
    pass


"""
class GraphicIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        tmp = self.__target[self.__index]
        self.__index += 1
        return tmp
"""


class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):
        # return GraphicIterator(self.__graphics)
        # self.__index = 0
        # while (self.__index < len(self.__graphics)):
        #     yield self.__graphics[self.__index]
        #     self.__index += 1
        # 执行过程：
        # 1. 调用当前方法，不执行。(内部创建迭代器对象)
        # 2. 调用__next__()才执行。
        # 3. 执行到yield语句，暂时离开。
        # 4. 再次调用__next__()方法，继续执行。
        # 5. 重复第3、4步骤，直至最后。
        for item in self.__graphics:
            yield item


manager = GraphicManager()
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())

for item in manager:
    print(item)
