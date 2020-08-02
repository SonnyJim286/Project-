# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Screen6.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Screen3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 163)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Notice = QtWidgets.QLabel(self.centralwidget)
        self.Notice.setGeometry(QtCore.QRect(20, 10, 711, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Notice.setFont(font)
        self.Notice.setObjectName("Notice")
        self.ButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonBack.setGeometry(QtCore.QRect(690, 70, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ButtonBack.setFont(font)
        self.ButtonBack.setObjectName("ButtonBack")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Notice.setText(_translate("MainWindow", "Please enter right Student name.(Your input should only be letter -c-)"))
        self.ButtonBack.setText(_translate("MainWindow", "Back"))
        self.ButtonBack.clicked.connect(self.GoBack)

    def CloseWindow(self):
        
        self.MainWindow.destroy()

    def GoBack(self):
        self.GB = QtWidgets.QMainWindow()
        self.GBui = Screen3.Ui_AddNewStScreen()
        self.GBui.setupUi(self.GB)
        self.GB.show()
        self.GB.setWindowTitle("Add New Student")
        self.CloseWindow()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
