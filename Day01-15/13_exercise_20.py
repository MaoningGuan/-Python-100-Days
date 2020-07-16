# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Python进程间内存是分开的，要想共享数据，要使用进程间通信的方式
"""
from multiprocessing import Process, Queue
from os import getpid
from time import sleep


def sub_task(string, queue):
    print('进程id:%d' % getpid())
    counter = queue.get()
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        queue.put(counter)
        sleep(0.01)
        try:
            counter = queue.get(timeout=1)
        except:
            break



def main():
    counter = 0
    queue = Queue()
    queue.put(counter)
    Process(target=sub_task, args=('Ping',queue)).start()
    Process(target=sub_task, args=('Pong',queue)).start()


if __name__ == '__main__':
    main()
