import sys

from PySide6.QtWidgets import (QApplication, QMainWindow)

from gui import Ui_MainWindow


def main():
    app = QApplication(sys.argv)
    form = QMainWindow()
    window = Ui_MainWindow()
    window.setupUi(form)
    form.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
