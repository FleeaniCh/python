"""

"""


class Student:
    count = 0
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def print_self(self):
        print(self.name, self.sex)


s01 = Student("无忌", "男")
s02 = Student("赵敏", "女")
s01.print_self()
print(Student.count)


"""
# 也可以通过对象地址访问类成员(不建议使用)
print(s01.count)

# 可以通过类名访问实例方法，但必须手动传递对象地址(不建议使用)
Student.print_self(s01)

class Student:
    pass

s01 = Student()
s01.name = "无忌"
s01.sex = "男"
print(s01.name)
print(s01.sex)
"""
