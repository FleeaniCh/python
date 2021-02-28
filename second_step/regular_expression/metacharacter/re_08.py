"""
    $   匹配目标字符串的结尾位置
"""
import re
print(re.findall('Jame$',"Hi,Jame"))
print(re.findall('Jame$',"Hi,Jame,now"))

# ^  与 $    同时出现
print(re.findall('^Jame$',"Jame"))  # 完全匹配