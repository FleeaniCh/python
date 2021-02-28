"""
    手雷炸了，可能伤害敌人/玩家的生命，
                        还可能未知事物（伤害鸭子，房子.......）
    要求：增加了新事物，不影响手雷
    体会：继承的作用
                多态的体现
                设计原则
                        开闭原则
                        单一职责
                        依赖倒置
"""


# 客户端代码
class Grenades:
    def __init__(self, atk):
        self.atk = atk

    def explode(self, damage_target):
        # 如果传入的不是子类，则异常
        if not isinstance(damage_target, Damageable):
            raise NotImplementedError("不是Damageable的子类")
        print("爆炸")
        # 多态：
        # 调用父类代表(玩家/敌人......)的可以受伤者
        # 执行子类(具体玩家/敌人......)
        damage_target.damage(self.atk)


class Damageable:
    """
        可以受伤
        继承：统一多个子类的概念，隔离变化
    """
    def damage(self, value):
        # 如果子类不重写，则异常
        raise NotImplementedError()


class Player(Damageable):
    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        print("玩家受伤了")
        self.hp -= value


class Enemy(Damageable):
    def damage2(self, value):
        print("敌人受伤了")


g01 = Grenades(100)
p01 = Player(300)
e01 = Enemy()
g01.explode(e01)
