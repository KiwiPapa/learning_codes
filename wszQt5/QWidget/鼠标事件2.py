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

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()==Qt.Key_Tab: #这是比较单个键盘按键的方法！！！
            print("按了Tab键")

        #接下来监听Ctrl+C
        #典型错误
        # if QKeyEvent.key() == Qt.ControlModifier and QKeyEvent.key()==Qt.Key_C:
        #     print("按了Ctrl+C")

        if QKeyEvent.modifiers()==Qt.ControlModifier and QKeyEvent.key()==Qt.Key_C:
            print("按了Ctrl+C")

        #谁来接受捕获这个键盘事件呢？？ ctrl+alt+c 多个修饰键使用或运算
        #或运算本来就是加法运算！
        if QKeyEvent.modifiers()==Qt.ControlModifier|Qt.AltModifier and QKeyEvent.key()==Qt.Key_C:
            print("按了Ctrl+Alt+C")
        #刚刚在按 ctrl+alt+a的时候被系统给拦截了，直接调用了截图！！！
        #想让标签来捕获事件
        #修饰键，就是ctrl和alt之类 tab不算是修饰键吗？
        #能打印出来的键都是普通键 tab
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("")
window.resize(500,500)
window.move(300,0)

l1=MyLabel(window)
l1.resize(200,200)
l1.move(100,100)
l1.setStyleSheet("background:cyan;")
#捕获键盘
l1.grabKeyboard()

#重写相关事件的方法
#还是继承。
window.show()
sys.exit(app.exec_())
