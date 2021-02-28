"""
    设计角度：
"""
# 数据角度
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_self(self):
        print(self.name, self.age)

s01 = Student("无忌哥哥", 28)
# 通过对象调用实例成员
s01.name = "张无忌"
s01.print_self()


class Student02:
    # 主流做法，必须掌握
    def __init__(self, name, age):
        self.name = name
        # self.__age = age
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self,value):
        self__age= value


s01 = Student02("无忌哥哥", 28)
s01.name = "张无忌"


class Student03:
    # 主流做法，必须掌握
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __get_age(self):
        return self.__age

    def __set_age(self,value):
        self__age= value

    age = property(None, __set_age)#只写 unreadable attribute


s01 = Student03("无忌哥哥", 28)
s01.name = "张无忌"
# print(s01.age)


class Student04:

    def __init__(self, name, age):
        self.name = name
        # 只读
        self.__age = age

    @property
    def age(self):
        return self.__age


s01 = Student04("无忌哥哥", 28)
s01.name = "张无忌"
print(s01.age)


class Student05:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __set_age(self, value):
        self.__age = value

    # 只写
    age = property(None, __set_age)


class Student07:
    __slots__ = ("name")#限制类创建的对象只能有固定的实例变量
    def __init__(self,name):
        self.name = name

s07 = Student07("wj")
s07.nmae = "无忌"
print(s07.nmae)