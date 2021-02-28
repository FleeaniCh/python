"""
    练习：编写一个接口，获取一段文字，判定文字中括号是否匹配正确，
    如果正确则打印正确，不正确则指出出错的地方。
"""
from lstack import *

text = "When an Open Data (standard) is created and promoted, " \
       "it’s [important ]to think why - what change is th=is {trying (to] drive}? " \
       "What will people do with this data that they couldn’t do before?"

# 将验证条件提前定义好
parens = "()[]{}"  # 需要特殊处理的字符集
left_parens = "([{"  # 入栈字符集
# 验证匹配关系
opposite = {'}': '{', ']': '[', ')': '('}

ls = LStack()  # 存储括号的栈


# 编写生成器，用来遍历字符串，不断的提供括号及其位置
def paren(text):
    # i 表示遍历字符串的索引位置
    i, text_len = 0, len(text)

    # 开始循环遍历字符串
    while True:
        while i < text_len and text[i] not in parens:
            i += 1
        # 到字符串结尾
        if i >= text_len:
            return
        else:
            yield text[i], i
            i += 1


# for i,j in paren(text):
#     print(i,j)
# 功能函数判断提供的括号是否匹配
def ver():
    for pr, i in paren(text):
        if pr in left_parens:
            ls.push((pr, i))  # 左括号入栈
        elif ls.is_empty() or ls.pop()[0] != opposite[pr]:
            print("Unmatching is found %d for %s" % (i, pr))
            break
    else:
        if ls.is_empty():
            print("All paren are matched")
        else:
            # 左括号多了
            d = ls.pop()
            print("Unmatching is found %d for %s" % (d[1], d[0]))


# 逻辑验证
ver()
