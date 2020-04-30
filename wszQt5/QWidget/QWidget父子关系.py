from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("父子关系学习")
window.resize(500,500)
window.move(300,0)

#写3个标签控件
# l1=QLabel(window)
# l1.setText("标签1")
# l2=QLabel(window)
# l2.setText("标签2")
# l2.move(50,50)
# l3=QLabel(window)
# l3.setText("标签3")
# l3.move(100,100)
#
# #看一下(55,55)对应的位置有没有字控件
# print(window.childAt(55, 55))
# print(window.childAt(255, 255))
#
# #parentWidget查看父控件
# print(l2.parentWidget())
# #查看子控件矩形

#层级关系调整
#如果两个标签处在window同一位置的话，那必然只能显示一个标签，下面代码显示的是L2
#当然可以自己来设置哪个标签显示，那个不显示
#l2.lower()或者l1.raise(), a.stackUnder(b),让a放在b下面
l1=QLabel(window)
l1.setText("标签1")
l1.resize(200,200)
l1.setStyleSheet("background-color:green;")
l2=QLabel(window)
l2.setText("标签2")
l2.resize(200,200)
l2.move(100,100)
l2.setStyleSheet("background-color:red;")
# l2.lower()
# l1.raise_()
l2.stackUnder(l1)
print(window.childrenRect())
window.show()
sys.exit(app.exec_())
s