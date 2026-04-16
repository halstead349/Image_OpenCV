import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna']
DIR = r'C:\Users\halstead_rideriver\Documents\Image_OpenCV\Faces\train'

haar = cv.CascadeClassifier('haar_face.xml')
features = []
labels= []

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            
            faces_rect = haar.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
                
create_train()

# print(f'len of features {len(features)}')
# print(f'Len of labels {len(labels)}')

features = np.array(features,dtype='object')
labels = np.array(labels)
face_recog = cv.face.LBPHFaceRecognizer.create()

# Train the recognizer on the feature list and labels list
face_recog.train(features,labels)
face_recog.save('face_training.yml')


np.save('features.npy',features)
np.save('labels.npy',labels)
    