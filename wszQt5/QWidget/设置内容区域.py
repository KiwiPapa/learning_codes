# -*- coding: utf-8 -*-
# @Time : 2019/8/6
# @Author : xcy
# @File : 设置内容区域.py
#@功能: 如题
#@核心代码: setContentsMargins(左边的间隔，上边的间隔，右边的间隔，下边的间隔
#           getContensMargrins()返回一个元组
#
#

from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("")
window.resize(500,500)
window.move(300,0)

l1=QLabel(window)
l1.setText("君子固穷，畏德畏心")
l1.resize(300,200)
#测试不同的数据

#l1.setContentsMargins(0,0,0,0)  #这行字显示在最中间的那一行
#l1.setContentsMargins(100,0,0,0)#这行字现在有了居中的效果
l1.setContentsMargins(100,100,50,50) #往右下角偏了。
l1.setStyleSheet("background-color: green;")
window.show()
sys.exit(app.exec_())