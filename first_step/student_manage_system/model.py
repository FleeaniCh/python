"""
    定义数据模型
"""
class StudentModel:
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
