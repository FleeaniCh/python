"""
    .编写一个程序，向一个文件中写入如下内容：
        1.2021-1-1    21:21:21
        2.2021-1-1    21:21:22
        3.  ......
        4.2021-1-1  21:21:27

        循环每个1s写入一次，序号从1排列
        ctrl-c结束程序，下次启动程序，序号与之前的衔接
"""
import time

f = open('log.txt', 'a+')
f.seek(0, 0)  # 文件偏移量移动到开头

n = 0
for line in f:
    n += 1  # 获取现有多少行

while True:
    n += 1
    time.sleep(1)
    s = "%d. %s" % (n, time.strftime("%Y-%m-%d %H:%M:%S"))
    f.write(s + '\n')
    f.flush()  # 随时查看


