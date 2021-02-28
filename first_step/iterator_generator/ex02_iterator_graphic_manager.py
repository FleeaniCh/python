class Graphic:
    pass


class GraphicIterator:
    """
        图形迭代器
    """
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        tmp = self.__target[self.__index]
        self.__index += 1
        return tmp


class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):
        return GraphicIterator(self.__graphics)

# ---------------测试代码-----------------
manager = GraphicManager()
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())

manager_iterator = manager.__iter__()
while True:
    try:
        item = manager_iterator.__next__()
        print(item)
    except StopIteration:
        break
