# 违反了开闭原则
# 如果增加了火车，需要增加“火车类”，再修改“人”类中的go_to()方法

class Vehicle:
    # 继承：隔离子类变化，将子类的共性提取到父类(运输)中
    """
        交通工具，代表所有的交通工具
    """
    def transport(self, str_position):
        # 因为父类过于抽象，所以写不出方法体
        pass


# 客户端代码，用交通工具
class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, vehicle, str_position):
        # 调用交通工具的运输方法
        # 多态：调用父，执行子
        vehicle.transport(str_position)


class Car:
    def transport(self, str_position):
        print("汽车开到", str_position)


class Airplane:
    def transport(self, str_position):
        print("飞机飞到", str_position)


p01 = Person("老张")
c01 = Car()
a01 = Airplane()
p01.go_to(c01, "东北")
p01.go_to(a01, "东北")
