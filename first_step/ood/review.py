class MyClass:
    def __init__(self, a):
        # 实例变量
        self.a = a

    def print_self(self):
        # 可以操作实例变量
        print(self.a)


m01 = MyClass(100)
m01.b = 1

m02 = MyClass(100)
# print(m02.b)
print(m02.a)


class MyClass02:
    a = 0

    @staticmethod
    def print_self(cls):
        print(cls.a)

print(MyClass02.a)