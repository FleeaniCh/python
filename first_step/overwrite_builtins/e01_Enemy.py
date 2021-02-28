class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    # 对象 --> 字符串（随意格式）
    def __str__(self):
        return "姓名：%s，血量：%d，攻击力：%d，防御力：%d" % (self.name, self.hp, self.atk, self.defense)

    # 对象 --> 字符串（python代码格式）
    def __repr__(self):
        return "Enemy('%s',%d,%d,%d)" % (self.name, self.hp, self.atk, self.defense)


e01 = Enemy("灭霸", 5000, 13099, 690)
print(e01)

e02 = eval(repr(e01))  # 克隆对象e01
e02.name = "玄冥二老"
print(e01.name)
print(e02)
