# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IntialScreen(object):
    def setupUi(self, IntialScreen):
        IntialScreen.setObjectName("IntialScreen")
        IntialScreen.resize(730, 295)
        self.centralwidget = QtWidgets.QWidget(IntialScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(10, 20, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.Createtimetable = QtWidgets.QPushButton(self.centralwidget)
        self.Createtimetable.setGeometry(QtCore.QRect(40, 150, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Createtimetable.setFont(font)
        self.Createtimetable.setObjectName("Createtimetable")
        self.Viewtimetable = QtWidgets.QPushButton(self.centralwidget)
        self.Viewtimetable.setGeometry(QtCore.QRect(400, 150, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Viewtimetable.setFont(font)
        self.Viewtimetable.setObjectName("Viewtimetable")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(490, 40, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Logo.setFont(font)
        self.Logo.setObjectName("Logo")
        IntialScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IntialScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 26))
        self.menubar.setObjectName("menubar")
        IntialScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IntialScreen)
        self.statusbar.setObjectName("statusbar")
        IntialScreen.setStatusBar(self.statusbar)

        self.retranslateUi(IntialScreen)
        QtCore.QMetaObject.connectSlotsByName(IntialScreen)

    def retranslateUi(self, IntialScreen):
        _translate = QtCore.QCoreApplication.translate
        IntialScreen.setWindowTitle(_translate("IntialScreen", "MainWindow"))
        self.Title.setText(_translate("IntialScreen", "Schedule timetable"))
        self.Createtimetable.setText(_translate("IntialScreen", "Create timetable"))
        self.Viewtimetable.setText(_translate("IntialScreen", "View timetable"))
        self.Logo.setText(_translate("IntialScreen", "Logo still design"))
        self.Createtimetable.setText(_translate("MainWindow", "Viewtimetable"))
        self.Createtimetable.clicked.connect(self.View)

    def View(self):
        self.Viewer = QtWidgets.QMainWindow()
        self.Viewerui = View Timetable Screen.ui.Ui_MainWindow()
        self.childui.setupUi(self.childwin)
        self.childwin.show()
        self.childwin.setWindowTitle("CHILD")

        self.childui.pushButton.clicked.connect(self.childOK)

    def childOK(self):
        self.lineEdit.setText(self.childui.lineEdit.text())
        self.childwin.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IntialScreen = QtWidgets.QMainWindow()
    ui = Ui_IntialScreen()
    ui.setupUi(IntialScreen)
    IntialScreen.show()
    sys.exit(app.exec_())
