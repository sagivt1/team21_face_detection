# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from singup import Ui_MainWindow


class Ui_Dialog(object):
    def connectCheck(self):
        self.singupWindow=QtGui.QUi_MainWindow()
        self.ui=Ui_MainWindow()
        self.setupUi(self.singupWindow)
        self.singupWindow.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 450)
        self.userpassword_box = QtWidgets.QTextBrowser(Dialog)
        self.userpassword_box.setGeometry(QtCore.QRect(130, 244, 191, 31))
        self.userpassword_box.setFrameShape(QtWidgets.QFrame.Box)
        self.userpassword_box.setFrameShadow(QtWidgets.QFrame.Plain)
        self.userpassword_box.setObjectName("userpassword_box")
        self.userpassword_label = QtWidgets.QLabel(Dialog)
        self.userpassword_label.setGeometry(QtCore.QRect(330, 254, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.userpassword_label.setFont(font)
        self.userpassword_label.setObjectName("userpassword_label")
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(330, 210, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.username_label.setFont(font)
        self.username_label.setAutoFillBackground(False)
        self.username_label.setTextFormat(QtCore.Qt.PlainText)
        self.username_label.setObjectName("username_label")
        self.singup_botton = QtWidgets.QPushButton(Dialog)
        self.singup_botton.setGeometry(QtCore.QRect(160, 320, 93, 28))
        self.singup_botton.setObjectName("singup_botton")
        self.username_box = QtWidgets.QTextBrowser(Dialog)
        self.username_box.setGeometry(QtCore.QRect(130, 204, 191, 31))
        self.username_box.setFrameShape(QtWidgets.QFrame.Box)
        self.username_box.setFrameShadow(QtWidgets.QFrame.Plain)
        self.username_box.setObjectName("username_box")
        self.connect_botton = QtWidgets.QPushButton(Dialog)
        self.connect_botton.setGeometry(QtCore.QRect(290, 320, 93, 28))
        self.connect_botton.setObjectName("connect_botton")
        self.connect_botton.clicked.connect(self.connectCheck)
        self.CU = QtWidgets.QLabel(Dialog)
        self.CU.setGeometry(QtCore.QRect(210, 70, 131, 101))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.CU.setFont(font)
        self.CU.setObjectName("CU")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Form"))
        self.userpassword_label.setText(_translate("Dialog", "סיסמא"))
        self.username_label.setText(_translate("Dialog", "שם משתמש"))
        self.singup_botton.setText(_translate("Dialog", "הירשם"))
        self.connect_botton.setText(_translate("Dialog", "התחבר"))
        self.CU.setText(_translate("Dialog", "ICU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
