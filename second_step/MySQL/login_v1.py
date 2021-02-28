import pymysql

# 连接数据库
db = pymysql.connect(host='192.168.214.139',
                     port=3306,
                     user='root',
                     password='root',
                     database='stu')
# 创建游标
cur = db.cursor()

def register():
    # 注册
    name = input("Name: ")
    password = input("Password: ")
    # 判断注册的用户是否已存在
    sql = "select * from user where name='%s'"%name
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False
    else:
        try:
            # 判断用户名密码是否正确
            sql = "insert into user(name,password) values(%s,%s)"
            cur.execute(sql,[name,password])
            db.commit()
            return True
        except:
            db.rollback()
            return False

def login():
    # 登录
    name = input("Name: ")
    password = input("Password: ")
    sql = "select * from user where name=%s and password=%s"
    cur.execute(sql,[name,password])
    result = cur.fetchone()
    if result:
        return True
    else:
        return False

while True:
    msg = """
    --------------
        1. Register
        2. Login
    --------------
    """
    print(msg)

    cmd = input("Please input your choice:　")

    if cmd == '1':
        if not register():
            print("Register fail !")
        else:
            print("Register success !")
    elif cmd == '2':
        if login():
            print("Login success !")
            break
        else:
            print("Login fail !")
    else:
        print("Input Error!")