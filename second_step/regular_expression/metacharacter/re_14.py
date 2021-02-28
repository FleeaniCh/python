import re

# 匹配任意(非)数字字符  \d  \D
print(re.findall('\d{1,5}', "Mysql:3306, http:80"))  # 匹配数字字符
print(re.findall('\D+', "Mysql:3306, http:80"))  # 匹配非数字字符

# 匹配任意(非)普通字符   \w  \W
print(re.findall('\w+', "server_port = 8888"))  # 匹配普通字符：数字、字母、下划线、汉字
print(re.findall('\W+', "server_port = 8888"))  # 匹配非普通字符
print(re.findall('\w+', "server_port = 三个八"))  # 匹配非普通字符

# 匹配任意(非)空字符   \s  \S
print(re.findall('\w+\s+\w+', "hello   world"))  # 匹配空字符：空格、\r、\n、\t、\v、\f
print(re.findall('\S+', "hello  world"))  # 匹配非空字符

# 匹配开头结尾位置     \A   \Z
print(re.findall('\Aworld', "hello world"))  # 匹配开头
print(re.findall('world\Z', "hello world"))  # 匹配结尾

# 匹配(非)单词边界位置   \b  \B
print(re.findall(r'\bis\b', "Thisa is a test."))  # 匹配单词边界：数字字母下划线汉字与其他字符交界的位置
print(re.findall(r'\Bis\b', "Thisa is a test."))  # 匹配非单词边界
print(re.findall(r'\b\d+\b', "123 65 a Num007"))  # 匹配非单词边界
