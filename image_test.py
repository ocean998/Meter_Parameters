from PyQt5 import QtWidgets  ,QtGui
from PyQt5.QtWidgets import QFileDialog
from PIL import Image
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.image=None
    def openimage(self):
   # 打开文件路径
   #设置文件扩展名过滤,注意用双分号间隔
        imgName,imgType= QFileDialog.getOpenFileName(self,
                                    "打开图片",
                                    "",
                                    " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        print(imgName)
        im=Image.open(imgName)
        self.image=imgName
        print(im.size)
        scene=QtWidgets.QGraphicsScene(self)
        pixmap=QtGui.QPixmap(imgName)
        #.scaled(im.size[1], im.size[1])
        item=QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)

        #png = QtGui.QPixmap(imgName).scaled(im.size[1], im.size[1])
        #self.graphicsView.scale(im.size[1], im.size[1])
        self.graphicsView.setScene(scene)
        #利用graphicsView显示图片

    def processing(self):
        print(self.image)
        scene=QtWidgets.QGraphicsScene(self)
        pixmap=QtGui.QPixmap(self.image)
        #.scaled(im.size[1], im.size[1])
        item=QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)

        #png = QtGui.QPixmap(imgName).scaled(im.size[1], im.size[1])
        #self.graphicsView.scale(im.size[1], im.size[1])
        self.graphicsView_2.setScene(scene)
        #利用graphicsView显示图片

if __name__=="__main__":
    import sys

    app=QtWidgets.QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())