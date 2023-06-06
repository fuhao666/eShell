from tkinter import *
from tkinter.messagebox import *

import requests
from request import Request
import traceback
from shellcmd import shellcmd
import socket
import select
import threading
import os,sys
import datetime
from time import sleep


class startserver():
    def __init__(self, master=None):
        self.setTime()
        self.start_client()
        self.start_self()

    def setTime(self):  # 设置linux时间
        try:
            shellcmd.cmd('timedatectl set-timezone Asia/Shanghai')
            json = {'url': 'http://ereport.yeestor.com/gettime/', 'myParams': ''}
            res = eval(Request.gets(json).text)
            times = datetime.datetime.fromtimestamp(res['time'])
            dt = times.strftime('%Y-%m-%d %H:%M:%S')
            shellcmd.cmd('timedatectl set-ntp  false')
            shellcmd.cmd('timedatectl set-time "%s"' % dt)
            shellcmd.cmd('timedatectl set-local-rtc 1')
        except:
            strtest = traceback.format_exc()
            print(strtest)

    def start_client(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('127.0.0.1', 8000))
            # 创建线程锁，防止主线程socket被close了，子线程还在recv而引发的异常
            socket_lock = threading.Lock()

            def read_thread_method():
                while True:
                    if not sock:  # 如果socket关闭，退出
                        break
                    # 使用select监听客户端（这里客户端需要不停接收服务端的数据，所以监听客户端）
                    # 第一个参数是要监听读事件列表，因为是客户端，我们只监听创建的一个socket就ok
                    # 第二个参数是要监听写事件列表，
                    # 第三个参数是要监听异常事件列表，
                    # 最后一个参数是监听超时时间，默认永不超时。如果设置了超时时间，过了超时时间线程就不会阻塞在select方法上，会继续向下执行
                    # 返回参数 分别对应监听到的读事件列表，写事件列表，异常事件列表
                    rs, _, _ = select.select([sock], [], [], 10)
                    for r in rs:  # 我们这里只监听读事件，所以只管读的返回句柄数组
                        socket_lock.acquire()  # 在读取之前先加锁，锁定socket对象（sock是主线程和子线程的共享资源，锁定了sock就能保证子线程在使用sock时，主线程无法对sock进行操作）

                        if not sock:  # 这里需要判断下，因为有可能在select后到加锁之间socket被关闭了
                            socket_lock.release()
                            break

                        data = r.recv(1024)  # 读数据，按自己的方式读

                        socket_lock.release()  # 读取完成之后解锁，释放资源

                        if not data:
                            print
                            'server close'
                        else:
                            print
                            data

            # 创建一个线程去读取数据
            read_thread = threading.Thread(target=read_thread_method)
            read_thread.setDaemon(True)
            read_thread.start()

            # 清理socket，同样道理，这里需要锁定和解锁
            socket_lock.acquire()
            sock.close()
            sock = None
            socket_lock.release()
        except:
            strtest = traceback.format_exc()
            print(strtest)

    def start_self(self):
        try:
            path = sys.path[0]
            f = open(path+'/eshell.desktop', "a")
            f.write('[Desktop Entry]'+'\n'+'Type=Application'+'\n'+'Exec=%s' % (path+'/dist/main'))
            f.close
            shellcmd.cmd('mv %s/eshell.desktop ~/.config/autostart/eshell.desktop' % path)
        except:
            strtest = traceback.format_exc()
            print(strtest)
