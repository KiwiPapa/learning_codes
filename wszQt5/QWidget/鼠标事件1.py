# -*- coding: utf-8 -*-
# @Time : 2019/8/6
# @Author : xcy
# @File : 鼠标事件1.py
#@功能: 
#@核心代码:
#
#
#

from PyQt5.Qt import *
import sys

class MyLabel(QLabel):
    def enterEvent(self, *args, **kwargs):
        print("鼠标进来")
        self.setText("欢迎光临")

    def leaveEvent(self, *args, **kwargs):
        self.setText("谢谢惠顾")
        print("鼠标出去")

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("")
window.resize(500,500)
window.move(300,0)

l1=MyLabel(window)
l1.resize(200,200)
l1.move(100,100)
l1.setStyleSheet("background:cyan;")

#重写相关事件的方法
#还是继承。
window.show()
sys.exit(app.exec_())
