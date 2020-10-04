from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import time
import face_recognition

from face_recognition import api 


class videoAnalysis(object):

    def getEncodings(self, images):
        encodings = []

        for i in range(0, len(images)):
            images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(images[i])
            if(len(face_locations) > 0):
                    top, right, bottom, left = face_locations[0]
                    pic = cv2.rectangle(images[i], (left-2,top-2), (right+2,bottom+2), color, thickness)
                    images[i] = pic[top:bottom, left:right]
                    height, width, _ = images[i].shape
                    fl = (0, width, height,0)
                    encode = face_recognition.face_encodings(images[i],[fl],num_jitters=0,model="small")[0]
                    encodings.append(encode) 
        
        return encodings

    def isFace(self, known_encodings, encoding):
        average = 0
        results = face_recognition.face_distance(known_encodings, encoding)
        for result in results:
            if(result < .55):
                average = 0
            average += result
        average /= len(results)
        if(average < .63):
            return True
        return False

    def setUpLoading(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 150)
        self.loadingLabel = QtWidgets.QLabel(Form)
        self.loadingLabel.setGeometry(QtCore.QRect(85, 50, 100, 100))
        self.loadingLabel.setText(" 0 % ")

        self.titleLabel = QtWidgets.QLabel(Form)
        self.titleLabel.setGeometry(QtCore.QRect(40, 0, 150, 50))
        self.titleLabel.setText(" Analyzing Video . . . ")
        QtWidgets.QApplication.processEvents()  

    def analyzeVideo(self, video, arrayOfFaces):

        stats = [0] * len(arrayOfFaces)
        vidcap = cv2.VideoCapture(video)  #40001

        total = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = vidcap.get(cv2.CAP_PROP_FPS) 
        duration = total/fps
        
        '''
        print('fps = ' + str(fps))
        print('number of frames = ' + str(total))
        print('duration (S) = ' + str(duration))
        minutes = int(duration/60)
        seconds = duration%60
        print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))
        '''
        num = 0

        start = time.time()
        while (num/1000) < duration-1:
            vidcap.set(cv2.CAP_PROP_POS_MSEC,num)
            success,image = vidcap.read()
            face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0)
            for face_loc in face_locations:
                top, right, bottom, left = face_loc
                face_image = image[top:bottom, left:right] 
                height, width, _ = face_image.shape
                fl = (0, width, height,0)
                encoded_face = face_recognition.face_encodings(face_image, [fl], num_jitters=0)[0]


                for i in range(0, len(arrayOfFaces)):
                    encodings = arrayOfFaces[i]
                    #print("Face # " + str(i))
                    if(self.isFace(encodings, encoded_face)):
                        stats[i] += 1
                '''cv2.imshow(str(num),image)
                cv2.waitKey(0)
                cv2.destroyWindow(str(num))'''
            num += 1000
            percent = int(int((num/1000) * 100) / int(duration) )
            percentString = str(percent)
            self.loadingLabel.setText( percentString + " % ")
            QtWidgets.QApplication.processEvents()
              
        return stats

    

    