from tkinter import *

from shellcmd import shellcmd


class AboutFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        Label(self, text='runinfo').pack()
        Label(self, text='test').pack()

        def callback():
            shellcmd.cmd('reboot')
            print("click me!")

        # 使用按钮控件调用函数
        Button(self, text="点击执行回调函数", command=callback).pack()
