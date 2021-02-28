def fun01(a, b, c):
    print(a)
    print(b)
    print(c)


# 位置实参
fun01(1, 2, 3)
list01 = [1, 2, 3]

# 星号：拆分序列
fun01(*list01)

dict01 = {"a": 1, "b": 3, "c": 2}

# 双星号：拆分字典
fun01(**dict01)

def fun02(a, b=0, c=0):
    print(a)
    print(b)
    print(c)


# 关键字实参
fun02(1,c=3)

# 将实参合并成一个元组
def fun03(*args):
    print(*args)

fun03(2,3,4,5,4)

# 将实参合并成一个字典
def fun04(**kwargs):
    print(kwargs)

fun04(a=3,b=4)

def fun05(*,name):# 命名关键字形参
    print(name)

fun05(name=" ")

print("#","*","%",sep="-----",end=" ")

