# 违反了开闭原则
# 如果增加了火车，需要增加“火车类”，再修改“人”类中的go_to()方法
class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, vehicle, str_position):
        if isinstance(vehicle, Car):
            vehicle.run(str_position)
        elif isinstance(vehicle, Airplane):
            vehicle.fly(str_position)


class Car:
    def run(self, str_position):
        print("汽车开到", str_position)


class Airplane:
    def fly(self, str_position):
        print("飞机飞到", str_position)


p01 = Person("老张")
c01 = Car()
p01.go_to(c01, "东北")
a01 = Airplane()
p01.go_to(a01, "东北")
