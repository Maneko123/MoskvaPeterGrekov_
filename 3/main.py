import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 5000, 2400)
        self.setWindowTitle('Pushbutton')
        self.button = QPushButton('Нажми', self)
        self.button.clicked.connect(self.draw)

    def draw(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setBrush(color)
        qp.setPen(color)
        size = randint(10, 300)
        x = randint(0, 400)
        y = randint(0, 250)
        qp.drawEllipse(x, y, size, size)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
