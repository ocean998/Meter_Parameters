from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget

import Meter_Parameter as ui


class Meter_Para(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__( self, parent = None ):
        super(Meter_Para, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.openfile)

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self, 'Open file', './')
        print(openfile_name)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MP = Meter_Para( )
    MP.show()
    sys.exit(app.exec_())
