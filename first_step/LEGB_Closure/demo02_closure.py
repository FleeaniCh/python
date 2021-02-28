"""
    闭包：三大要素
            作用：fun01执行完毕后栈帧没有立即释放，而是等着fun02执行
            定义：指的是两个函数的执行环境整合
"""
def fun01():
    a = 1
    def fun02():
        print(a)

    return fun02

"""
# 调用外部函数，返回值是内嵌函数
result = fun01()
# 调用内嵌函数
result() #可以访问外部变量a
"""

# 闭包应用
# 压岁钱
def give_life_money(money):
    """
        得到压岁钱
    :return:
    """
    print("得到了%d压岁钱"%money)
    def child_buy(target,price):
        """
            孩子购买商品
        :param target:需要购买的商品
        :param price:商品的单价
        :return:
        """
        nonlocal money#声明外部嵌套作用域变量
        if money >= price:
            money -= price
            print("孩子花了%.1f元钱，购买了%s"%(price,money))
        else:
            print("金额不足")

    return child_buy

# 下列代码是一个连续的逻辑
action = give_life_money(10000)
action("唐僧肉",0.5)
action("小汽车",2000)
action("手机",8000)
