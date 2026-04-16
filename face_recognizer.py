import numpy as np
import cv2 as cv

haar = cv.CascadeClassifier('haar_face.xml')
people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna']
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recog = cv.face.LBPHFaceRecognizer.create()
face_recog.read('face_training.yml')

img = cv.imread(r'C:\Users\halstead_rideriver\Documents\Image_OpenCV\Faces\val\ben_afflek\3.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Detect the face ogf the image.
face_rect = haar.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in face_rect:
    person_roi = gray[y:y+h,x:x+h]
    
    label,confidence = face_recog.predict(person_roi)
    
    
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
cv.imshow('DETECTED FACE',img)

cv.waitKey(0)