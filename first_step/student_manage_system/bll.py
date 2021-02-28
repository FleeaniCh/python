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
        #         return True
        # return False