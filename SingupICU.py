# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SingupICU.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(513, 422)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(186, 226, 255, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.userpassword_labelS = QtWidgets.QLabel(Dialog)
        self.userpassword_labelS.setGeometry(QtCore.QRect(338, 210, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.userpassword_labelS.setFont(font)
        self.userpassword_labelS.setObjectName("userpassword_labelS")
        self.wrongmessage_label = QtWidgets.QLabel(Dialog)
        self.wrongmessage_label.setEnabled(False)
        self.wrongmessage_label.setGeometry(QtCore.QRect(150, 310, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wrongmessage_label.setFont(font)
        self.wrongmessage_label.setObjectName("wrongmessage_label")
        self.Code_label = QtWidgets.QLabel(Dialog)
        self.Code_label.setGeometry(QtCore.QRect(318, 260, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Code_label.setFont(font)
        self.Code_label.setObjectName("Code_label")
        self.username_lineS = QtWidgets.QLineEdit(Dialog)
        self.username_lineS.setGeometry(QtCore.QRect(130, 160, 171, 22))
        self.username_lineS.setText("")
        self.username_lineS.setObjectName("username_lineS")
        self.userpassword_lineS = QtWidgets.QLineEdit(Dialog)
        self.userpassword_lineS.setGeometry(QtCore.QRect(130, 210, 171, 22))
        self.userpassword_lineS.setObjectName("userpassword_lineS")
        self.Code_line = QtWidgets.QLineEdit(Dialog)
        self.Code_line.setGeometry(QtCore.QRect(188, 260, 113, 22))
        self.Code_line.setObjectName("Code_line")
        self.Ok_ButtonS = QtWidgets.QPushButton(Dialog)
        self.Ok_ButtonS.setGeometry(QtCore.QRect(220, 340, 93, 28))
        self.Ok_ButtonS.setObjectName("Ok_ButtonS")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.username_labelS = QtWidgets.QLabel(Dialog)
        self.username_labelS.setGeometry(QtCore.QRect(328, 160, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.username_labelS.setFont(font)
        self.username_labelS.setObjectName("username_labelS")
        self.Iduser_labelS = QtWidgets.QLabel(Dialog)
        self.Iduser_labelS.setGeometry(QtCore.QRect(320, 110, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Iduser_labelS.setFont(font)
        self.Iduser_labelS.setObjectName("Iduser_labelS")
        self.Iduser_lineS = QtWidgets.QLineEdit(Dialog)
        self.Iduser_lineS.setGeometry(QtCore.QRect(130, 110, 171, 22))
        self.Iduser_lineS.setText("")
        self.Iduser_lineS.setObjectName("Iduser_lineS")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.userpassword_labelS.setText(_translate("Dialog", "סיסמא"))
        self.wrongmessage_label.setText(_translate("Dialog", "אחד מהפרטים שהזנת אינם נכונים"))
        self.Code_label.setText(_translate("Dialog", "קוד הרשאה"))
        self.Ok_ButtonS.setText(_translate("Dialog", "אישור"))
        self.label.setText(_translate("Dialog", "הרשמה"))
        self.username_labelS.setText(_translate("Dialog", "שם משתמש"))
        self.Iduser_labelS.setText(_translate("Dialog", "תעודת זהות"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
