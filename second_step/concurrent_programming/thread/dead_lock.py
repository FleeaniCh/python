"""

"""
from threading import Thread,Lock
from time import sleep

class Account:
    def __init__(self,_id,balance,lock):
        self.id = _id
        self.balance = balance
        self.lock = lock

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

Tom = Account('Tom',5000,Lock())
Alex = Account('Alex',8000,Lock())

# 转账过程
def transfer(from_,to,amount):
    if from_.lock.acquire():    # 锁住自己的账户
        from_.withdraw(amount)  # 账户减少
        sleep(0.5)
        if to.lock.acquire():   # 对方账户上锁
            to.deposit(amount)  # to账户加钱
            to.lock.release()   # to账户解锁
        from_.lock.release()    # from_账户解锁
    print("%s给%s转账%d"%(from_.id,to.id,amount))

# transfer(Tom,Alex,4000)
t1 = Thread(target=transfer,args=(Tom,Alex,2000))
t2 = Thread(target=transfer,args=(Alex,Tom,3500))
t1.start()
t2.start()
t1.join()
t2.join()