"""
    定义父类
                车(数据：品牌，速度)

    定义子类
                电动车(数据：电池容量，充电功率)

    创建对象
    画出内存图
"""


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Electrocar(Car):
    def __init__(self, brand, speed, battery_cap, power):
        super().__init__(brand, speed)
        self.battery_cap = battery_cap
        self.power = power


c01 = Car("Audi", 100)

e01 = Electrocar("Aima", 40, 100000, 500)
