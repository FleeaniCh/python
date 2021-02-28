class Wife:

    def __init__(self, name, age, weight):
        self.name = name
        # 私有化本质：障眼法(实际将变量名改为：_类名__age)
        self.age = age
        # self.set_weight(weight)
        self.weight = weight

    @property#创建property对象，只负责拦截读取操作
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 30:
            self.__age = value
        else:
            raise ValueError("我不要")

    # 属性 property拦截对age的读写操作
    # age = property(get_age,set_age)

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if 40 < value < 58:
            self.__weight = value
        else:
            raise ValueError("我不要")

    # weight = property(get_weight,set_weight)


"""
w01 = Wife("铁锤公主", 87, 87)
w01.age = 107  # 重新创建了新变量：age
# w01.__age = 107#重新创建了新变量：__age
w01._Wife__age = 107  # 修改类中定义的私有变量
print(w01.name)
print(w01.age)
print(w01.__dict__)  # python内置变量，存储对象的实例变量
# {'name': '铁锤公主', '_Wife__age': 87, '_Wife__weight': 87, 'age': 107}
# print(w01.weight)
"""
w01 = Wife("铁锤公主", 30, 50)
w01.age = 25
print(w01.age)
print(w01.__dict__)
