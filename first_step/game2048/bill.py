"""
    游戏逻辑控制器
"""
from model import *
import random


class GameCoreControll:

    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移动到末尾
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合并相同元素
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                # 将后一个累加前一个之上
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __move_left(self):
        """
            向左移动
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        """
            向右移动
        """
        for line in self.__map:
            self.__list_merge = line[:: -1]  # (读取)切片：返回新的列表给list_merge
            self.__merge()
            line[::-1] = self.__list_merge  # 返回的新的列表赋值给原来的列表(此时通过切片定位列表元素)

    def __square_matrix_transpose(self):
        """
            矩阵转置函数
        """
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]

    def __move_up(self):
        """
            上移
        """
        self.__square_matrix_transpose()
        self.__move_left()
        self.__square_matrix_transpose()

    def __move_down(self):
        """
            下移
        """
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    def move(self, dir):
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()

    """
    def generate_new_number(self):
        list_empty_location = []
        # 思路：选出所有的空白位置，再随机挑选一个
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    # 记录r   c
                    list_empty_location.append((r, c))
        # 确定哪个空白位置1     0
        loc = random.choice(list_empty_location)
        # 产生随机数
        if random.randint(1, 10) == 1:
            self.__map[loc[0]][loc[1]] = 4
        else:
            self.__map[loc[0]][loc[1]] = 2
    """

    def generate_new_number(self):
        # 获取所有空白位置
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        # 产生一个随机数
        loc = random.choice(self.__list_empty_location)
        if random.randint(1, 10) == 1:
            self.__map[loc.r_index][loc.c_index] = 4
        else:
            self.__map[loc.r_index][loc.c_index] = 2
        # 因为在该位置生成了新数字，所以该位置就不是空位置了
        self.__list_empty_location.remove(loc)

    def __get_empty_location(self):
        # list_empty_location = []
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(Location(r, c))

    def is_game_over(self):
        """
            游戏是否结束
        :return: False表示没有结束
        """
        # 是否具有空位置
        if len(self.__list_empty_location) > 0:
            return False

        # # 判断横向有无相同的元素
        # for r in range(len(self.__map)):
        #     for c in range(len(self.__map[r])-1):
        #         if self.__map[r][c] == self.__map[r][c+1]:
        #             return False
        #
        # # 判断竖向有无相同的元素
        # for c in range(len(self.__map)):
        #     for r in range(len(self.__map[c])-1):
        #         if self.__map[r][c] == self.__map[r+1][c]:
        #             return False

        for r in range(len(self.__map)):
            for c in range(len(self.__map[r]) - 1):
                if self.__map[r][c] == self.__map[r][c + 1] or self.__map[c][r] == self.__map[c + 1][r]:
                    return False

        return True


# -------------------测试代码----------------------
if __name__ == '__main__':
    controller = GameCoreControll()
    # controller.move_left()
    # controller.move_up()
    # controller.__move_right()
    # controller.move(DirectionModel.LEFT)
    controller.generate_new_number()
    print(controller.map)
