class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        self.set_atk(atk)
        self.set_hp(hp)

    def get_atk(self):
        return self.__atk

    def set_atk(self, value):
        if 10 <= value <= 50:  # 定义攻击力的范围
            self.__atk = value
        else:
            raise ValueError("非正常人类攻击力！")

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if 100 <= value <= 200:#定义血量的范围
            self.__hp = value
        else:
            raise ValueError("非正常人类血量！")


e01 = Enemy("FuckX", 50, 101)
print(e01.get_atk(),e01.get_hp())
