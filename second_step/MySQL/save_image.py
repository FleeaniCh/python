"""
    save_image.py
    二进制文件存储
"""
import pymysql

db = pymysql.connect(host='192.168.214.139',
                     port=3306,
                     user='root',
                     password='root',
                     database='stu')

# 获取游标(操作数据库，执行sql语句)
cur = db.cursor()


# # 存储图片
# with open('wxj.jpg','rb') as f:
#     data = f.read()
# try:
#     sql = "update class_1 set image=%s where name='Jame';"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 获取图片
sql = "select image from class_1  where name='Jame'"
cur.execute(sql)
data = cur.fetchone()
with open('scen.jpg','wb') as f:
    f.write(data[0])

#  关闭数据库
cur.close()
db.close()