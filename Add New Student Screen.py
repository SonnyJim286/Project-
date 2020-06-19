# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddNewStScreen(object):
    def setupUi(self, AddNewStScreen):
        AddNewStScreen.setObjectName("AddNewStScreen")
        AddNewStScreen.resize(800, 305)
        self.centralwidget = QtWidgets.QWidget(AddNewStScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.AddStTitle = QtWidgets.QLabel(self.centralwidget)
        self.AddStTitle.setGeometry(QtCore.QRect(10, 0, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AddStTitle.setFont(font)
        self.AddStTitle.setObjectName("AddStTitle")
        self.StName = QtWidgets.QLabel(self.centralwidget)
        self.StName.setGeometry(QtCore.QRect(10, 90, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StName.setFont(font)
        self.StName.setObjectName("StName")
        self.Sub = QtWidgets.QLabel(self.centralwidget)
        self.Sub.setGeometry(QtCore.QRect(80, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Sub.setFont(font)
        self.Sub.setObjectName("Sub")
        self.Name = QtWidgets.QTextEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(200, 90, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.Subject = QtWidgets.QComboBox(self.centralwidget)
        self.Subject.setGeometry(QtCore.QRect(200, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Subject.setFont(font)
        self.Subject.setObjectName("Subject")
        self.ButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAdd.setGeometry(QtCore.QRect(600, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ButtonAdd.setFont(font)
        self.ButtonAdd.setObjectName("ButtonAdd")
        self.ButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonBack.setGeometry(QtCore.QRect(700, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ButtonBack.setFont(font)
        self.ButtonBack.setObjectName("ButtonBack")
        AddNewStScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddNewStScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        AddNewStScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddNewStScreen)
        self.statusbar.setObjectName("statusbar")
        AddNewStScreen.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewStScreen)
        QtCore.QMetaObject.connectSlotsByName(AddNewStScreen)

    def retranslateUi(self, AddNewStScreen):
        _translate = QtCore.QCoreApplication.translate
        AddNewStScreen.setWindowTitle(_translate("AddNewStScreen", "MainWindow"))
        self.AddStTitle.setText(_translate("AddNewStScreen", "Add New Student"))
        self.StName.setText(_translate("AddNewStScreen", "Student Name:"))
        self.Sub.setText(_translate("AddNewStScreen", "Subject:"))
        self.ButtonAdd.setText(_translate("AddNewStScreen", "Add"))
        self.ButtonBack.setText(_translate("AddNewStScreen", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNewStScreen = QtWidgets.QMainWindow()
    ui = Ui_AddNewStScreen()
    ui.setupUi(AddNewStScreen)
    AddNewStScreen.show()
    sys.exit(app.exec_())
