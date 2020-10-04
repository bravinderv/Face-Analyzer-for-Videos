# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faceAnalyzerSelectTest.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_selectVideo(object):
    def setupUi(self, selectVideo):
        selectVideo.setObjectName("selectVideo")
        selectVideo.resize(400, 474)
        self.label = QtWidgets.QLabel(selectVideo)
        self.label.setGeometry(QtCore.QRect(10, 9, 381, 61))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(selectVideo)
        self.pushButton.setGeometry(QtCore.QRect(130, 70, 141, 71))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(selectVideo)
        self.graphicsView.setGeometry(QtCore.QRect(110, 180, 181, 151))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_2 = QtWidgets.QPushButton(selectVideo)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 380, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(selectVideo)
        QtCore.QMetaObject.connectSlotsByName(selectVideo)

    def retranslateUi(self, selectVideo):
        _translate = QtCore.QCoreApplication.translate
        selectVideo.setWindowTitle(_translate("selectVideo", "Select Video"))
        self.label.setText(_translate("selectVideo", "Select a Video to Analyze"))
        self.pushButton.setText(_translate("selectVideo", "Select\n"
"Video"))
        self.pushButton_2.setText(_translate("selectVideo", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectVideo = QtWidgets.QWidget()
    ui = Ui_selectVideo()
    ui.setupUi(selectVideo)
    selectVideo.show()
    sys.exit(app.exec_())
