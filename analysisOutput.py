from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from cv2 import *



class Analysis_Form(object):

    def createTable(self,names, stats, video, pics):
       # Create table

        self.tableWidget = QTableWidget()
        self.tableWidget.resize(625,500)
        self.tableWidget.setRowCount(len(names))
        self.tableWidget.setColumnCount(5)
        #self.tableWidget.setCellWidget(1,1,self.label)
        #self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setHorizontalHeaderLabels(['  Name  ', '  Picture  ', '  Seconds (s)  ','  Minutes (m:s)  ','  Percent (%)  '])
        self.setNames(names)
        self.setPics(pics)
        self.setStats(stats, video)
        
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.show()

    def setNames(self, names ):
        for i in range(0, len(names)):
            self.tableWidget.setItem(i,0, QTableWidgetItem("  " + names[i] + "  "))

    def setPics(self, pics):
        for i in range(0, len(pics)):
            self.label = QtWidgets.QLabel()
            pixMap = QtGui.QPixmap(pics[i][0])
            pixMap = pixMap.scaled(100, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(pixMap)
            self.label.resize(110,160)
            self.tableWidget.setCellWidget(i,1, self.label)
            
    def setStats(self, stats, video):

        vidcap =  VideoCapture(video)  #40001
        total = int(vidcap.get(CAP_PROP_FRAME_COUNT))
        fps = vidcap.get(CAP_PROP_FPS) 
        duration = total/fps

        for i in range(0, len(stats)):
            self.tableWidget.setItem(i,2, QTableWidgetItem("  " + str(stats[i]) + "  "))
            minutes = int(stats[i])/int(60)
            seconds = int(stats[i])%60
            minSec = str(int(minutes)) + ":" + str(seconds)
            self.tableWidget.setItem(i,3, QTableWidgetItem("  " + minSec + "  "))
            percent = int(stats[i] * 100)/int(duration)
            self.tableWidget.setItem(i,4, QTableWidgetItem("  " + str(int(percent)) + " %  " ))

    def setupUi(self, Form, names, stats, video, pics):
        Form.setObjectName("Results")
        self.createTable(names,stats,video,pics)
        self.retranslateUi(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Results", "Results"))