import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 5000, 2400)
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        color = QColor(255,255,0)
        qp.setBrush(color)
        qp.setPen(color)
        size = randint(10, 300)
        x = randint(0, 400)
        y = randint(0, 250)
        qp.drawEllipse(x, y, size, size)
        qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


application = QApplication(sys.argv)
sys.excepthook = except_hook
executable = MainWindow()
executable.show()
sys.exit(application.exec_())