from PyQt5.Qt import *
import sys

class Label(QLabel):
    def mousePressEvent(self, QMouseEvent):
        self.raise_()

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("")
window.resize(500,500)
window.move(300,0)
l1=Label(window)
l1.setText("标签1")
l1.resize(200,200)
l1.setStyleSheet("background-color:green;")
l2=Label(window)
l2.setText("标签2")
l2.resize(200,200)
l2.move(100,100)
l2.setStyleSheet("background-color:red;")
# l2.lower()

window.show()
sys.exit(app.exec_())
