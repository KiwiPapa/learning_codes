from PyQt5.Qt import *
import sys

class myWindow(QWidget):
    def __init__(self):
        super().__init__()

        l1=QLabel(self)
        l1.resize(20,30)
        l1.setText("标签标签标签标签")
        l1.move(100,50)
        #l1.setHidden(True)
        l1.hide()

        le = QLineEdit(self)
        le.setText("")
        le.move(100, 100)

        btn = QPushButton(self)
        btn.setText("登录")
        btn.move(100, 150)
        btn.setEnabled(False)

        def label_show():

            if(le.text()=="123456"):
                l1.setText("登录成功！")
                l1.adjustSize()
                l1.show()
            else:
                l1.setText("登录失败！")
                l1.adjustSize()
                l1.show()
        btn.pressed.connect(label_show)
        def text_cao():
            # if(len(le.text())>0):
            #     btn.setEnabled(True)
        #可以写得更加简洁点
            btn.setEnabled(len(le.text())>0)
        le.textChanged.connect(text_cao)

app=QApplication(sys.argv)
window=myWindow()
window.setWindowTitle("ddd")
window.resize(500,500)
window.move(300,0)

window.show()
sys.exit(app.exec_())
