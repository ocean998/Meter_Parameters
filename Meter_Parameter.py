# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog




class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        # self.retranslateUi( self )

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("电表参数比对")
        MainWindow.resize(1061, 768)
        MainWindow.setStatusTip("电表参数比对")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 1021, 161))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 871, 81))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_3.setIndent(5)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 0, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 0, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 0, 7, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 0, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 0, 4, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 0, 6, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 0, 8, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 1, 3, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_4.addWidget(self.lineEdit_4, 1, 4, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_4.addWidget(self.lineEdit_5, 1, 5, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_4.addWidget(self.lineEdit_6, 1, 6, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_4.addWidget(self.lineEdit_7, 1, 7, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_4.addWidget(self.lineEdit_8, 1, 8, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_4.addWidget(self.lineEdit_9, 2, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_4.addWidget(self.lineEdit_10, 2, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_4.addWidget(self.lineEdit_11, 2, 3, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_4.addWidget(self.lineEdit_12, 2, 4, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_4.addWidget(self.lineEdit_13, 2, 5, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_4.addWidget(self.lineEdit_14, 2, 6, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_4.addWidget(self.lineEdit_15, 2, 7, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_4.addWidget(self.lineEdit_16, 2, 8, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(890, 50, 90, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openfile)

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(890, 80, 90, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 511, 491))
        self.groupBox_2.setObjectName("groupBox_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView.setGeometry(QtCore.QRect(0, 20, 501, 461))
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(530, 180, 511, 491))
        self.groupBox_3.setObjectName("groupBox_3")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 20, 501, 461))
        self.graphicsView_2.setObjectName("graphicsView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openfile(self):
        # filename = QFileDialog.getOpenFileName(self, 'Open file', './')
        # print(filename)


        filename = QFileDialog.getOpenFileName( self, 'Open file', './' )
        print( filename )



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "电表参数比对"))
        self.groupBox.setTitle(_translate("MainWindow", "参数比对项目"))
        self.label_3.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">MDS 参数 </span></p></body></html>"))
        self.label_2.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">实物参数 </span></p></body></html>"))
        self.label_18.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">生产厂家：</span></p></body></html>"))
        self.label_20.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">类型：</span></p></body></html>"))
        self.label_25.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">资产条形码：</span></p></body></html>"))
        self.label_22.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">无功常数：</span></p></body></html>"))
        self.label_21.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">电压：</span></p></body></html>"))
        self.label_19.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">电流：</span></p></body></html>"))
        self.label_23.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">有功常数：</span></p></body></html>"))
        self.label_26.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">年份：</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "打开实物图片"))
        self.pushButton_2.setText(_translate("MainWindow", "打开MDS图片"))
        self.groupBox_2.setTitle(_translate("MainWindow", "实物图片"))
        self.groupBox_3.setTitle(_translate("MainWindow", "MDS图片"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_2.clicked.connect(ui.openfile)
    MainWindow.show()
    sys.exit(app.exec_())
