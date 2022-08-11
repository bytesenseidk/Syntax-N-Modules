import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable, pyqtSignal


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 573, 240)
        self.setWindowTitle("PyQt5 Demonstration")
        self.initUI()

        self.count = 0

    def initUI(self):
        self.top_label = QtWidgets.QLabel(self)
        self.top_label.setGeometry(QtCore.QRect(10, 10, 551, 51))
        font = QtGui.QFont(); font.setFamily("Courier New")
        font.setPointSize(36); font.setBold(True)
        font.setWeight(75); self.top_label.setFont(font)
        self.top_label.setObjectName("top_label")
        self.top_label.setText("PyQt5 Demonstration")

        self.change_label = QtWidgets.QLabel(self)
        self.change_label.setGeometry(QtCore.QRect(210, 90, 131, 31))
        font = QtGui.QFont(); font.setPointSize(16)
        font.setBold(True); font.setWeight(75)
        self.change_label.setFont(font)
        self.change_label.setObjectName("change_label")
        self.change_label.setText("Change Me!")

        self.button = QtWidgets.QPushButton(self)
        self.button.setGeometry(QtCore.QRect(210, 140, 131, 41))
        font = QtGui.QFont(); font.setPointSize(14)
        font.setBold(True); font.setWeight(75)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.button.setText("Press Here!")
        self.button.clicked.connect(self.pressed)

        self.lcd_counter = QtWidgets.QLCDNumber(self)
        self.lcd_counter.setGeometry(QtCore.QRect(440, 100, 80, 35))
        self.lcd_counter.setObjectName("lcd_counter")

        self.count_label = QtWidgets.QLabel(self)
        self.count_label.setGeometry(QtCore.QRect(410, 70, 141, 31))
        font = QtGui.QFont(); font.setPointSize(12)
        font.setBold(True); font.setWeight(75)
        self.count_label.setFont(font)
        self.count_label.setObjectName("count_label")
        self.count_label.setText("Pressed Counter:")

        self.raise_amount = QtWidgets.QSpinBox(self)
        self.raise_amount.setGeometry(QtCore.QRect(50, 100, 42, 22))
        self.raise_amount.setObjectName("raise_amount")

        self.raise_label = QtWidgets.QLabel(self)
        self.raise_label.setGeometry(QtCore.QRect(10, 70, 131, 31))
        font = QtGui.QFont(); font.setPointSize(12)
        font.setBold(True); font.setWeight(75)
        self.raise_label.setFont(font)
        self.raise_label.setObjectName("raise_label")
        self.raise_label.setText("Raise Amount:")


    def pressed(self):
        raise_amount = self.raise_amount.value()
        self.count += raise_amount
        self.lcd_counter.display(self.count)
        self.change_label.setText(f"Count: {self.count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
