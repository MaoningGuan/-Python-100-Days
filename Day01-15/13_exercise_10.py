# -*- coding: utf-8 -*-
from time import sleep, time
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        sleep(2)
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟受理存款业务需要0.01秒的时间
            sleep(0.01)
            # 修改账户余额
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []

    start = time()
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(5):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    end = time()
    print('账户余额为: ￥%d元，花费的时间为%.3f' % (account.balance, end - start))


if __name__ == '__main__':
    main()

# 账户余额为: ￥5元，花费的时间为2.056