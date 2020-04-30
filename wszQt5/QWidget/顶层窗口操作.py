from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("窗口")

#设置图标
icon=QIcon("images/c7.png")  #需要提供文件路径
window.setWindowIcon(icon)

#不透明度
window.setWindowOpacity(0.5)
print(window.windowOpacity())
window.resize(500,500)
window.move(300,0)


window.show()
sys.exit(app.exec_())
