# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addFaceToAnalyze.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from addPictures import Ui_Form as addPictures_Form
from addPictures import *
from selectVideo import *
from videoAnalysis import *
from analysisOutput import *

class AFTA_Ui_Form(object):

    def openAddPicturesWindow(self):
        self.ui.setupUi(self.Window, self.widget, self)
        self.Window.show()
        self.widget.hide()

    def getVideo(self, video):
        self.video = video

    def encodeImages(self, images):
        encodings = []
        for image in images:
            img = face_recognition.load_image_file(image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(img, number_of_times_to_upsample=0)
            top, right, bottom, left = face_locations[0]
            face_image = img[top:bottom, left:right] 
            height, width, _ = face_image.shape
            fl = (0, width, height,0)

            encodedImage = face_recognition.face_encodings(face_image, [fl], num_jitters=0)[0]
            
            encodings.append(encodedImage)

        return encodings

    def analyzeTheVideo(self):

        self.widget.hide()
        self.loadWindow = QtWidgets.QWidget()
        self.analyzeVideoForm = videoAnalysis()
        self.analyzeVideoForm.setUpLoading(self.loadWindow)
        self.loadWindow.show()
        stats = self.analyzeVideoForm.analyzeVideo(video=self.video, arrayOfFaces=self.arrayOfArrayOfEncodings)
        self.loadWindow.hide()
        self.win = QtWidgets.QWidget()
        names = self.getAllNames()
        self.analysisForm.setupUi(self.win, names, stats, self.video, self.arrayOfArrayOfImages )
        

        
    def getAllNames(self):
        names = []
        for textbox in self.arrayOfTextBoxes:
            names.append( textbox.toPlainText() )

        return names

    def getPictures(self, images):
        if(len(images) == 0):
            return
        self.arrayOfArrayOfImages.append(images)
        encodings = self.encodeImages(images)
        self.arrayOfArrayOfEncodings.append( encodings )
        self.newButton.setIcon(QtGui.QIcon(images[0]))

        self.extendPage()
        self.buttonY += 150

        self.newButton = QtWidgets.QPushButton(self.widget)
        #QRect (Pos L-R,pos U-D , W, H)
        self.newButton.setGeometry(QtCore.QRect(280, self.buttonY, 131, 131))
        self.newButton.setText("")
        self.newButton.setIcon(QtGui.QIcon("../question mark.png"))
        self.newButton.clicked.connect(self.openAddPicturesWindow)
        self.newButton.setIconSize(QtCore.QSize(120,110))
        self.arrayOfButtons.append(self.newButton)

        self.arrayOfTextBoxes.append(self.textBox)

        self.textBox = QtWidgets.QTextEdit(self.widget)
        self.textBox.setGeometry(QtCore.QRect(50, self.buttonY +55, 201, 28))


        
        #need to get the array of images, add them to the list of faces
    def extendPage(self):
        self.y+= 150
        self.widget.resize(self.x,self.y)
        self.analyzeY += 150
        self.pushButton.setGeometry(QtCore.QRect(100, self.analyzeY, 201, 28))
        
    def addImages(self, pic_1, pic_2, pic_3):
        arrayOfImages = []
        if(pic_1):
            arrayOfImages.append(pic_1)

        if(pic_2):
            arrayOfImages.append(pic_2)

        if(pic_3):
            arrayOfImages.append(pic_3)

        self.arrayOfArrayOfImages.append(arrayOfImages)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.x = 433
        self.y = 453

        self.arrayOfArrayOfImages = []
        self.arrayOfArrayOfEncodings = []
        self.arrayOfButtons = []
        self.arrayOfTextBoxes = []

        self.nameLabel = QtWidgets.QLabel(Form)
        self.nameLabel.setText("Name of Face:")
        self.nameLabel.setGeometry(QtCore.QRect(110, 240, 101, 30))

        self.textBox = QtWidgets.QTextEdit(Form)
        self.textBox.setGeometry(QtCore.QRect(50, 275, 201, 28))

        Form.resize(self.x, self.y)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 19, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 79, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.analyzeY = 390
        self.pushButton.setGeometry(QtCore.QRect(100, self.analyzeY, 201, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.analyzeTheVideo)
        self.newButton = QtWidgets.QPushButton(Form)
        #QRect (Pos L-R,pos U-D , W, H)
        self.buttonY = 220
        self.newButton.setGeometry(QtCore.QRect(280, self.buttonY, 131, 131))
        self.newButton.setText("")
        self.newButton.setIcon(QtGui.QIcon("../question mark.png"))
        self.newButton.setObjectName("newButton")
        self.newButton.clicked.connect(self.openAddPicturesWindow)
        self.newButton.setIconSize(QtCore.QSize(120,110))
        self.arrayOfButtons.append(self.newButton)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 160, 221, 20))
        self.label_4.setObjectName("label_4")
        self.label_Num = 5
        self.button_Num = 3

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.widget = Form

        self.Window = QtWidgets.QWidget()
        self.ui =  addPictures_Form()
        self.analysisForm = Analysis_Form()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Add faces to lookout for"))
        self.label_2.setText(_translate("Form", "note: adding more than one of the same persons face will generate \n"
"more accurate results"))
        self.pushButton.setText(_translate("Form", "Analyze"))
        self.label_4.setText(_translate("Form", "Click the question mark to add a face"))
