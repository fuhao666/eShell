from tkinter import *
import tkinter.messagebox
from startserver import startserver
from secondPage import AboutFrame

# 创建窗口：实例化一个窗口对象。
class mainPage:
    def __init__(self, master):
        self.root = master
        lenth = round(self.root.winfo_screenwidth()/2)
        hei = round(self.root.winfo_screenheight()/2)
        # 窗口大小
        self.root.title('eShell')
        self.root.geometry('%dx%d' % (lenth, hei))  # 设置窗口大小
        self.root.maxsize(lenth, hei)
        # 设置窗口被允许最小调整的范围，与resizble()冲突
        self.root.minsize(lenth, hei)
        button = Button(self.root, text="关闭", command=self.root.quit)
        # 将按钮放置在主窗口内
        button.pack(side="bottom")
        self.creatmenu()
        startserver()
        # 显示窗口

    def creatmenu(self):
        self.about_frame = AboutFrame(self.root)
        self.main_frame = Frame(self.root)
        Label(self.main_frame, text='abccdef').pack()
        Label(self.main_frame, text='testsssdsa').pack()
        main_menu = Menu(self.root)
        main_menu.add_command(label="主页", command=self.show_main)
        main_menu.add_command(label="结束", )
        main_menu.add_command(label="关于", command=self.show_second)
        self.root['menu'] = main_menu
        self.show_main()

    def show_main(self):
        self.distory()
        self.about_frame.pack()

    def show_second(self):
        self.distory()
        self.main_frame.pack()

    def distory(self):
        self.main_frame.pack_forget()
        self.about_frame.pack_forget()


if __name__ == '__main__':
    root = Tk()
    mainPage(root)
    root.mainloop()
