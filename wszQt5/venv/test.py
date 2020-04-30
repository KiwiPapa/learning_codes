from PyQt5.Qt import *
import sys

from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)


w = QWidget()
w.setWindowTitle('Hello world')
w.resize(500, 500)
w.move(400, 200)

w.show()
sys.exit(app.exec_())