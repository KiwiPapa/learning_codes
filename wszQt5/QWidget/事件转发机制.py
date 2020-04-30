# -*- coding: utf-8 -*-
# @Time : 2019/8/6
# @Author : xcy
# @File : 事件转发机制.py
#@功能: 如果事件指向的对象（控件）处理了这个事件，那就没什么好说的。如果不能处理这个事件，那么父对象就要负责处理这个事件，
#       是父对象而不是父类，这点要明确
#       事件对象具有两个属性 accept和ignore，前者表示事件已经处理好了，后者表示不处理这个事件，继续向父对象传递这个事件
#@核心代码:
#

from PyQt5.Qt import *
import sys


class Window(QWidget):
    def mousePressEvent(self,QMouseEvent):
        print("顶层窗口鼠标按下") #写了这个函数后就默认这个事件已经得到了处理
        print(QMouseEvent.isAccepted())  #这个isAccepted()函数来查看事件是否得到了处理
        print(dir(QMouseEvent))   #发现并没有 isIgnored()函数，哈哈
        
class MidWindow(QWidget):
    def mousePressEvent(self, QMouseEvent):
        print("中层窗口鼠标按下")

class Label(QLabel):
    def mousePressEvent(self, QMouseEvent):
        print("标签鼠标按下")
        QMouseEvent.ignore()



app=QApplication(sys.argv)
window=Window()
window.setWindowTitle("事件传递机制")
window.resize(500,500)
window.move(300,0)

midWindow=MidWindow(window)
midWindow.resize(300,300)
midWindow.setAttribute(Qt.WA_StyledBackground,True)
midWindow.setStyleSheet("background-color:green;")

l1=Label(midWindow)
l1.setText("我是标签")
l1.setStyleSheet("background-color:red;")
l1.move(100,100)

btn=QPushButton(midWindow)
btn.setText("我是按钮")
btn.setStyleSheet("background-color:red;")
btn.move(50,50)

window.show()
sys.exit(app.exec_())