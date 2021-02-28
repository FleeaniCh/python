"""
read_db.py      读操作示例（select）
"""
import pymysql

host = '192.168.214.139'

# 连接数据库
db = pymysql.connect(host=host,
                     port=3306,
                     user='root',
                     password='root',
                     database='stu',
                     charset='utf8')

# 获取游标（操作数据库，执行sql语句）
cur = db.cursor()

# 获取数据库数据
# sql = "select * from class_1 where gender='m';"
sql = "select * from class_1;"
cur.execute(sql)    # 执行正确后cur调用函数获取结果

# # 获取一个查询结果
# one_row = cur.fetchone()
# print(one_row)  # 元组：(2, 'Baron', 18, 'm', 93.0, datetime.date(2020, 2, 29))
#
# # 获取多个查询结果
# many_row = cur.fetchmany(2)
# print(many_row)

# 获取所有查询结果
all_row = cur.fetchall()
print(all_row)

# 关闭数据库
cur.close()
db.close()