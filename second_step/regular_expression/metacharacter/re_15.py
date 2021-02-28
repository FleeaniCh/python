"""
    分组
        一个正则表达式可以包含多个子组
"""
import re

print(re.findall(r'ab+', "ababababababab"))

print(re.search(r'(ab)+', "ababababab").group())

print(re.search(r'王|李\w{1,3}', "李世民").group())
print(re.search(r'(王|李)\w{1,3}', "王者荣耀").group())

print(re.search(r'(https|http|ftp|file)://\S+', "https://www.baidu.com").group())  # https://www.baidu.com
print(re.search(r'(https|http|ftp|file)://\S+', "https://www.baidu.com").group(1))  # https

# 捕获组
print(re.search(r'(?P<pig>ab)+',"ababababab").group())
print(re.search(r'(?P<pig>ab)+',"ababababab").group('pig'))

# 匹配身份证号
print(re.search(r'\d{17}(\d|x)',"身份证号：34088119930702950x").group())
