class Vector2:
    """
        二维向量
        可以表示位置/方向
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 函数：表示左边的方向
    @staticmethod
    def left():
        return Vector2(0, -1)

    # 函数：表示右边的方向
    @staticmethod
    def right():
        return Vector2(0, 1)

    # 函数：表示向上的方向
    @staticmethod
    def up():
        return Vector2(-1, 0)

    # 函数：表示向下的方向
    @staticmethod
    def down():
        return Vector2(1, 0)


class DoubleListHelper:
    """
        在二维列表中获取指定位置的，某个方向的，指定数量的元素
    """
    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        """
            在二维列表中获取指定位置的，某个方向的，指定数量的元素
        :param target: 二维列表
        :param vect_pos: 位置
        :param vect_dir: 方向
        :param count: 数量
        :return: 列表
        """
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result
