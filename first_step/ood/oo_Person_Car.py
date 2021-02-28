"""
    封装设计思想
                需求：老张开车去东北
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def go_to(self, str_position, type):#type：Person类与Car类交互
        print(self.name, "去", str_position)
        type.run(str_position)


class Car:
    def run(self, str_position):
        print("行驶到: " + str_position)


lz = Person("老张")
car = Car()
# 老张开车去东北
lz.go_to("东北", car)
