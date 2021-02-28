"""
    继承——变量
"""


class Person:
    def __init__(self, name):
        self.name = name


"""
class Student(Person):
    # 1.子类若没有构造函数，则使用父类的
    pass

s01 = Student()
print(s01.name)
"""


class Student(Person):
    # 2.子类若具有构造函数，则必须先调用父类的构造函数
    def __init__(self, name, score):
        super().__init__(name)
        self.score = score


p01 = Person("李四")
print(p01.name)

s01 = Student("kai", 100)
print(s01.score)
print(s01.name)
