"""
    regex.py    re模块    功能函数演示
"""
import re

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"\w+:\d+"  # 正则表达式
# pattern = r"(\w+):(\d+)"  # 正则表达式：包含子组

# re 模块直接调用findall()
l = re.findall(pattern, s)
print(l)  # ['Alex:1994', 'Sunny:1996']
# print(l)    # [('Alex', '1994'), ('Sunny', '1996')]

# compile   对象调用
regex = re.compile(pattern)  # 生成正则表达式对象
# l = regex.findall(s)
l = regex.findall(s, 0, 12)
print(l)  # ['Alex:1994', 'Sunny:1996']

# 按照正则表达式匹配内容切割字符串
l = re.split(r'[:,]', s)
print(l)

# 替换目标字符串
# s = re.sub(r':', '-',s)
# s = re.sub(r':', '-',s,1)
s = re.subn(r':', '-', s, 1)  # n：替换几处
print(s)
