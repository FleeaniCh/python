class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 10 <= value <= 50:  # 定义攻击力的范围
            self.__atk = value
        else:
            raise ValueError("非正常人类攻击力！")

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 100 <= value <= 200:#定义血量的范围
            self.__hp = value
        else:
            raise ValueError("非正常人类血量！")


e01 = Enemy("FuckX", 50, 99)
print(e01.atk,e01.hp)
