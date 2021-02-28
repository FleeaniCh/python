def fun07(a, b, *args, c=0, d, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)


fun07(1, 2, 3, 4, 5, 6, 7, d=9, e=8, f=9)


# 位置实参无限 + 关键字实参无限
def fun01(*args, **kwargs):
    print(args)
    print(kwargs)

fun01()
fun01(1,2,3,a=4,c=5)
