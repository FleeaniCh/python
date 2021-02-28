class Wife:

    def __init__(self, name, age, weight):
        self.name = name
        # 私有化本质：障眼法(实际将变量名改为：_类名__age)
        # self.__age = age
        self.set_age(age)
        # self.__weight = weight
        self.set_weight(weight)

    # 提供公开的读写方法
    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 30:
            self.__age = value
        else:
            raise ValueError("我不要")

    # 提供公开的读写方法
    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if 40 < value < 58:
            self.__weight = value
        else:
            raise ValueError("我不要")


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
w01 = Wife("铁锤公主", 29, 87)
# w01.set_age(107)
print(w01.get_age())
