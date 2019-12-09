# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginICU.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SingupICU import Ui_Dialog

class Ui_MainWindow(object):

    def ButtonSingin(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 422)
        MainWindow.setStyleSheet("QMainWindow {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(186, 226, 255, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userpassword_line = QtWidgets.QLineEdit(self.centralwidget)
        self.userpassword_line.setGeometry(QtCore.QRect(170, 210, 161, 22))
        self.userpassword_line.setObjectName("userpassword_line")
        self.username_line = QtWidgets.QLineEdit(self.centralwidget)
        self.username_line.setGeometry(QtCore.QRect(170, 160, 161, 22))
        self.username_line.setObjectName("username_line")
        self.userpassword_label = QtWidgets.QLabel(self.centralwidget)
        self.userpassword_label.setGeometry(QtCore.QRect(350, 210, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.userpassword_label.setFont(font)
        self.userpassword_label.setObjectName("userpassword_label")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(350, 160, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")


        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(350, 310, 93, 28))
        self.login_button.setObjectName("login_button")


        self.singup_button = QtWidgets.QPushButton(self.centralwidget)
        self.singup_button.setGeometry(QtCore.QRect(190, 310, 93, 28))
        self.singup_button.setObjectName("singup_button")
        self.singup_button.clicked.connect(self.ButtonSingin)


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.wrongmessage_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.wrongmessage_label_2.setEnabled(False)
        self.wrongmessage_label_2.setGeometry(QtCore.QRect(150, 250, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wrongmessage_label_2.setFont(font)
        self.wrongmessage_label_2.setObjectName("wrongmessage_label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.userpassword_label.setText(_translate("MainWindow", "סיסמא"))
        self.username_label.setText(_translate("MainWindow", "שם משתמש"))
        self.login_button.setText(_translate("MainWindow", "התחבר"))
        self.singup_button.setText(_translate("MainWindow", "הרשמה"))
        self.label_2.setText(_translate("MainWindow", "ICU"))
        self.wrongmessage_label_2.setText(_translate("MainWindow", "שם המשתמש או הסיסמא אינם נכונים"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
