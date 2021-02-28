"""
    写操作
"""
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

# 写数据库
try:
    # sql语句执行
    # 插入操作
    # name = input('Name: ')
    # age = input('Age: ')
    # score = input('Score: ')
    # 注意sql语句中的字符串

    # 将变量插入到sql语句合成最终操作语句
    # sql = "insert into class_1(name,age,score) " \
    #       "values ('%s',%s,%s);"%(name, age,score)

    # sql = "insert into class_1(name,age,score) " \
    #       "values (%s,%s,%s);"
    # # 可以使用列表直接给sql的value传值
    # cur.execute(sql,[name,age,score])   #执行

    # # 修改操作
    # sql = "update interest set price=11800 where name='Abby'"
    # cur.execute(sql)

    # 删除操作
    sql = "delete from class_1 where score<80;"
    cur.execute(sql)

    db.commit() # 提交
except Exception as e:
    db.rollback() # 退回到commit执行之前的数据库状态
    print(e)

# 关闭数据库
cur.close()
db.close()
