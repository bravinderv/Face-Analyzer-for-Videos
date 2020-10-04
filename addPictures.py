# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPictures.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2
import numpy as np
import time
import face_recognition
import addFaceToAnalyze

class Ui_Form(object):

    def getFaces(self, picNum):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"Select pictures",options=options)
        if fileName:
            pic = fileName
            if(picNum == 1):
                self.pic_1 = pic
                self.pushButton_2.setIcon(QtGui.QIcon(fileName))
                self.pushButton_2.setIconSize(QtCore.QSize(75,210))
                self.pushButton_2.setText("")
            elif(picNum == 2):
                self.pic_2 = pic
                self.pushButton_3.setIcon(QtGui.QIcon(fileName))
                self.pushButton_3.setIconSize(QtCore.QSize(75,210))
                self.pushButton_3.setText("")
            else:
                self.pic_3 = pic
                self.pushButton_4.setIcon(QtGui.QIcon(fileName))
                self.pushButton_4.setIconSize(QtCore.QSize(75,210))
                self.pushButton_4.setText("")

        
    def goBack(self):
        self.widget.hide()
        self.parent.show()
        
        
        
        

    def confirm(self):
        self.widget.hide()
        images = self.getImages()
        self.parentForm.getPictures(images=images)
        self.parent.show()
        


    def getImages(self):
        arrayOfImages = []
        if(self.pic_1):
            arrayOfImages.append(self.pic_1)

        if(self.pic_2):
            arrayOfImages.append(self.pic_2)

        if(self.pic_3):
            arrayOfImages.append(self.pic_3)

        return arrayOfImages

    def setupUi(self, Form, parentWidget, parentForm):

        self.parent = parentWidget
        self.parentForm = parentForm
        
        Form.setObjectName("Form")
        Form.resize(403, 398)
        Form.setWindowTitle("Add pictures")

        self.pic_1 = None
        self.pic_2 = None
        self.pic_3 = None

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(225, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.goBack)
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 200, 111, 120))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.getFaces(1))

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 200, 111, 120))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.getFaces(2))

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 200, 111, 120))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.getFaces(3))

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(75, 340, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.confirm)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.widget = Form

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Add pictures", "Add pictures"))
        self.label.setText(_translate("Form", "Select up to 3 faces for the same person \n(the more faces the more accurate will be)"))
        self.pushButton.setText(_translate("Form", "Back"))
        self.pushButton_2.setText(_translate("Form", "Select \npicture(1)"))
        self.pushButton_3.setText(_translate("Form", "Select \npicture(2)"))
        self.pushButton_4.setText(_translate("Form", "Select \npicture(3)"))
        self.pushButton_5.setText(_translate("Form", "Confirm"))