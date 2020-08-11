# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Screen2
import Screen7
import csv
subject_list = []
with open("Subject.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        subject_list.append(str(row[0]))


class Ui_AddNewStScreen(object):
    def setupUi(self, AddNewStScreen):
        self.AddNewStScreen = AddNewStScreen
        AddNewStScreen.setObjectName("AddNewStScreen")
        AddNewStScreen.resize(800, 500)
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
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(200, 90, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        #########################################################
        # Subject1
        self.Subject1 = QtWidgets.QComboBox(self.centralwidget)
        self.Subject1.setGeometry(QtCore.QRect(200, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Subject1.setFont(font)
        self.Subject1.setObjectName("Subject")
        #Subject2
        self.Subject2 = QtWidgets.QComboBox(self.centralwidget)
        self.Subject2.setGeometry(QtCore.QRect(200, 200, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Subject2.setFont(font)
        self.Subject2.setObjectName("Subject")
        #Subject3
        self.Subject3 = QtWidgets.QComboBox(self.centralwidget)
        self.Subject3.setGeometry(QtCore.QRect(200, 250, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Subject3.setFont(font)
        self.Subject3.setObjectName("Subject")
        #Subject4
        self.Subject4 = QtWidgets.QComboBox(self.centralwidget)
        self.Subject4.setGeometry(QtCore.QRect(200, 300, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Subject4.setFont(font)
        self.Subject4.setObjectName("Subject")
        #Subject5
        self.Subject5 = QtWidgets.QComboBox(self.centralwidget)
        self.Subject5.setGeometry(QtCore.QRect(200, 350, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Subject5.setFont(font)
        self.Subject5.setObjectName("Subject")
        #Subject6
        self.Subject6 = QtWidgets.QComboBox(self.centralwidget)
        self.Subject6.setGeometry(QtCore.QRect(200, 400, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Subject6.setFont(font)
        self.Subject6.setObjectName("Subject")

        #############################################################
        self.ButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAdd.setGeometry(QtCore.QRect(600, 400, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ButtonAdd.setFont(font)
        self.ButtonAdd.setObjectName("ButtonAdd")
        self.ButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonBack.setGeometry(QtCore.QRect(700, 400, 91, 41))
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



        self.Subject1.addItems(subject_list)
        self.Subject2.addItems(subject_list)
        self.Subject3.addItems(subject_list)
        self.Subject4.addItems(subject_list)
        self.Subject5.addItems(subject_list)
        self.Subject6.addItems(subject_list)


    def retranslateUi(self, AddNewStScreen):
        _translate = QtCore.QCoreApplication.translate
        AddNewStScreen.setWindowTitle(_translate("AddNewStScreen", "MainWindow"))
        self.AddStTitle.setText(_translate("AddNewStScreen", "Add New Student"))
        self.StName.setText(_translate("AddNewStScreen", "Student Name:"))
        self.Sub.setText(_translate("AddNewStScreen", "Subject:"))
        self.ButtonAdd.setText(_translate("AddNewStScreen", "Add"))
        self.ButtonAdd.clicked.connect(self.AddData)
        self.ButtonBack.setText(_translate("AddNewStScreen", "Back"))
        self.ButtonBack.clicked.connect(self.GoBack)
        

    def CloseWindow(self):
        self.AddNewStScreen.destroy()

    def GoBack(self):
        self.GB = QtWidgets.QMainWindow()
        self.GBui = Screen2.Ui_ViewTimetableScreen()
        self.GBui.setupUi(self.GB)
        self.GB.show()
        self.GB.setWindowTitle("View Timetable")
        self.CloseWindow()

    def AddData(self):
        if self.Name.text().isalpha() == True:

            with open('StudentData.csv', mode='a') as StudentData:
                StudentData_writer = csv.writer(StudentData, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                StudentData_writer.writerow([self.Name.text(), self.Subject1.currentText(), 
                self.Subject2.currentText(), self.Subject3.currentText(), self.Subject4.currentText(), self.Subject5.currentText(), self.Subject6.currentText(),])
            
            self.GoBack()

        else:
            self.HW = QtWidgets.QMainWindow()
            self.HWui = Screen7.Ui_MainWindow()
            self.HWui.setupUi(self.HW)
            self.HW.show()
            self.HW.setWindowTitle("Wrong input")
            self.CloseWindow()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNewStScreen = QtWidgets.QMainWindow()
    ui = Ui_AddNewStScreen()
    ui.setupUi(AddNewStScreen)
    AddNewStScreen.show()
    sys.exit(app.exec_())
