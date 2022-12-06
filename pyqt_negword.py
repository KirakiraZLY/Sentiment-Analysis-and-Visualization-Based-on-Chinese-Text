from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout,QTextBrowser
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from pyqt import *

class Neg_WordCloud(QtWidgets.QMainWindow):
    def __init__(self):
        super(Neg_WordCloud, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        w = QtWidgets.QWidget(self.centralwidget)
        w.setGeometry(0, 50, 1300, 1000)
        w.setWindowTitle('lesson 2')
        png = QtGui.QPixmap('./pics/neg_cloud.jpg')
        l1 = QtWidgets.QLabel(w)
        l1.setPixmap(png)
        l1.move(100, 20)
        w.show()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "负向情感词云"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Neg_WordCloud()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
