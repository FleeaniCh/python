"""
    内置可重写函数
"""


class StudentModel:
    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    # 对象--> 字符串（随意格式）
    def __str__(self):
        return "我叫%s，编号是%d，年龄是%d岁，成绩是%d分" % (self.name, self.id, self.age, self.score)

    # 对象 --> 字符串（解释器可识别：格式有规定，满足python语法）
    # 返回python代码格式的字符串
    def __repr__(self):
        return 'StudentModel("%s", %d, %d, %d)' % (self.name, self.age, self.score, self.id)


s01 = StudentModel("无忌", 27, 100, 101)
# str01 = str(s01)
# print(str01)
print(s01)

s02 = repr(s01)
print(s02)
# 根据字符串执行python代码
re = eval("1+2*5")
print(re)

# repr返回python格式的字符串(创建对象)
# eval()根据字符串执行代码
s02 = eval(repr(s01))  # 克隆一个对象
s02.name = "老张"
print(s01.name)  # 无忌
print(type(s02))
