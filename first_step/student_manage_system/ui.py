from model import StudentModel
from bll import StudentManagerController


class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_student(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        else:
            self.__output_student_by_score()

    def __input_student(self):
        name = input("请输入姓名：")
        age = self.input_data("请输入年龄：")
        score = self.input_data("请输入成绩：")
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def input_data(self, message):
        while True:
            try:
                input_data = int(input(message))
                return input_data
            except:
                print("输入有误，请重新输入！")
                continue

    def __output_student(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        id = self.input_data("请输入待删除的学生编号：")
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.id = self.input_data("请输入待修改学生编号：")
        stu.name = input("请输入姓名：")
        stu.age = self.input_data("请输入年龄：")
        stu.score = self.input_data("请输入成绩：")
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_student(self.__manager.stu_list)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
