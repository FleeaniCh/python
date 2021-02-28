"""
    体会：类区别行为的不同
"""


class Player:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    def attack(self, other):
        # 打的逻辑
        print("玩家攻击敌人")
        # 通过敌人对象地址，调用实例方法
        other.damage(self.atk)

    def damage(self, value):
        print("玩家受伤")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("玩家死咯")
        print("游戏结束")


class Enemy:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    def damage(self, value):
        print("敌人受伤啦")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    # 私有的死亡方法
    def __death(self):
        # 死亡的逻辑
        print("死亡")
        print("掉装备")
        print("死亡")

    def attack(self, other):
        print("敌人攻击玩家")
        other.damage(self.atk)


p01 = Player(10,100)
e01 = Enemy(5,20)
p01.attack(e01)
e01.attack(p01)
p01.attack(e01)


