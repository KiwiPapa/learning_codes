# -*- coding: utf-8 -*-
# @Time : ${DATE} ${TIME}
# @Author : xcy
# @File : ${NAME}.py
#@功能  调整窗口的大小，或者限定窗口大小，再或者将窗口大小限定在一个范围内
#
#@核心代码: setFixedSize() setMaximumSize() setMinimumSiz()
#


from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)
window=QWidget()

window.setWindowTitle("")

#可以通过鼠标来调整大小
window.resize(500,500)
# 不给你调整大小，直接固定死了
window.setFixedSize(500,500)

#重点来了，给了鼠标能调整的范围
#有点无聊
window.setMaximumSize(1000,1000)
window.setMinimumSize(400,400)
window.move(300,0)
window.show()
sys.exit(app.exec_())