
# -*- coding: utf-8 -*-
import traceback
import os


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox

import Meter_Parameter as ui
import w_Chart as wc


class Meter_Para(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__( self, parent = None ):
        super(Meter_Para, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.logout)
        self.pushButton_7.clicked.connect(self.help_msg)
        self.pushButton_2.clicked.connect(self.open_real)
        self.pushButton.clicked.connect(self.open_mds)
        # 微信接收到消息后的槽函数
        self.signal_slot()

    def open_real(self):
        print(os.path.abspath(os.path.dirname(__file__)))
        imgName, imgType = QFileDialog.getOpenFileName(
            self, "打开实物图片", "", "*.jpg;;*.png;;All Files(*)")
        self.show_picture(self.label, imgName)
        self.statusbar.show('打开实物图片:'+imgName)

    def open_mds(self):
        print(os.path.abspath(os.path.dirname(__file__)))
        imgName, imgType = QFileDialog.getOpenFileName(
            self, "打开MDS图片", "", "*.jpg;;*.png;;All Files(*)")
        self.show_picture(self.label_4, imgName)
        self.statusbar.show('打开MDS图片:' + imgName)

    def login(self):
        try:
            wc.login_wchat()
        except Exception as e:
            self.statusbar.showMessage('微信打开失败！')
        else:
            name =  '微信（网页版）'+ wc.get_name()+ ' 已登录，请用手机微信的文件助手发送图片进行比对'
            print(name)
            self.statusbar.showMessage(name)
            self.sent_text()

    def logout(self):

        name = '微信（网页版）' + wc.get_name() + ' 已退出'
        wc.logout_wchat()
        self.statusbar.showMessage(name)


    def sent_text(self):
        wc.sent_msg('请回复1或2然后发送图片')



    def signal_slot(self):
        send = wc.signal
        send.sendmsg.connect(self.get)

    def get(self, msg1, msg2):
        if msg1 == 'Text':
            if msg2 == '1':
                self.label.setText('请发送实物图片！在此处显示')
                self.label_4.setText('    MDS 图片')
            if msg2 == '2':
                self.label_4.setText('请发送MDS图片！在此处显示')
                self.label.setText('    实物图片')

        if msg1 == 'Picture':
            if self.label.text == '请发送实物图片！在此处显示':
                self.show_picture(self.label,msg2)
            if self.label_4.text == '请发送MDS图片！在此处显示':
                self.show_picture(self.label_4,msg2)

    def show_picture(self, label, fn='None'):
        if fn != 'None' :
                jpg = QtGui.QPixmap(fn).scaled(
                    label.width(), label.height())
                label.setPixmap(jpg)

    #  显示消息对话框
    def help_msg( self ):
        msg = '向文件助手发送图片，自动获取图片中的参数信息完成比对。\n'
        msg = msg + '本程序只接收微信文件助手的消息，向文件助手发送图片前请先回复：\n'
        msg = msg + '回复1代表将要发送实物图片\n回复2代表将要发送MDS系统图片\n'
        msg = msg + '是否将简要提示发送到文件助手？\n'
        reply = QMessageBox.question(self, '电能表参数比对说明', msg,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            if wc.bot is None:
                msg = '请先登录微信！'
                reply = QMessageBox.question(self, '电能表参数比对说明', msg,
                                             QMessageBox.Yes  )
            else:
                wc.sent_msg('回复1代表将要发送实物图片\n回复2代表将要发送MDS系统图片')
                name = '微信（网页版）' + wc.get_name() + ' 已登录，回复1代表将要发送实物图片，\n回复2代表将要发送MDS系统图片。'
                self.statusbar.showMessage(name)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MP = Meter_Para( )
    MP.show()
    sys.exit(app.exec_())
