#encoding: utf-8
"""
@project = FtpTools
@file = gui
@function = 
@author = Cindy
@create_time = 2018/6/19 9:18
@python_version = 3.x
"""
from tkinter import *
import easygui
from run_func import RunFunc
import os


class MyFrame:

    def __init__(self):
        # 创建主窗口
        window = Tk()
        window.title('算量下载助手')
        window.geometry('200x300')  #窗口尺寸
        # 创建一个frame
        frm = Frame(window)
        frm.pack()
        # 在frame上创建左右两个frame
        frm_l = Frame(frm)
        frm_r = Frame(frm)
        frm_l.pack(side='left')
        frm_r.pack(side='right')
        # 创建产品下载按钮
        product_l = [('土建', 'TJ'),
                     ('安装', 'AZ'),
                     ('钢筋', 'GJ'),
                     ('下料', 'XL'),
                     ('场布', 'CB'), ]
        product_r = [('排布', 'PB'),
                     ('模架', 'MJ'),
                     ('万通Revit', 'Revit'),
                     ('万通Tekla', 'Tekla'),
                     ('万通Rhino', 'Rhino'), ]
        for k, v in product_l:
            self.btn = Button(frm_l, text=k, textvariable=v, width=10)
            self.btn.bind('<Button-1>', self.download)
            self.btn.bind('<Button-1>', self.download)
            self.btn.pack(padx=5, pady=5)

        for k, v in product_r:
            self.btn = Button(frm_r, text=k, textvariable=v, width=10)
            self.btn.bind('<Button-1>', self.download)
            self.btn.pack(padx=5, pady=5)

        # 创建设置按钮
        self.btn_setting = Button(window, text='修改配置文件', bg='yellow', width=23, command=self.setting)
        self.btn_setting.pack(pady=10)

        # 用法提示标签
        self.l_tips = Label(window,
                       text='点击上方的产品名称按钮即可从\nftp上下载最新版本并启动软件！',
                       fg='red',
                       width=30, height=3)
        self.l_tips.pack(side='bottom')
        window.mainloop()


    # 下载按钮点击事件
    def download(self, event):
        product = str(event.widget['textvariable'])
        print('下载"%s"中....' % product)
        RunFunc(product)

    # 设置按钮点击事件
    def setting(self):
        os.startfile('config.ini')

App = MyFrame()


