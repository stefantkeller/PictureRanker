# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Sat Apr 26 17:50:50 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphic_left = QtGui.QGraphicsView(self.centralwidget)
        self.graphic_left.setGeometry(QtCore.QRect(20, 40, 470, 500))
        self.graphic_left.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.graphic_left.setObjectName(_fromUtf8("graphic_left"))
        self.graphic_right = QtGui.QGraphicsView(self.centralwidget)
        self.graphic_right.setGeometry(QtCore.QRect(510, 40, 470, 500))
        self.graphic_right.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.graphic_right.setObjectName(_fromUtf8("graphic_right"))
        self.folderloader = QtGui.QToolButton(self.centralwidget)
        self.folderloader.setGeometry(QtCore.QRect(20, 5, 150, 30))
        self.folderloader.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.folderloader.setObjectName(_fromUtf8("folderloader"))
        self.readbutton = QtGui.QToolButton(self.centralwidget)
        self.readbutton.setGeometry(QtCore.QRect(180, 5, 150, 30))
        self.readbutton.setObjectName(_fromUtf8("readbutton"))
        self.selectleft = QtGui.QToolButton(self.centralwidget)
        self.selectleft.setGeometry(QtCore.QRect(170, 545, 150, 30))
        self.selectleft.setObjectName(_fromUtf8("selectleft"))
        self.selectright = QtGui.QToolButton(self.centralwidget)
        self.selectright.setGeometry(QtCore.QRect(670, 545, 150, 30))
        self.selectright.setObjectName(_fromUtf8("selectright"))
        self.folderlabel = QtGui.QLabel(self.centralwidget)
        self.folderlabel.setGeometry(QtCore.QRect(510, 5, 300, 30))
        self.folderlabel.setText(_fromUtf8(""))
        self.folderlabel.setObjectName(_fromUtf8("folderlabel"))
        self.savebutton = QtGui.QToolButton(self.centralwidget)
        self.savebutton.setGeometry(QtCore.QRect(340, 5, 150, 30))
        self.savebutton.setObjectName(_fromUtf8("savebutton"))
        self.statuslabel = QtGui.QLabel(self.centralwidget)
        self.statuslabel.setGeometry(QtCore.QRect(830, 5, 150, 30))
        self.statuslabel.setText(_fromUtf8(""))
        self.statuslabel.setObjectName(_fromUtf8("statuslabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.folderloader.setText(QtGui.QApplication.translate("MainWindow", "Select folder", None, QtGui.QApplication.UnicodeUTF8))
        self.readbutton.setText(QtGui.QApplication.translate("MainWindow", "Read", None, QtGui.QApplication.UnicodeUTF8))
        self.selectleft.setText(QtGui.QApplication.translate("MainWindow", "left", None, QtGui.QApplication.UnicodeUTF8))
        self.selectright.setText(QtGui.QApplication.translate("MainWindow", "right", None, QtGui.QApplication.UnicodeUTF8))
        self.savebutton.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))

