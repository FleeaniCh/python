"""
    定义函数，在控制台中获取成绩函数
    要求：如果异常，继续获取成绩，直到得到正确的成绩为止；
                成绩还必须在0--100之间
"""


def get_score():
    while True:
        try:
            score = int(input("请输入成绩："))
        except Exception:
            print("未知错误")
            continue
        if 0 <= score <= 100:
            return score


re = get_score()
print("录入的成绩为：%d" % re)
