"""
    运算符重载
"""
class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def __add__(self, other):
        return Vector1(self.x+other)

    def __radd__(self, other):
        return Vector1(self.x+other)

    def __iadd__(self, other):
        self.x += other
        return self

v01 = Vector1(10)
# print(v01+2)
# print(2+v01)
v01 += 2
print(v01,id(v01))