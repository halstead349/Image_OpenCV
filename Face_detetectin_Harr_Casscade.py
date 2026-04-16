import cv2 as cv
import numpy as np

trump = cv.imread('trump.jpg')
trump = cv.resize(trump,(500,500),interpolation=cv.INTER_AREA)

# graying the image:
gray = cv.cvtColor(trump,cv.COLOR_BGR2GRAY)
# cv.imshow("trumpgrey",gray)

# implementing haar cascades starts:
haar = cv.CascadeClassifier('haar_face.xml')
face_rect = haar.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3) # the minNeighbors are more sensitive to noises in the image , so altering its value can give much precise recognitions.
print(f'Number of faces = {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(trump,(x,y),(x+w,y+h),(0,255,0),thickness=2) 
cv.imshow('rect', trump)

cv.waitKey(0)