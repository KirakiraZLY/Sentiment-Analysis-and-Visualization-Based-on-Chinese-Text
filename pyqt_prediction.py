from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout,QTextBrowser
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from pyqt import *
import chinese_sentiment_predict as cs

class Prediction(QtWidgets.QMainWindow):
    def __init__(self):
        super(Prediction, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 110, 600, 150))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("请输入文本")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(200, 350, 350, 200))
        # self.textEdit_2.setStyleSheet("font-family:'Microsoft YaHei';font-size:20px;color:#FFFFF0;")
        # QFont font = QFont("Microsoft YaHei", 20, 2)
        self.textEdit_2.setPlaceholderText("返回结果")
        self.textEdit_2.setObjectName("返回结果")

        w = QtWidgets.QWidget(self.centralwidget)
        w.setGeometry(500, 350, 300, 200)
        w.setWindowTitle('lesson 2')
        png = QtGui.QPixmap('./pics/ques.png')
        l1 = QtWidgets.QLabel(w)
        l1.setPixmap(png)
        l1.move(100, 20)
        w.show()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 600, 80))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 251, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 120, 91, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 510, 581, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 90, 141, 31))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 280, 100, 40))
        self.pushButton.setStyleSheet("background-color:rgb(250,20,147);"
                                      "font-family:'Microsoft YaHei';font-size:20px;color:#FFFFF0;")
        self.pushButton.setObjectName("pushButton")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.pushButton.clicked.connect(self.handleCalc)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def handleCalc(self):
        info = self.textEdit.toPlainText()
        # info = "测试测试测试"
        result = cs.predict_sentiment(info)
        # result = 1
        print(type(result))
        if result >= 0.6:
            st = "这是一例正面评价"
            png = QtGui.QPixmap('./pics/pos_sent.png')
        elif result <= 0.4:
            st = "这是一例负面评价"
            png = QtGui.QPixmap('./pics/neg_sent.png')
        else:
            st = "这是一例中性评价"
            png = QtGui.QPixmap('./pics/neutral_sent.png')
        # self.textEdit_2.setText(info+'\n'+st)
        # self.textEdit_2.resize(350,200)
        # self.textEdit_2.setPixelSize(25)
        self.textEdit_2.setText(
            '<font size= "6">' + info + '</font size>' + '<font color=\"#FF1493\"><font size= "6"><br>' + st + '</font color></br></font size>')
        # self.textEdit_2.setText('<html><font size= "10">'+info+'</font size></html>'+'<html><font size= "10"><br>'+st+'</br></font size></html>')
        w = QtWidgets.QWidget(self.centralwidget)
        w.setGeometry(500, 350, 300, 200)
        w.setWindowTitle('lesson 2')
        # png = QtGui.QPixmap('./pos_cloud.png')
        l1 = QtWidgets.QLabel(w)
        l1.setPixmap(png)
        l1.move(100, 20)
        w.show()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "中文情感预测系统"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:24pt; font-weight:1000; font-family:Microsoft Yahei; color:#FF1493;\">中文情感预测系统</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "点击预测"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Prediction()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
