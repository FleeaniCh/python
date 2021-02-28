"""
将单词本存入数据库

1. 创建数据库   dict   (utf8)
2. 创建数据库表 words     将单词和解释存入不同的字段
3. 将单词存入words单词表    超过19500即可
"""
import pymysql
import  re

f = open('dict.txt')    # 打开文件

db = pymysql.connect(host='192.168.214.139',
                     port=3306,
                     user='root',
                     password='root',
                     database='dict')

# 获取游标(操作数据库，执行sql语句)
cur = db.cursor()
'''
data = f.readline()
tmp = data.split()
word = tmp[0]
mean = ' '.join(tmp[1:]).strip()
'''
sql = "insert into words(word,mean) values (%s,%s)"

for line in f:
    # 获取单词和解释
    tup = re.findall(r"(\S+)\s+(.*)",line)[0]
    print(tup)
    # try:
    #     cur.execute(sql,tup)
    #     db.commit()
    # except:
    #     db.rollback()

f.close()
#  关闭数据库
cur.close()
db.close()