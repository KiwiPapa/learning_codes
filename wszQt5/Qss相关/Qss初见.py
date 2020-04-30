
"""
如果想要单独应用标签1的样式而不是所有的标签样式，可以为l1单独设置对象名称
l1.setObjectName("")
ID选择器是 QLabel#L1 用到#号的语法

Qss与UI设计分离
更好的做法是单独设置一个类来做这件事情
"""

from PyQt5.Qt import *
from Tool import QSSTool
import sys


class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qss初见")
        self.resize(500, 500)
        self.move(300, 0)
        self.setupUI()

    def setupUI(self):
        box1=QWidget(self)
        box2=QWidget(self)

        #box1.setStyleSheet("background:orange;")#这个Qss影响了box1所有的控件！
        #如果要全局设置样式的话就得调用QApplication对象
        #app 则是包括所有的控件和子控件。。。
        #box2.setStyleSheet("background:cyan;")

        v_layout=QVBoxLayout()
        self.setLayout(v_layout)
        v_layout.addWidget(box1)
        v_layout.addWidget(box2)

        l1=QLabel("标签1",box1)
        l1.setObjectName("L1")
        l1.move(50,50)
        btn1=QPushButton("按钮1",box1)
        btn1.move(150,50)

        l2 = QLabel("标签2", box2)
        l2.move(50, 50)
        btn2 = QPushButton("按钮2", box2)
        btn2.setObjectName("Btn2")
        btn2.move(150, 50)
app=QApplication(sys.argv)

#这个写的不好！一点也不好！
# qss=QSSTool()
# qss.setQssToObj("test.qss",app)

QSSTool.setQssToObj("test.qss",app)
# with open("test.qss","r") as f:
#     content=f.read()
#     app.setStyleSheet(content)
window=myWindow()
window.show()
sys.exit(app.exec_())
