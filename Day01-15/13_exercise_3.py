# -*- coding: utf-8 -*-
"""
Python进程间内存是分开的，要想共享数据，要使用进程间通信的方式
"""
from multiprocessing import Process
from os import getpid
from time import sleep

counter = 0


def sub_task(string, ):
    global counter
    print('进程id:%d' % getpid())
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)


def main():
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()


if __name__ == '__main__':
    main()
