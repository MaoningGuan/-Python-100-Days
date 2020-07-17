# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
import threading
from threading import Thread
import os
from django.http import FileResponse
import errno

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'

body = '''Hello, world! <h1> from the5fire 《Django企业开发实战》</h1> - from {thread_name}'''
response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun, 07 June 2020 19:08:00 GMT',
    'Content-Type: text/html; charset=utf-8',
    'Content-Length: {length}\r\n',
    body,
]
response = '\r\n'.join(response_params)

# 获取文件的名字
SAVED_FILES_DIR = r'D:\2018级计算机与软件学院开题报告电子版2'  # 合并后保存的路径
files = []
all_files_name = os.listdir(SAVED_FILES_DIR)  # 读取文件夹下的所有文件名
for file_name in all_files_name:
    if file_name.endswith('.pdf'):  # 判断是否为PDF文件名
        student_number = file_name.strip('.pdf')

        file = {
            'number': student_number,
            'file_name': file_name,
        }
        files.append(file)


# 自定义线程类
class FileTransferHandler(Thread):
    def __init__(self, cclient, filename):
        super().__init__()
        self.cclient = cclient
        self.filename = filename

    def run(self):
        file_pathname = os.path.join(SAVED_FILES_DIR, self.filename)
        print(file_pathname)
        file_response = {}
        with open(file_pathname, 'rb') as f:
            file_response['body'] = b64encode(f.read()).decode('utf-8')
            file_response['Content-Type'] = 'application/octet-stream'
            file_response['Content-Disposition'] = 'attachment;filename=' + self.filename
            file_response['Content-Length'] = os.path.getsize(file_pathname)

        # 通过dumps函数将字典处理成JSON字符串
        json_str = dumps(file_response)
        # 发送JSON字符串
        self.cclient.send(json_str.encode('utf-8'))
        self.cclient.close()


class HandleConnection(Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        print('oh, new conn', self.conn, self.addr)
        length = len(threading.enumerate())  # 枚举返回个列表
        print('当前运行的线程数为：%d' % length)
        # time.sleep(60)
        request = b""
        while EOL1 not in request and EOL2 not in request:
            try:
                request += self.conn.recv(1024)
            except socket.error as e:
                if e.args[0] != errno.EWOULDBLOCK:
                    raise
                continue

        print(request)
        file_name = '1800271038-关茂柠.pdf'
        FileTransferHandler(self.conn, file_name).start()
        # current_thread = threading.currentThread()
        # current_length = len(body.format(thread_name=current_thread.name).encode())
        # data = response.format(thread_name=current_thread.name, length=current_length)
        # print(data)
        # self.conn.send(data.encode())  # response转为bytes后传输
        # self.conn.close()
        # print('---------------------------------------------')

def handle_connection(conn, addr):
    print('oh, new conn', conn, addr)
    length = len(threading.enumerate())  # 枚举返回个列表
    print('当前运行的线程数为：%d' % length)
    # time.sleep(60)
    request = b""
    while EOL1 not in request and EOL2 not in request:
        try:
            request += conn.recv(1024)
        except socket.error as e:
            if e.args[0] != errno.EWOULDBLOCK:
                raise
            continue

    print(request)
    current_thread = threading.currentThread()
    current_length = len(body.format(thread_name=current_thread.name).encode())
    # length = len(threading.enumerate())  # 枚举返回个列表
    # print('当前运行的线程数为：%d' % length)
    # print(current_thread.name)
    # print(response.format(thread_name=current_thread.name, length=current_length).encode())
    data = response.format(thread_name=current_thread.name, length=current_length)
    conn.send(data.encode())  # response转为bytes后传输
    conn.close()


def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    # socket.AF_INET 用于服务器与服务器之间的网络通信
    # socket.SOCK_STREAM 用于基于TCP的流式socket通信
    server = socket(AF_INET, SOCK_STREAM)
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind(('172.31.73.103', 8888))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(10)
    print('服务器启动开始监听...')
    try:
        while True:
            try:
                conn, addr = server.accept()
            except socket.error as e:
                # print(e.args[0])
                # print(errno.EWOULDBLOCK)
                if e.args[0] != errno.EWOULDBLOCK:
                    raise
                continue

            # 启动一个线程来处理客户端的请求
            # handle_connection(conn, addr)
            HandleConnection(conn, addr).start()
    finally:
        server.close()


if __name__ == '__main__':
    main()
