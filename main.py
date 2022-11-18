import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randrange


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.paint)
        self.do_painter = False

    def paintEvent(self, event):
        if self.do_painter:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.do_painter = False

    def paint(self):
        self.do_painter = True
        self.repaint()

    def draw_circle(self, qp):
        n = randrange(10, 31)
        for i in range(n):
            qp.setBrush(QColor(randrange(150, 256), randrange(150, 256), 0))
            d = randrange(50)
            qp.drawEllipse(randrange(500 - d), randrange(500 - d), d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
