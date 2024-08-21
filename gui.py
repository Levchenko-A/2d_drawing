# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_menubarcLRiYc.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(598, 478)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionCursor = QAction(MainWindow)
        self.actionCursor.setObjectName(u"actionCursor")
        self.actionCoordinates = QAction(MainWindow)
        self.actionCoordinates.setObjectName(u"actionCoordinates")
        self.actionCursor_2 = QAction(MainWindow)
        self.actionCursor_2.setObjectName(u"actionCursor_2")
        self.actionCoordinates_2 = QAction(MainWindow)
        self.actionCoordinates_2.setObjectName(u"actionCoordinates_2")
        self.actionCursor_3 = QAction(MainWindow)
        self.actionCursor_3.setObjectName(u"actionCursor_3")
        self.actionCoordinates_3 = QAction(MainWindow)
        self.actionCoordinates_3.setObjectName(u"actionCoordinates_3")
        self.actionCursor_4 = QAction(MainWindow)
        self.actionCursor_4.setObjectName(u"actionCursor_4")
        self.actionCoordinates_4 = QAction(MainWindow)
        self.actionCoordinates_4.setObjectName(u"actionCoordinates_4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 10, 581, 421))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 598, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuGeometry = QMenu(self.menubar)
        self.menuGeometry.setObjectName(u"menuGeometry")
        self.menuPoint = QMenu(self.menuGeometry)
        self.menuPoint.setObjectName(u"menuPoint")
        self.menuLine = QMenu(self.menuGeometry)
        self.menuLine.setObjectName(u"menuLine")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuPoint_2 = QMenu(self.menuEdit)
        self.menuPoint_2.setObjectName(u"menuPoint_2")
        self.menuLine_2 = QMenu(self.menuEdit)
        self.menuLine_2.setObjectName(u"menuLine_2")
        self.menuEndpoints = QMenu(self.menuLine_2)
        self.menuEndpoints.setObjectName(u"menuEndpoints")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGeometry.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuGeometry.addAction(self.menuPoint.menuAction())
        self.menuGeometry.addAction(self.menuLine.menuAction())
        self.menuPoint.addAction(self.actionCursor)
        self.menuPoint.addAction(self.actionCoordinates)
        self.menuLine.addAction(self.actionCursor_2)
        self.menuLine.addAction(self.actionCoordinates_2)
        self.menuEdit.addAction(self.menuPoint_2.menuAction())
        self.menuEdit.addAction(self.menuLine_2.menuAction())
        self.menuPoint_2.addAction(self.actionCursor_3)
        self.menuPoint_2.addAction(self.actionCoordinates_3)
        self.menuLine_2.addAction(self.menuEndpoints.menuAction())
        self.menuEndpoints.addAction(self.actionCursor_4)
        self.menuEndpoints.addAction(self.actionCoordinates_4)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionCursor.setText(QCoreApplication.translate("MainWindow", u"Cursor", None))
        self.actionCoordinates.setText(QCoreApplication.translate("MainWindow", u"Coordinates", None))
        self.actionCursor_2.setText(QCoreApplication.translate("MainWindow", u"Cursor", None))
        self.actionCoordinates_2.setText(QCoreApplication.translate("MainWindow", u"Coordinates", None))
        self.actionCursor_3.setText(QCoreApplication.translate("MainWindow", u"Cursor", None))
        self.actionCoordinates_3.setText(QCoreApplication.translate("MainWindow", u"Coordinates", None))
        self.actionCursor_4.setText(QCoreApplication.translate("MainWindow", u"Cursor", None))
        self.actionCoordinates_4.setText(QCoreApplication.translate("MainWindow", u"Coordinates", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuGeometry.setTitle(QCoreApplication.translate("MainWindow", u"Geometry", None))
        self.menuPoint.setTitle(QCoreApplication.translate("MainWindow", u"Point", None))
        self.menuLine.setTitle(QCoreApplication.translate("MainWindow", u"Line", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuPoint_2.setTitle(QCoreApplication.translate("MainWindow", u"Point", None))
        self.menuLine_2.setTitle(QCoreApplication.translate("MainWindow", u"Line", None))
        self.menuEndpoints.setTitle(QCoreApplication.translate("MainWindow", u"Endpoints", None))
    # retranslateUi

