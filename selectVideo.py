# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectVideo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from addFaceToAnalyze import *
from videoAnalysis import *

class Ui_selectVideo(object):
    def openFtoAWindow(self):
        self.Window = QtWidgets.QWidget()
        self.ui = addFaceToAnalyze.AFTA_Ui_Form()
        self.ui.setupUi(self.Window)
        self.ui.getVideo(video=self.video)
        self.Window.show()
        self.widget.hide()
        

    def getVideo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"Select Video",options=options)
        if fileName:
            '''vidcap = cv2.VideoCapture(fileName)
            total = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
            num = total/2
            vidcap.set(cv2.CAP_PROP_POS_MSEC,num)
            success,image = vidcap.read()'''
            shortenedFileName = self.getShortenedFilename(fileName)
            self.movieImageLabel.setPixmap( QtGui.QPixmap() )
            self.movieImageLabel.clear()
            self.movieImageLabel.setGeometry(QtCore.QRect(140, 240, 201, 201))
            self.movieImageLabel.setStyleSheet("border: 1px solid black;")
            self.movieImageLabel.setAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(20)
            self.movieImageLabel.setFont(font)
            self.movieImageLabel.setText(shortenedFileName)
            self.pushButton_2.setEnabled(True)
            self.video = fileName


    def getShortenedFilename(self, filename):
        temp = ""
        i = len(filename) - 1
        while i > 0:
            if(filename[i] == '/' or filename[i] == '\\'):
                return temp
            temp = filename[i] + temp
            i-=1

        return temp


    def setupUi(self, selectVideo):
        selectVideo.setObjectName("selectVideo")
        selectVideo.resize(508, 584)
        self.label = QtWidgets.QLabel(selectVideo)
        self.label.setGeometry(QtCore.QRect(90, 40, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(selectVideo)
        self.pushButton.setGeometry(QtCore.QRect(140, 160, 201, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getVideo)
        self.pushButton_2 = QtWidgets.QPushButton(selectVideo)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 490, 201, 41))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openFtoAWindow)
        self.pushButton_2.setEnabled(False)
        self.movieImageLabel = QtWidgets.QLabel(selectVideo)
        self.movieImageLabel.setGeometry(QtCore.QRect(160, 240, 211, 201))
        self.movieImageLabel.setText("")
        self.movieImageLabel.setPixmap(QtGui.QPixmap("../camera.jpg"))
        self.movieImageLabel.setObjectName("movieImageLabel")
        
        self.video = QVideoWidget()
        self.video.resize(300, 300)
        self.video.move(0, 0)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video)
        

        self.retranslateUi(selectVideo)
        QtCore.QMetaObject.connectSlotsByName(selectVideo)
        self.widget = selectVideo

    def retranslateUi(self, selectVideo):
        _translate = QtCore.QCoreApplication.translate
        selectVideo.setWindowTitle(_translate("selectVideo", "Form"))
        self.label.setText(_translate("selectVideo", "Select a video"))
        self.pushButton.setText(_translate("selectVideo", "Select"))
        self.pushButton_2.setText(_translate("selectVideo", "Continue"))
