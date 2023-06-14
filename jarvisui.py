from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowgui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 764)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-6, -5, 1031, 771))
        self.bg.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.gui = QtWidgets.QLabel(self.centralwidget)
        self.gui.setGeometry(QtCore.QRect(4, 5, 1011, 751))
        self.gui.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border : 2px Solid Red")
        self.gui.setText("")
        self.gui.setPixmap(QtGui.QPixmap("D:\\BCA III final draft project\\DataBase\\GUI\\gui1.jpg"))
        self.gui.setScaledContents(True)
        self.gui.setObjectName("gui")
        self.START = QtWidgets.QPushButton(self.centralwidget)
        self.START.setGeometry(QtCore.QRect(442, 547, 131, 101))
        self.START.setStyleSheet("background-color: transparent;\n"
"font: 75 14pt \"Comic Sans MS\";\n"
"color: rgb(255, 0, 0);\n"
"")
        self.START.setObjectName("START")
        self.STOP = QtWidgets.QPushButton(self.centralwidget)
        self.STOP.setGeometry(QtCore.QRect(852, 687, 151, 51))
        self.STOP.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Timeline\";\n"
"color: rgb(85, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border : 2px Solid Red")
        self.STOP.setObjectName("STOP")
        self.side1 = QtWidgets.QLabel(self.centralwidget)
        self.side1.setGeometry(QtCore.QRect(10, 630, 311, 121))
        self.side1.setText("")
        self.side1.setPixmap(QtGui.QPixmap("D:\\BCA III final draft project\\DataBase\\GUI\\gui2.gif"))
        self.side1.setScaledContents(True)
        self.side1.setObjectName("side1")
        self.side2 = QtWidgets.QLabel(self.centralwidget)
        self.side2.setGeometry(QtCore.QRect(780, 40, 191, 191))
        self.side2.setText("")
        self.side2.setPixmap(QtGui.QPixmap("D:\\BCA III final draft project\\DataBase\\GUI\\gui7.gif"))
        self.side2.setScaledContents(True)
        self.side2.setObjectName("side2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.START.setText(_translate("MainWindow", "START"))
        self.STOP.setText(_translate("MainWindow", "STOP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowgui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
