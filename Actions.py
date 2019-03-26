# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Actions.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import w_Chart as wc


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
        self.pushButton.clicked.connect(self.login)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 90, 90, 23))
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.sent_text)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 210, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 40, 90, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 130, 90, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.logout)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 90, 491, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(280, 140, 401, 91))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 120, 70, 12))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 310, 731, 271))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.signal_slot()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "启动机器人"))
        self.pushButton_2.setText(_translate("MainWindow", "发送消息"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "接收的消息"))
        self.label_2.setText(_translate("MainWindow", "接收的图片"))
        self.pushButton_4.setText(_translate("MainWindow", "模拟发送"))
        self.pushButton_6.setText(_translate("MainWindow", "关闭机器人"))

    def login(self):
        wc.login_wchat()

    def logout(self):
        wc.logout_wchat()

    def sent_text(self):
        print(self.lineEdit.text())
        wc.sent_msg(self.lineEdit.text())

    def get(self, msg1, msg2):
        print("QSlot get msg => " + msg1 + ' ' + msg2)
        self.textEdit.append(msg1)
        self.textEdit.append(msg2)
        print('get', msg2)
        self.show_picture(msg2)

    def signal_slot(self):
        send = wc.signal
        print('--- 把信号绑定到槽函数 ---')
        send.sendmsg.connect(self.get)

    def show_picture(self, fn='None'):
        if fn != 'None':
            # self.image = QImage(fn)
            # self.imageView.setPixmap(QPixmap.fromImage(self.image))
            # self.resize(self.image.width(), self.image.height())
            # self.label_2.setPicture(QPixmap.fromImage(self.image))

            jpg = QtGui.QPixmap(fn).scaled(
                self.label_2.width(), self.label_2.height())
            self.label_2.setPixmap(jpg)

            # imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
            # jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
            # self.label.setPixmap(jpg)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
