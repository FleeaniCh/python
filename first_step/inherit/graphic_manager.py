"""
    定义图形管理器类
                1.管理所有图形
                2.提供计算所有图形总面积的方法

    具体图形：
            圆形
            矩形

    测试：
            创建1个圆形对象，1个矩形对象，添加到图像管理器中
            调用图形管理器的计算面积方法，输出结果

    要求：增加新图形，不修改图形管理器的代码
"""

# 客户端代码
class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        if isinstance(graphic, Graphic):
            self.__graphics.append(graphic)
        else:
            raise ValueError()

    def get_total_area(self):
        total_area = 0
        for graphic in self.__graphics:
            # 多态：调用父类方法，执行子类方法
            total_area += graphic.caculate_area()
        return total_area


class Graphic:
    # 继承
    def caculate_area(self):
        # 如果子类不重写，则异常
        raise NotImplementedError()


class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    def caculate_area(self):
        return 2 * 3.14 * (self.r ** 2)


class Rectangle(Graphic):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def caculate_area(self):
        return self.length * self.width


gm = GraphicManager()
c01 = Circle(2)
r01 = Rectangle(3, 4)
gm.add_graphic(c01)
gm.add_graphic(r01)

re = gm.get_total_area()
print(re)
