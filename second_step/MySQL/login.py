import pymysql

# 连接数据库
db = pymysql.connect(host='192.168.214.139',
                     port=3306,
                     user='root',
                     password='root',
                     database='stu')

# 获取游标，操作数据库
cur = db.cursor()

# 1. 创建user表
# sql  = "create table user(id int primary key auto_increment,\
#        name char(10) not null,\
#        passwrod char(10) not null)"
# cur.execute(sql)

def read_data():
    # 获取表中数据
    sql = "select name,password from user;"
    cur.execute(sql)
    users = cur.fetchall()
    # print(users)
    return users

def write_data(name,password):
    # 写入注册数据
    sql = "insert into user(name,password) values (%s,%s);"
    try:
        cur.execute(sql,[name,password])
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)

if __name__ == '__main__':
    while True:
        print("--------1.Register---------")
        print("--------2.Login---------")

        num = input("Please input your choice(1 or 2): ")

        if num == '1':
            while True:
                # 注册
                name = input("Name:　")
                password = input("Password:　")
                for item in read_data():
                    if name == item[0]:
                        print("Sorry,the username is existed,please try again.")
                        continue
                else:
                    write_data(name,password)
        elif num == '2':
            # 登录
            while True:
                name = input("Name:　")
                password = input("Password:　")
                if (name, password) not in read_data():
                    print("Try again!")
                    continue
                print("Login success!")
                break


# # 关闭数据库
# cur.close()
# db.close()