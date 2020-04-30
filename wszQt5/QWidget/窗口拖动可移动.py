from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)

#这是个计算问题，该怎么计算呢
#确定鼠标的坐标和窗口的左上坐标，要确定拖拽向量
#新的窗口位置就是 窗口坐标点+向量，要注意的是窗口坐标点也是实时更新的，脑瘫理解！
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.flag=False

    def mousePressEvent(self, QMouseEvent):
        self.flag=True
        self.mouseX=QMouseEvent.globalX()
        self.mouseY=QMouseEvent.globalY()
        self.originX=self.x()
        self.originY=self.y()

    def mouseMoveEvent(self, QMouseEvent):
        #计算移动向量
        #还别说整得挺好
        print(self.flag)

        if self.flag:
            moveX=QMouseEvent.globalX()-self.mouseX
            moveY=QMouseEvent.globalY()-self.mouseY
            destX=self.originX+moveX
            destY=self.originY+moveY
            self.move(destX,destY)

    def mouseReleaseEvent(self, QMouseEvent):
        self.flag=False #把这条语句注销了也挺好玩的。


    #在做鼠标跟踪的方法
window=Window()
window.setWindowTitle("")
window.resize(500,500)
window.move(300,0)
window.setMouseTracking(True)

window.show()
sys.exit(app.exec_())
