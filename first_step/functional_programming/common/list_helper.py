"""
    列表助手模块
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件的多个元素方法
        :param list_target:需要查找的列表
        :param func_condition:需要查找的条件，函数类型
                        函数名(参数) --> bool
        :return:需要查找的元素，生成器类型
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target, func_condition):
        """
            通用的查找某个条件的单个元素的方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件，函数类型
                        函数名(参数) --> bool
        :return: 需要查找的元素
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(list_target, func_condition):
        """通用的查找符合条件的数据数量"""
        count_value = 0
        for item in list_target:
            if func_condition(item):
                count_value += 1
        return count_value

    @staticmethod
    def is_exist(list_target, func_condition):
        """通用的判断是否存在某个条件元素的方法"""
        for item in list_target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def sum(list_target, func_handle):
        """
            通用的求和方法
        :param list_target:需要求和的列表
        :param func_handle:需要求和的处理逻辑
        :return:和
        """
        sum_value = 0
        for item in list_target:
            sum_value += func_handle(item)
        return sum_value

    @staticmethod
    def select(list_target, func_handle):
        """
            通用的筛选方法
        :param list_target: 需要筛选的方法
        :param func_handle: 需要筛选的逻辑
        :return: 生成器
        """
        # list_result = []
        for item in list_target:
            # list_result.append(func_handle(item))
            # return list_result
            yield func_handle(item)

    @staticmethod
    def get_max(list_target, func_handle):
        """
            通用的获取最大元素方法
        :param func_handle:需要搜索的处理逻辑
        :return:
        """
        max_value = list_target[0]
        for i in range(1, len(list_target)):
            if func_handle(max_value) < func_handle(list_target[i]):
                max_value = list_target[i]
        return max_value

    @staticmethod
    def get_min(list_target, func_handle):
        """
            通用的获取最大元素方法
        :param func_handle:需要搜索的处理逻辑
        :return:
        """
        min_value = list_target[0]
        for i in range(1, len(list_target)):
            if func_handle(min_value) > func_handle(list_target[i]):
                min_value = list_target[i]
        return min_value

    @staticmethod
    def order_by(list_target, func_handle):
        """
            通用升序排序方法
        :param list_target: 需要排序的数据
        :param func_handle: 排序的逻辑
                函数(参数) --> int/float......  需要比较的数据
        """
        for i in range(0, len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                # if list_target[i].atk > list_target[j].atk:
                if func_handle(list_target[i]) > func_handle(list_target[j]):
                    list_target[i], list_target[j] = list_target[j], list_target[i]

    @staticmethod
    def order_by_desc(list_target, func_handle):
        """
            通用降序排序方法
        :param list_target: 需要排序的数据
        :param func_handle: 排序的逻辑
                函数(参数) --> int/float......  需要比较的数据
        """
        for i in range(0, len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                # if list_target[i].atk > list_target[j].atk:
                if func_handle(list_target[i]) < func_handle(list_target[j]):
                    list_target[i], list_target[j] = list_target[j], list_target[i]

    @staticmethod
    def delete_all(list_target, func_handle):
        """
            根据指定条件删除元素
        :param list_target:需要操作的列表
        :param func_handle: 删除条件
        """
        for i in range(len(list_target) - 1, -1, -1):
            if func_handle(list_target[i]):
                del list_target[i]
