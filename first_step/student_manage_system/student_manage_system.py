"""
    学生管理系统
    项目计划：
                    1.完成数据模型类StudentModel
                    2.创建逻辑控制类StudentManagerController
                    3.完成数据：学生列表__stu_list
                    4.行为：获取列表   stu_list
                    5.添加学生方法    add_student
                    6.根据编号删除学生remove_student
"""


class StudentModel:
    """
        学生模型
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
            创建学生对象
        :param id: 编号（该学生对象的唯一标识）
        :param name: 姓名，str类型
        :param age: 年龄，int类型
        :param score: 成绩，float类型
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


class StudentManagerController:
    """
        学生管理控制器，负责业务逻辑处理
    """
    # 类变量，表示初始编号
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []  # 只读

    @property
    def stu_list(self):
        """
            学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
            添加一个新学生
        :param stu_info: 没有编号的学生信息
        """
        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, id):
        """
            移除学生信息
        :param id: 待删除的学生编号
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True  # 表示移除成功
        return False  # 表示移除失败

    def update_student(self, stu_info):
        """
            修改学生信息
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        """
            根据成绩对学生成绩进行升序排序
        """
        for i in range(len(self.stu_list) - 1):
            for j in range(i + 1, len(self.stu_list)):
                if self.stu_list[i].score > self.stu_list[j].score:
                    self.stu_list[i], self.stu_list[j] = self.stu_list[j], \
                                                         self.stu_list[i]
                return True
        return False


'''
# -------------测试代码---------------
manager = StudentManagerController()
s01 = StudnetModel("zs", 24, 100)
manager.add_student(s01)
manager.add_student(StudnetModel("ls", 24, 100))
for item in manager.stu_list:
    print(item.id)

print(manager.remove_student(1002))
for item in manager.stu_list:
    print(item.id)
'''


class StudentManagerView:
    """
        学生管理器视图
    """

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
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_student(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        id = int(input("请输入待删除的学生编号："))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.id = int(input("请输入待修改学生编号："))
        stu.name = input("请输入姓名：")
        stu.age = int(input("请输入年龄："))
        stu.score = int(input("请输入成绩："))
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


view = StudentManagerView()
view.main()
