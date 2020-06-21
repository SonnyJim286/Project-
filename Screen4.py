# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '4.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddNewSubScreen(object):
    def setupUi(self, AddNewSubScreen):
        AddNewSubScreen.setObjectName("AddNewSubScreen")
        AddNewSubScreen.resize(800, 228)
        self.centralwidget = QtWidgets.QWidget(AddNewSubScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.SubjectName = QtWidgets.QLabel(self.centralwidget)
        self.SubjectName.setGeometry(QtCore.QRect(10, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SubjectName.setFont(font)
        self.SubjectName.setObjectName("SubjectName")
        self.SubName = QtWidgets.QTextEdit(self.centralwidget)
        self.SubName.setGeometry(QtCore.QRect(200, 70, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SubName.setFont(font)
        self.SubName.setObjectName("SubName")
        self.ButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAdd.setGeometry(QtCore.QRect(600, 130, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ButtonAdd.setFont(font)
        self.ButtonAdd.setObjectName("ButtonAdd")
        self.BttonBack = QtWidgets.QPushButton(self.centralwidget)
        self.BttonBack.setGeometry(QtCore.QRect(700, 130, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BttonBack.setFont(font)
        self.BttonBack.setObjectName("BttonBack")
        AddNewSubScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddNewSubScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        AddNewSubScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddNewSubScreen)
        self.statusbar.setObjectName("statusbar")
        AddNewSubScreen.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewSubScreen)
        QtCore.QMetaObject.connectSlotsByName(AddNewSubScreen)

    def retranslateUi(self, AddNewSubScreen):
        _translate = QtCore.QCoreApplication.translate
        AddNewSubScreen.setWindowTitle(_translate("AddNewSubScreen", "MainWindow"))
        self.label.setText(_translate("AddNewSubScreen", "Add New Subject"))
        self.SubjectName.setText(_translate("AddNewSubScreen", "Subject Name:"))
        self.ButtonAdd.setText(_translate("AddNewSubScreen", "Add"))
        self.BttonBack.setText(_translate("AddNewSubScreen", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNewSubScreen = QtWidgets.QMainWindow()
    ui = Ui_AddNewSubScreen()
    ui.setupUi(AddNewSubScreen)
    AddNewSubScreen.show()
    sys.exit(app.exec_())
