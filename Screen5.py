# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateNewTimetableScreen(object):
    def setupUi(self, CreateNewTimetableScreen):
        CreateNewTimetableScreen.setObjectName("CreateNewTimetableScreen")
        CreateNewTimetableScreen.resize(800, 318)
        self.centralwidget = QtWidgets.QWidget(CreateNewTimetableScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.StI = QtWidgets.QLabel(self.centralwidget)
        self.StI.setGeometry(QtCore.QRect(10, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StI.setFont(font)
        self.StI.setObjectName("StI")
        self.SubI = QtWidgets.QLabel(self.centralwidget)
        self.SubI.setGeometry(QtCore.QRect(10, 70, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SubI.setFont(font)
        self.SubI.setObjectName("SubI")
        self.PN = QtWidgets.QLabel(self.centralwidget)
        self.PN.setGeometry(QtCore.QRect(190, 130, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PN.setFont(font)
        self.PN.setObjectName("PN")
        self.StISF = QtWidgets.QPushButton(self.centralwidget)
        self.StISF.setGeometry(QtCore.QRect(390, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StISF.setFont(font)
        self.StISF.setObjectName("StISF")
        self.SubSF = QtWidgets.QPushButton(self.centralwidget)
        self.SubSF.setGeometry(QtCore.QRect(390, 80, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SubSF.setFont(font)
        self.SubSF.setObjectName("SubSF")
        self.PNBox = QtWidgets.QComboBox(self.centralwidget)
        self.PNBox.setGeometry(QtCore.QRect(390, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PNBox.setFont(font)
        self.PNBox.setObjectName("PNBox")
        self.Create = QtWidgets.QPushButton(self.centralwidget)
        self.Create.setGeometry(QtCore.QRect(580, 220, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Create.setFont(font)
        self.Create.setObjectName("Create")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(690, 220, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Back.setFont(font)
        self.Back.setObjectName("Back")
        CreateNewTimetableScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateNewTimetableScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        CreateNewTimetableScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateNewTimetableScreen)
        self.statusbar.setObjectName("statusbar")
        CreateNewTimetableScreen.setStatusBar(self.statusbar)

        self.retranslateUi(CreateNewTimetableScreen)
        QtCore.QMetaObject.connectSlotsByName(CreateNewTimetableScreen)

    def retranslateUi(self, CreateNewTimetableScreen):
        _translate = QtCore.QCoreApplication.translate
        CreateNewTimetableScreen.setWindowTitle(_translate("CreateNewTimetableScreen", "MainWindow"))
        self.StI.setText(_translate("CreateNewTimetableScreen", "Import Student Information："))
        self.SubI.setText(_translate("CreateNewTimetableScreen", "Import Subject Information："))
        self.PN.setText(_translate("CreateNewTimetableScreen", "Period number："))
        self.StISF.setText(_translate("CreateNewTimetableScreen", "Select file"))
        self.SubSF.setText(_translate("CreateNewTimetableScreen", "Select file"))
        self.Create.setText(_translate("CreateNewTimetableScreen", "Create"))
        self.Back.setText(_translate("CreateNewTimetableScreen", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateNewTimetableScreen = QtWidgets.QMainWindow()
    ui = Ui_CreateNewTimetableScreen()
    ui.setupUi(CreateNewTimetableScreen)
    CreateNewTimetableScreen.show()
    sys.exit(app.exec_())
