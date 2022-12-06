from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout,QTextBrowser
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from pyqt import *
# import  chinese_sentiment_predict as cs
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

class Prediction(QtWidgets.QMainWindow):
    def __init__(self):
        super(Prediction, self).__init__()
        self.setupUi(self)
        # self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.window = QtWidgets.QWidget(MainWindow)
        self.window.resize(1000, 700)
        self.window.move(800, 400)
        self.window.setWindowTitle('中文情感分析')

        self.textEdit = QPlainTextEdit()
        self.textEdit.setPlaceholderText("请输入文本")
        self.textEdit.move(100, 200)
        self.textEdit.resize(800, 400)

        # pic = QtGui.QPixmap('./pos_cloud.png')
        # self.label_pic = QLabel()
        # self.label_pic.setPixmap(pic)
        # self.label_pic.setScaledContents(True)

        self.button = QPushButton('预测', self.window)
        self.button.resize(150, 50)
        self.button.move(100, 100)
        self.button.setGeometry(QtCore.QRect(90, 150, 191, 61))
        self.button.clicked.connect(self.handleCalc)

        self.button1 = QPushButton('积极评价词云',self.window)
        self.button1.resize(200,50)
        self.button1.move(350,100)
        # self.button1.clicked.connect(self.label_pic)

        self.button2 = QPushButton('消极评价词云',self.window)
        self.button2.resize(200,50)
        self.button2.move(650,100)




    def handleCalc(self):
        info = self.textEdit.toPlainText()
        # result = cs.predict_sentiment(info)
        result = 1
        print(type(result))
        if result >= 0.6:
            QMessageBox.about(
                self.window,
                '预测结果',
                 f'''是一例正面评价'''
            )  # :\n{'output=%.2f'%result}
        elif result <= 0.4:
            QMessageBox.about(
                self.window,
                '预测结果',
                f'''是一例负面评价'''
            )
        else:
            QMessageBox.about(
                self.window,
                '预测结果',
                f'''是一例中性评价'''
            )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Prediction()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())