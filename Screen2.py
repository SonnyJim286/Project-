# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Screen1
import Screen3
import Screen4


class Ui_ViewTimetableScreen(object):
    def setupUi(self, ViewTimetableScreen):
        self.ViewTimetableScreen = ViewTimetableScreen
        ViewTimetableScreen.setObjectName("ViewTimetableScreen")
        ViewTimetableScreen.resize(731, 627)
        self.centralwidget = QtWidgets.QWidget(ViewTimetableScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.Timetableviewer = QtWidgets.QListView(self.centralwidget)
        self.Timetableviewer.setGeometry(QtCore.QRect(0, 0, 731, 511))
        self.Timetableviewer.setObjectName("Timetableviewer")
        self.AddSub = QtWidgets.QPushButton(self.centralwidget)
        self.AddSub.setGeometry(QtCore.QRect(0, 520, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.AddSub.setFont(font)
        self.AddSub.setObjectName("AddSub")
        self.AddSt = QtWidgets.QPushButton(self.centralwidget)
        self.AddSt.setGeometry(QtCore.QRect(180, 520, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.AddSt.setFont(font)
        self.AddSt.setObjectName("AddSt")
        self.BottonSave = QtWidgets.QPushButton(self.centralwidget)
        self.BottonSave.setGeometry(QtCore.QRect(370, 520, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BottonSave.setFont(font)
        self.BottonSave.setObjectName("BottonSave")
        self.ButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonBack.setGeometry(QtCore.QRect(630, 520, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ButtonBack.setFont(font)
        self.ButtonBack.setObjectName("ButtonBack")
        ViewTimetableScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewTimetableScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 26))
        self.menubar.setObjectName("menubar")
        ViewTimetableScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewTimetableScreen)
        self.statusbar.setObjectName("statusbar")
        ViewTimetableScreen.setStatusBar(self.statusbar)

        self.retranslateUi(ViewTimetableScreen)
        QtCore.QMetaObject.connectSlotsByName(ViewTimetableScreen)

    def retranslateUi(self, ViewTimetableScreen):
        _translate = QtCore.QCoreApplication.translate
        ViewTimetableScreen.setWindowTitle(_translate("ViewTimetableScreen", "MainWindow"))
        self.AddSub.setText(_translate("ViewTimetableScreen", "Add Subject"))
        self.AddSt.setText(_translate("ViewTimetableScreen", "Add Student"))
        self.BottonSave.setText(_translate("ViewTimetableScreen", "Save"))
        self.ButtonBack.setText(_translate("ViewTimetableScreen", "Back"))
        self.ButtonBack.clicked.connect(self.GoBack)
        self.AddSt.setText(_translate("MainWindow", "Add Student"))
        self.AddSt.clicked.connect(self.AddStudent)
        self.AddSub.setText(_translate("MainWindow", "Add Subject"))
        self.AddSub.clicked.connect(self.AddSubject)

    def CloseWindow(self):
        self.ViewTimetableScreen.destroy()

    def AddStudent(self):
        self.ADST = QtWidgets.QMainWindow()
        self.ADSTui = Screen3.Ui_AddNewStScreen()
        self.ADSTui.setupUi(self.ADST)
        self.ADST.show()
        self.ADST.setWindowTitle("Add New Student")
        self.CloseWindow()

    def AddSubject(self):
        self.ADSU = QtWidgets.QMainWindow()
        self.ADSUui = Screen4.Ui_AddNewSubScreen()
        self.ADSUui.setupUi(self.ADSU)
        self.ADSU.show()
        self.ADSU.setWindowTitle("Add New Subject")
        self.CloseWindow()

    def GoBack(self):
        self.GB = QtWidgets.QMainWindow()
        self.GBui = Screen1.Ui_IntialScreen()
        self.GBui.setupUi(self.GB)
        self.GB.show()
        self.GB.setWindowTitle("Intial Screen")
        self.CloseWindow()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewTimetableScreen = QtWidgets.QMainWindow()
    ui = Ui_ViewTimetableScreen()
    ui.setupUi(ViewTimetableScreen)
    ViewTimetableScreen.show()
    sys.exit(app.exec_())
