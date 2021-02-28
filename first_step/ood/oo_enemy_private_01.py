class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        # self.set_atk(atk)
        # self.set_hp(hp)#创建对象时直接调用拦截方法
        self.atk = atk
        self.hp = hp#创建对象时间接调用拦截方法

    def get_atk(self):
        return self.__atk

    def set_atk(self, value):
        if 10 <= value <= 50:  # 定义攻击力的范围
            self.__atk = value
        else:
            raise ValueError("非正常人类攻击力！")

    # 拦截对实例变量atk的操作
    atk = property(get_atk,set_atk)

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if 100 <= value <= 200:#定义血量的范围
            self.__hp = value
        else:
            raise ValueError("非正常人类血量！")

    hp = property(get_hp, set_hp)


e01 = Enemy("FuckX", 50, 101)
e01.atk = 49
print(e01.atk,e01.hp)
print(e01.__dict__)
