import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            try:
                qp.begin(self)
                self.draw_flag(qp)
                qp.end()
            except ValueError:
                pass

    def paint(self):
        self.pushButton.setHidden(True)
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        for z in range(randint(10, 20)):
            diameter = randint(20, 100)
            x, y = (randint(0, 300 - diameter), randint(0, 300 - diameter))
            qp.setBrush(Qt.yellow)
            qp.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
