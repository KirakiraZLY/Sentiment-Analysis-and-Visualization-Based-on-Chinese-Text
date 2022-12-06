from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout,QTextBrowser
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from pyqt_prediction import *
from pyqt_about import *
from pyqt_posword import *
from pyqt_negword import *

import chinese_sentiment_predict as cs
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

class Stats(QtWidgets.QMainWindow):
    def __init__(self):
        super(Stats,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000,700)
        # MainWindow.setStyleSheet()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(250, 180, 180, 60))
        self.pushButton_1.setStyleSheet("font: 12pt, Microsoft Yahei;\n""")
        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 180, 220, 60))
        self.pushButton_2.setStyleSheet("font: 12pt \"Microsoft Yahei\";\n""")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 300, 220, 60))
        self.pushButton_3.setStyleSheet("font: 12pt \"Microsoft Yahei\";\n""")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 300, 180, 60))
        self.pushButton_4.setStyleSheet("font: 12pt \"Microsoft Yahei\";\n""")
        self.pushButton_4.setObjectName("pushButton_4")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 50, 351, 111))
        self.label.setObjectName("label")

        w = QtWidgets.QWidget(self.centralwidget)
        w.setGeometry(250, 400, 700, 800)
        png = QtGui.QPixmap('./pics/main_pic2.png')
        l1 = QtWidgets.QLabel(w)
        l1.setPixmap(png)
        l1.move(100, 20)
        w.show()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_1.clicked.connect(self.prediction)
        self.pushButton_2.clicked.connect(self.pos_wordcloud)
        self.pushButton_3.clicked.connect(self.neg_wordcloud)
        self.pushButton_4.clicked.connect(self.about)

    def prediction(self):
        ui_hello_1.show()
        # MainWindow.close()

    def pos_wordcloud(self):
        """
        w = QtWidgets.QWidget(self.centralwidget)
        w.setGeometry(150, 380, 900, 500)
        png = QtGui.QPixmap('./pos_cloud.jpg')
        l1 = QtWidgets.QLabel(w)
        l1.setPixmap(png)
        l1.move(100, 20)
        w.show()
        """
        ui_hello_2.show()

    def neg_wordcloud(self):
        """
        w = QtWidgets.QWidget(self.centralwidget)
        w.setGeometry(150, 380, 900, 500)
        png = QtGui.QPixmap('./neg_cloud.jpg')
        # png.raise_()
        l2 = QtWidgets.QLabel(w)
        l2.setPixmap(png)
        l2.move(100, 20)
        w.show()
        """
        ui_hello_3.show()

    def about(self):
        ui_hello_4.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "中文情感分析"))
        self.pushButton_1.setText(_translate("MainWindow", "情感预测"))
        self.pushButton_2.setText(_translate("MainWindow", "正向情感词云"))
        self.pushButton_3.setText(_translate("MainWindow", "负向情感词云"))
        self.pushButton_4.setText(_translate("MainWindow", "关于"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; font-family:Microsoft Yahei; color:#FF1493;\">中文情感分析</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Stats()
    ui.setupUi(MainWindow)
    ui_hello_1 = Prediction()
    ui_hello_2 = Pos_WordCloud()
    ui_hello_3 = Neg_WordCloud()
    ui_hello_4 = About()
    MainWindow.show()
    sys.exit(app.exec_())

"""
        self.window = QMainWindow()
        self.window.resize(1000, 700)
        self.window.move(800, 400)
        self.window.setWindowTitle('中文情感分析')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入文本")
        self.textEdit.move(100, 200)
        self.textEdit.resize(800, 400)

        pic = QtGui.QPixmap('./pos_cloud.png')
        self.label_pic = QLabel()
        self.label_pic.setPixmap(pic)
        self.label_pic.setScaledContents(True)

        self.button = QPushButton('预测', self.window)
        self.button.resize(150,50)
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

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)
stats = Stats()
stats.window.show()
app.exec_()
"""
'''
def handleCalc():
    info = textEdit.toPlainText()
    # result = cs.predict_sentiment(info)
    result = 1
    print(type(result))
    if result >= 0.6:
        QMessageBox.about(
            window,
            '预测结果',

        ) # :\n{'output=%.2f'%result}
    elif result <= 0.4:
        QMessageBox.about(
            window,
            '预测结果',

        )
    else:
        QMessageBox.about(
            window,
            '预测结果',
        
        )



app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

window = QMainWindow()
window.resize(1000, 800)
window.move(400, 400)
window.setWindowTitle('中文情感分析')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入文本")
textEdit.move(50,30)
textEdit.resize(500,550)

button = QPushButton('预测', window)
button.resize(200,100)
button.move(380,280)
button.clicked.connect(handleCalc)

button1 = QPushButton('预测', window)

label1 = QLabel()

window.show()

app.exec_()

'''