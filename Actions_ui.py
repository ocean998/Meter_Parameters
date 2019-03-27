# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Actions_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import os
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 604)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 90, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 90, 90, 23))
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 220, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 90, 491, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(280, 140, 401, 91))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 120, 71, 16))
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 210, 90, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 130, 90, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 260, 351, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 260, 391, 301))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_3.clicked.connect(self.open_picture2)
        self.pushButton_5.clicked.connect(self.open_picture)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "启动机器人"))
        self.pushButton_2.setText(_translate("MainWindow", "发送消息"))
        self.pushButton_3.setText(_translate("MainWindow", "打开到praphic"))
        self.lineEdit.setText(_translate("MainWindow", "水电费"))
        self.label.setText(_translate("MainWindow", "接收的消息"))
        self.pushButton_5.setText(_translate("MainWindow", "打开到Label"))
        self.pushButton_6.setText(_translate("MainWindow", "关闭机器人"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))

    def open_picture( self ):
        file = os.path.abspath(os.path.dirname(__file__))
        file = file + '\\190327-093024.png'
        self.show_picture(file)
    def show_picture( self, fn='None' ):
        if fn != 'None':
            print('Label_2:', fn)
            print('size:', QtGui.QPixmap(fn).height(), QtGui.QPixmap(fn).width())
            jpg = QtGui.QPixmap(fn).scaled(
                self.label.width(), self.label.height())

            # self.label_2.setPixmap(jpg)
            image = QtGui.QImage(fn)

            print('image size:',image.size())
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))


            self.label_2.setScaledContents(True)
            print('size:', QtGui.QPixmap(fn).height(), QtGui.QPixmap(fn).width())

            print(jpg)

    def open_picture2( self ):
        file = os.path.abspath(os.path.dirname(__file__))
        file = file + '\\190327-093024.png'
        print('file:',file)
        self.show_picture2(file)
    def show_picture2( self, fn='None' ):
        print('show_picture2:',fn)
        if fn != 'None':
            im = Image.open( fn )
            print( im.size )
            scene = QtWidgets.QGraphicsScene(  )
            print( im.size )

            image = QtGui.QImage(fn)
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))



            print( im.size )
            print('*'*20)
            item = QtWidgets.QGraphicsPixmapItem( pixmap )
            print( im.size )
            scene.addItem( item )
            print( im.size )
            self.graphicsView.setScene( scene )
            self.graphicsView.show()
            print( fn )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
