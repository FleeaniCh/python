"""
    #  练习
    1. 创建学生类
        ——数据：姓名，年龄，成绩，性别
        ——行为：在控制台打印个人信息的方法
    2. 在控制台中循环录入学生信息，如果名称为空，退出录入
    3. 在控制台中输入每个学生信息（调用打印学生类的打印方法）
    4. 打印第一个学生信息
"""


class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        print("学生的姓名是%s，年龄是%d，分数为%.1f，性别为%s" %
              (self.name, self.age, self.score, self.sex))


students_list = []
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    age = int(input("请输入学生年龄："))
    score = float(input("请输入学生成绩："))
    sex = input("请输入学生性别：")
    # 之前使用字典表达一个具体学生信息
    # dict_info = {"name": name, "age": age, "score": score, "gender": gender}
    stu = Student(name, age, score, sex)
    students_list.append(stu)

# 打印第一个学生信息
if len(students_list) == 0:
    print("No students in list.")
else:
    students_list[0].print_self_info()
