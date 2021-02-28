class Student:
    def __init__(self, name, age, score, sex):
        # 创建实例变量
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        # 读取实例变量
        print("学生的姓名是%s，年龄是%d，分数为%.1f，性别为%s" %
              (self.name, self.age, self.score, self.sex))


list01 = [
    Student("赵敏",28,100,"女"),
    Student("苏大强",68,72,"男")
]

s01 = list01[0]
s01.name = "小昭"
s01.score = 98
print(list01[0].name, list01[0].score)