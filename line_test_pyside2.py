import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QPen
from PySide2.QtCore import Qt, QPoint


class LineDrawerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.start_point = None
        self.end_point = None
        self.click_count = 0
        self.lines = []  # List to store all lines (start and end points)
        self.setWindowTitle("Draw Lines with PySide2")
        self.setGeometry(100, 100, 400, 300)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.click_count == 0:
                # First click - store start point
                self.start_point = event.pos()
                self.click_count = 1
            elif self.click_count == 1:
                # Second click - store end point and add the line to the list
                self.end_point = event.pos()
                self.lines.append((self.start_point, self.end_point))
                self.click_count = 0  # Reset click count to allow drawing another line
                self.update()  # Trigger a repaint to draw the lines

    def paintEvent(self, event):
        # Create a QPainter object for drawing
        painter = QPainter(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

        # Iterate over all stored lines and draw each one
        for line in self.lines:
            start_point, end_point = line
            painter.drawLine(start_point, end_point)


class LineDrawerApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.widget = LineDrawerWidget()
        self.widget.show()


if __name__ == '__main__':
    app = LineDrawerApp(sys.argv)
    sys.exit(app.exec_())
