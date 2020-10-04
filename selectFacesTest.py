# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectImagesTest.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1007, 484)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 19, 971, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.selectImagesButton = QtWidgets.QPushButton(Form)
        self.selectImagesButton.setGeometry(QtCore.QRect(400, 110, 201, 121))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.selectImagesButton.setFont(font)
        self.selectImagesButton.setObjectName("selectImagesButton")
        self.viewImagesButton = QtWidgets.QGraphicsView(Form)
        self.viewImagesButton.setGeometry(QtCore.QRect(110, 260, 771, 192))
        self.viewImagesButton.setObjectName("viewImagesButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Select Image(s) of faces "))
        self.selectImagesButton.setText(_translate("Form", "Select\n"
"Image(s)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
