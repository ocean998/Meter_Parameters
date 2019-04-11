
# -*- coding: utf-8 -*-
import analyze_pic as ap
import os


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox

import Meter_Parameter as ui
import w_Chart as wc


class Meter_Para(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Meter_Para, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.logout)
        self.pushButton_7.clicked.connect(self.help_msg)
        self.pushButton_6.clicked.connect(self.clear_rst)
        self.pushButton_2.clicked.connect(self.open_real)
        self.pushButton.clicked.connect(self.open_mds)
        self.pushButton_5.clicked.connect(self.get_para)
        # 微信接收到消息后的槽函数
        self.signal_slot()
        self.real_pic = ''
        self.mds_pic = ''

    def open_real(self):
        imgName, imgType = QFileDialog.getOpenFileName(
            self, "打开实物图片", "", "*.jpg;;*.png;;All Files(*)")

        self.show_picture(self.label, imgName)
        msg = '打开实物图片:' + imgName
        self.statusbar.showMessage(msg)

    def open_mds(self):
        imgName, imgType = QFileDialog.getOpenFileName(
            self, "打开MDS图片", "", "*.jpg;;*.png;;All Files(*)")
        self.show_picture(self.label_4, imgName)
        msg = '打开MDS图片' + imgName
        self.statusbar.showMessage(msg)

    def login(self):
        try:
            wc.login_wchat()
        except Exception as e:
            self.statusbar.showMessage('微信打开失败！')
        else:
            name = '微信（网页版）' + wc.get_name() + ' 已登录，请用手机微信的文件助手发送图片进行比对'
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
        send.sendmsg.connect(self.get_pic)

    def get_pic(self, msg1, msg2):
        print(msg1)
        print(msg2)
        if msg1 == 'Text':
            if msg2 == '1':
                self.label.setText('请发送实物图片！在此处显示')
                self.label_4.setText('    MDS 图片')
            if msg2 == '2':
                self.label_4.setText('请发送MDS图片！在此处显示')
                self.label.setText('    实物图片')

        if msg1 == 'Picture':
            if '发送实物图片' in self.label.text():
                self.show_picture(self.label, msg2)
                return
            if '发送MDS图片' in self.label_4.text():
                self.show_picture(self.label_4, msg2)
                return
            if self.label.pixmap() is None and self.label_4.pixmap() is None:
                self.show_picture(self.label, msg2)
            elif self.label_4.pixmap() is None:
                self.show_picture(self.label_4, msg2)
            else:
                self.show_picture(self.label, msg2)

    def clear_rst(self):
        if self.label.pixmap() is not None:
            self.label.setPixmap(QtGui.QPixmap(""))
        if self.label_4.pixmap() is not None:
            self.label_4.setPixmap(QtGui.QPixmap(""))
        self.label_4.setText('    MDS 图片')
        self.label.setText('    实物图片')
        self.mds_pic = ''
        self.real_pic = ''

    def show_picture(self, label, fn='None'):
        if label.text().find('实物') > 0 :
            self.real_pic = fn
        if label.text().find('MDS') > 0 :
            self.mds_pic = fn
        if fn != 'None' and label is not None:
            jpg = QtGui.QPixmap(fn).scaled(
                label.width(), label.height())
            label.setPixmap(jpg)


    def show_para( self, pic='real' , para={}):

        if pic == 'real':
            for x in para:
                if x == '生产厂家':
                    self.lineEdit.setText(para[x])
                if x == '条形码':
                    self.lineEdit_2.setText(para[x])
                if x == '类型':
                    self.lineEdit_3.setText(para[x])
                if x == '电流':
                    self.lineEdit_4.setText(para[x])
                if x == '电压':
                    self.lineEdit_5.setText(para[x])
                if x == '精度':
                    self.lineEdit_17.setText(para[x])
                if x == '有功常数':
                    self.lineEdit_6.setText(para[x])
                if x == '无功常数':
                    self.lineEdit_7.setText(para[x])
                if x == '年份':
                    self.lineEdit_8.setText(para[x])

        if pic == 'mds':
            for x in para:
                if x == '生产厂家':
                    self.lineEdit_9.setText(para[x])
                if x == '条形码':
                    self.lineEdit_10.setText(para[x])
                if x == '类型':
                    self.lineEdit_11.setText(para[x])
                if x == '电流':
                    self.lineEdit_12.setText(para[x])
                if x == '电压':
                    self.lineEdit_13.setText(para[x])
                if x == '有功常数':
                    self.lineEdit_14.setText(para[x])
                if x == '精度':
                    self.lineEdit_18.setText(para[x])
                if x == '无功常数':
                    self.lineEdit_15.setText(para[x])
                if x == '年份':
                    self.lineEdit_16.setText(para[x])




    def get_para( self ):
        if len(self.real_pic) < 3:
            QMessageBox.question(self, '电能表参数比对说明', '请先打开或拍摄电能表实物图片！',
                                 QMessageBox.Yes)
            return
        if len(self.mds_pic) < 3:
            QMessageBox.question(self, '电能表参数比对说明', '请先打开或拍摄电能表MDS系统参数图片！',
                                 QMessageBox.Yes)
            return
        ans = ap.analyze_pic(self.real_pic)
        real = ap.get_para(ans)
        self.show_para('real', real)

        ans = ap.analyze_pic(self.mds_pic)
        mds = ap.get_para(ans)
        self.show_para('mds', mds)
        para = ['条形码', '类型', '精度', '电压', '电流', '有功常数', '无功常数', '生产厂家', '年份']
        for x in para:
            s = x + ':\t' + real[x]
            self.textEdit.append(s)
            s = '      \t' + mds[x]
            self.textEdit.append(s)
    #  显示消息对话框
    def help_msg(self):
        msg = '向文件助手发送图片，自动获取图片中的参数信息完成比对。\n'
        msg = msg + '本程序只接收微信文件助手的消息，向文件助手发送图片前请先回复：\n'
        msg = msg + '回复1代表将要发送实物图片\n回复2代表将要发送MDS系统图片\n'
        msg = msg + '是否将简要提示发送到文件助手？\n'
        reply = QMessageBox.question(
            self,
            '电能表参数比对说明',
            msg,
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            if wc.bot is None:
                msg = '请先登录微信！'
                reply = QMessageBox.question(self, '电能表参数比对说明', msg,
                                             QMessageBox.Yes)
            else:
                wc.sent_msg('回复1代表将要发送实物图片\n回复2代表将要发送MDS系统图片')
                name = '微信（网页版）' + wc.get_name() + ' 已登录，回复1代表将要发送实物图片，\n回复2代表将要发送MDS系统图片。'
                self.statusbar.showMessage(name)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MP = Meter_Para()
    MP.show()
    sys.exit(app.exec_())
