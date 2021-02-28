"""
    练习：敌人类（攻击力0-100）
            抛出异常信息：消息/行/攻击力/错误编号
"""
class AtkError(Exception):
    def __init__(self,message,code_line,atk,error_number):
        self.message = message
        self.code_line = code_line
        self.atk = atk
        self.error_number = error_number


class Enemy:
    def __init__(self,atk):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self,value):
        if 0<=value<=100:
            self.__atk = value
        else:
            raise AtkError("超过我所想要的范围啦",24,value,10001)


e01 = Enemy(120)
