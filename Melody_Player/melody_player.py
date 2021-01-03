import sys, winsound
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(548, 225, 548, 225)
        self.setWindowTitle("Melody Player")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.initUI()

    def initUI(self):
        self.Button_00 = QtWidgets.QPushButton(self)
        self.Button_00.setGeometry(QtCore.QRect(10, 10, 75, 71))
        self.Button_00.setObjectName("Button_00")
        self.Button_00.setText("♩")
        self.Button_00.clicked.connect(lambda: winsound.Beep(2300, 100))

        self.Button_01 = QtWidgets.QPushButton(self)
        self.Button_01.setGeometry(QtCore.QRect(100, 10, 75, 71))
        self.Button_01.setObjectName("Button_01")
        self.Button_01.setText("♪")
        self.Button_01.clicked.connect(lambda: winsound.Beep(2100, 100))
        
        self.Button_02 = QtWidgets.QPushButton(self)
        self.Button_02.setGeometry(QtCore.QRect(190, 10, 75, 71))
        self.Button_02.setObjectName("Button_02")
        self.Button_02.setText("♫")
        self.Button_02.clicked.connect(lambda: winsound.Beep(1900, 100))

        self.Button_03 = QtWidgets.QPushButton(self)
        self.Button_03.setGeometry(QtCore.QRect(280, 10, 75, 71))
        self.Button_03.setObjectName("Button_03")
        self.Button_03.setText("≠")
        self.Button_03.clicked.connect(lambda: winsound.Beep(1700, 100))

        self.Button_04 = QtWidgets.QPushButton(self)
        self.Button_04.setGeometry(QtCore.QRect(370, 10, 75, 71))
        self.Button_04.setObjectName("Button_04")
        self.Button_04.setText("♭")
        self.Button_04.clicked.connect(lambda: winsound.Beep(1500, 100))

        self.Button_05 = QtWidgets.QPushButton(self)
        self.Button_05.setGeometry(QtCore.QRect(460, 10, 75, 71))
        self.Button_05.setObjectName("Button_05")
        self.Button_05.setText("♮")
        self.Button_05.clicked.connect(lambda: winsound.Beep(1300, 100))

        self.Button_06 = QtWidgets.QPushButton(self)
        self.Button_06.setGeometry(QtCore.QRect(10, 90, 75, 71))
        self.Button_06.setObjectName("Button_06")
        self.Button_06.setText("°")
        self.Button_06.clicked.connect(lambda: winsound.Beep(1100, 100))

        self.Button_07 = QtWidgets.QPushButton(self)
        self.Button_07.setGeometry(QtCore.QRect(100, 90, 75, 71))
        self.Button_07.setObjectName("Button_07")
        self.Button_07.setText("ø")
        self.Button_07.clicked.connect(lambda: winsound.Beep(900, 100))

        self.Button_08 = QtWidgets.QPushButton(self)
        self.Button_08.setGeometry(QtCore.QRect(190, 90, 75, 71))
        self.Button_08.setObjectName("Button_08")
        self.Button_08.setText("♬")
        self.Button_08.clicked.connect(lambda: winsound.Beep(700, 100))

        self.Button_09 = QtWidgets.QPushButton(self)
        self.Button_09.setGeometry(QtCore.QRect(280, 90, 75, 71))
        self.Button_09.setObjectName("Button_09")
        self.Button_09.setText("≭")
        self.Button_09.clicked.connect(lambda: winsound.Beep(500, 100))

        self.Button_10 = QtWidgets.QPushButton(self)
        self.Button_10.setGeometry(QtCore.QRect(370, 90, 75, 71))
        self.Button_10.setObjectName("Button_10")
        self.Button_10.setText("♯")
        self.Button_10.clicked.connect(lambda: winsound.Beep(300, 100))

        self.Button_11 = QtWidgets.QPushButton(self)
        self.Button_11.setGeometry(QtCore.QRect(460, 90, 75, 71))
        self.Button_11.setObjectName("Button_11")
        self.Button_11.setText("؂")
        self.Button_11.clicked.connect(lambda: winsound.Beep(100, 100))

        self.tag = QtWidgets.QLabel(self)
        self.tag.setGeometry(QtCore.QRect(220, 170, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tag.setFont(font)
        self.tag.setObjectName("tag")
        self.tag.setText("python_genius")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


