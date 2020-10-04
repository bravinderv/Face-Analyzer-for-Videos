# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoFaceMainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from selectVideo import *

class Ui_Form(object):

    def openSelectVideo(self):
        self.Window = QtWidgets.QWidget()
        self.ui = Ui_selectVideo()
        self.ui.setupUi(self.Window)
        self.Window.show()
        MainWindow.hide()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 304)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 190, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openSelectVideo)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Welcome to Video-Face Analyzer"))
        self.label_2.setText(_translate("Form", "This app allows the user to input a video then input pictures of \n"
"multiple people. the app will then output how often each of those people \n"
"appear in the video."))
        self.pushButton.setText(_translate("Form", "BEGIN"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
