"""
    regex2.py
    match   对象属性演示
"""
import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)  # 生成正则表达式对象
obj = regex.search('abcdefghi', 0, 8)  # match对象（截取了一部分）

# 属性变量
print(obj.pos)  # 目标字符串开始位置
print(obj.endpos)  # 目标字符串结束位置
print(obj.re)  # 正则表达式
print(obj.string)  # 全部目标字符串内容（非截取）
print(obj.lastgroup)  # 最后一组的组名
print(obj.lastindex)  # 最后一组的序列号

print("------------------------------")
# 属性方法
print(obj.span())  # 匹配内容在字符串中的位置
print(obj.start())
print(obj.end())
print(obj.groupdict())  # 生成捕获组字典   {'pig': 'ef'}
print(obj.groups())  # 子组对应内容的元组 ('ab', 'ef')
print(obj.group())  # abcdef    获取match对应的内容
print(obj.group(1))  # ab
print(obj.group('pig'))  # ef
