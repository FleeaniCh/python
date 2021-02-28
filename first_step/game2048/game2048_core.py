"""
    2048    游戏核心算法
"""
# 1.[2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]

list_merge = [2, 2, 2, 0]


def zero_to_end():
    """
        零元素移动到末尾
    """
    # 从后向前，如果发现零元素，删除并追加
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# zero_to_end()
# print(list_merge)

def merge():
    """
        合并相同元素
    """
    # 思想：先将中间的零元素移动至末尾
    # 再合并相邻相同元素
    zero_to_end()
    # print(list_merge)#去零
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            # 将后一个累加前一个之上
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)
            # print(list_merge)


# merge()
# print(list_merge)

map = [
    [2, 0, 0, 2],
    [4, 4, 2, 2],
    [2, 4, 0, 4],
    [0, 0, 0, 2]
]


def move_left():
    """
        向左移动
    """
    # 思想：将二维列表中每行(从左往右)交给merge处理
    for line in map:
        global list_merge  # 在函数内部只能读全局变量，想要赋值必须使用global
        list_merge = line
        merge()


# move_left()
# print(map)

def move_right():
    """
        向右移动
    """
    # 思想：将二维列表中每行(从右往左)交给merge函数操作
    for line in map:
        global list_merge
        # 从右向左取出数据  形成新列表
        list_merge = line[:: -1]  # (读取)切片：返回新的列表给list_merge
        merge()
        # 从右向左接收    合并后的数据
        line[::-1] = list_merge  # 返回的新的列表赋值给原来的列表(此时通过切片定位列表元素)


# move_right()
# print(map)


def square_matrix_transpose(sqr_matrix):
    """
        矩阵转置函数
    """
    for c in range(1, len(sqr_matrix)):
        for r in range(c, len(sqr_matrix)):
            sqr_matrix[r][c - 1], sqr_matrix[c - 1][r] = sqr_matrix[c - 1][r], sqr_matrix[r][c - 1]


def move_up():
    """
        上移
    """
    square_matrix_transpose(map)
    move_left()
    square_matrix_transpose(map)


def move_down():
    """
        下移
    """
    square_matrix_transpose(map)
    move_right()
    square_matrix_transpose(map)


move_down()
print(map)
