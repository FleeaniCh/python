import re

print(re.findall('\d+\*\*\d+', "2**16"))

print(re.findall('-?\d+\S+', "12 -36 28 1.34 -3.8"))
print(re.findall('-?\d+\.?\d*', "12 -36 28 1.34 -3.8"))

print(re.findall('\\$\\d+', "日薪：$100"))
print(re.findall('\$\d+', "日薪：$100"))

print(re.findall('\\\\', "\\"))

s = "hello \n world"
print(s)

# 贪婪模式与非贪婪模式
s = "[花千骨],[陆贞传奇],[新还珠格格],[楚乔传]"
print(re.findall(r'\[\w+\]', s))

print(re.findall(r'\[.+\]', s)) # 贪婪模式：尽可能重复多的
print(re.findall(r'\[.+?\]', s)) # 非贪婪模式
