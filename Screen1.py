# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Screen2
import Screen5


class Ui_IntialScreen(object):
    def setupUi(self, IntialScreen):
        self.IntialScreen = IntialScreen
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
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(490, 40, 221, 51))
        self.Logo.setText("")
        self.Logo.setTextFormat(QtCore.Qt.RichText)
        self.Logo.setPixmap(QtGui.QPixmap("2222.jpg"))
        self.Logo.setScaledContents(True)
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
        IntialScreen.setWindowTitle(_translate("IntialScreen", "Intial Screen"))
        self.Title.setText(_translate("IntialScreen", "Schedule timetable"))
        self.Createtimetable.setText(_translate("IntialScreen", "Create timetable"))
        self.Viewtimetable.setText(_translate("IntialScreen", "View timetable"))
        self.Viewtimetable.setText(_translate("IntialScreen", "Viewtimetable"))
        self.Viewtimetable.clicked.connect(self.View)
        self.Createtimetable.setText(_translate("IntialScreen", "Createtimetable"))
        self.Createtimetable.clicked.connect(self.Create)

    def CloseWindow(self):
        self.IntialScreen.destroy()

    def View(self):
        self.Viewer = QtWidgets.QMainWindow()
        self.Viewerui = Screen2.Ui_ViewTimetableScreen()
        self.Viewerui.setupUi(self.Viewer)
        self.Viewer.show()
        self.Viewer.setWindowTitle("View Timetable")
        self.CloseWindow()

    def Create(self):
        self.Creater = QtWidgets.QMainWindow()
        self.Createrui = Screen5.Ui_CreateNewTimetableScreen()
        self.Createrui.setupUi(self.Creater)
        self.Creater.show()
        self.Creater.setWindowTitle("Create Timetable")
        self.CloseWindow()
       
        



   





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IntialScreen = QtWidgets.QMainWindow()
    ui = Ui_IntialScreen()
    ui.setupUi(IntialScreen)
    IntialScreen.show()
    sys.exit(app.exec_())
    
