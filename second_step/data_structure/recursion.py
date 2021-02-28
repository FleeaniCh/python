"""
    求一个数的阶乘
    递归实现:
            1.终止条件
            2.递推：逐层调用
"""
"""
def factorial(num):
    # 定义一个函数，参数传入整数，返回该整数的阶乘
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product
"""
# print(factorial(5))

def recursion(num):
    if num<=1:
        return 1
    return num*recursion(num-1)

print("n! = ",recursion(5))