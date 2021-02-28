"""
    正则匹配练习
"""
import re
# 1. 匹配一个.com邮箱格式字符串
# print(re.findall(r'\S+\.com',"2316231830@qq.com 17355641830@163.com 18531244286@qq.cn.com"))
print(re.findall(r'\w+@\w+\.com',"2316231830@qq.com 17355641830@163.com 18531244286@qq.cn.com"))

# 2. 匹配一个密码 8-12位数字字母下划线构成
print(re.findall(r'\w{8,12}',"xdcg123_ deuwqgfb-cdsbacfbj123"))

# 3. 匹配一个数字     整数，负数，正数，小数，分数1/2，百分数45%
print(re.findall(r'-?\d+\.?/?\d%?',"12,-13,1/2,1/3,45%"))

# 4. 匹配一段文字中以大写字母开头的单词，注意文字中可能有 iPython(不算)， H-base(算)
# 单词可能有大小字母，小写字母，横杆，下划线
s = "A-bdehb n你好吗, THE N_GOOD,tEA Teacher你 iPython H-base"
# print(re.findall('[A-Z]-?\w+[A-Za-z]+',s))
print(re.findall(r'\b[A-Z][-_a-zA-Z]*',s))