# 方式1：
list01 = []
import double_list_helper as helper
re1 = helper.DoubleListHelper.get_elements(list01, helper.Vector2(1, 3), helper.Vector2.left(), 3)

# 方式2：
from double_list_helper import DoubleListHelper, Vector2
re2 = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)

# 方式3：
from double_list_helper import *
re3 = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)


