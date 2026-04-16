import cv2 as cv
import numpy as np
# # read the image 
# image = cv.imread("C:/Users/halstead_rideriver/Pictures/Screenshots/Screenshot 2026-01-23 111246.png")
# cv.imshow('ICON',image)

# draw on images:

# blank_img = np.zeros((500,500,3),dtype='uint8') # create a blank image.(500 : height,500: width, 3 : color sections(rgb) )
# # blank_img[0:500, 0:100] =0,255,0 # painting a particular area [row_start:row_end, col_start:col_end]

# # cv.rectangle(blank_img,(0,0),(250,300),(0,255,0),thickness=cv.FILLED) # drawing a rectangle => (img,x-point,y-point,color,thickness(-1 or cv.FILLED=> filles in the color))
# #cv.circle(blank_img,(250,250),50,(0,0,255),thickness=2)
# # cv.circle(blank_img,(blank_img.shape[1]//2,blank_img.shape[0]//2),50,(0,0,255),thickness=2)
# # print(blank_img.shape[0]//3)
# # cv.putText(blank_img,"Hi,Welcome...",(10,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2) # create text.
# cv.imshow('Blank',blank_img)

# 5 Essential functions:
img = cv.imread("C:/Users/halstead_rideriver/Pictures/Screenshots/Screenshot 2026-01-23 111246.png")
# 1) Grey image:
# img_grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('GreyImage',img_grey)

# 2) blur:
# blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("BLURR",blur)

# 3) Edge detection or cascading: (using Canny method) , we can use blur images to get less edges detection.
# edge = cv.Canny(img,125,175)
# cv.imshow("",edge)

# 4) Dilate:
# dilate = cv.dilate(edge,(7,7),iterations=7)
#cv.imshow("dilate",dilate)

#5) Erode:
# eroded = cv.erode(dilate,(3,3),iterations=5)
# cv.imshow("erode",eroded)

# resize function:
# resize = cv.resize(img,(250,250),interpolation=cv.INTER_AREA)
# cv.imshow("resized",resize)

# crop: [row_start:row_end, col_start:col_end]
# crop = img[0:300,0:400]
# cv.imshow("cropped",crop)


#--------------------------- Image Transformation--------------------------------

# Image Translation: -> shifting image along x or y axis:

# def translate(img,x,y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMat,dimensions)
# '''
# +x --> right
# +y --> down
# -x --> left
# -y -->up
# '''
# translated = translate(img,100,100)
# cv.imshow("Translated",translated)
'''
An affine transformation is a way to manipulate, move, or reshape an object (like an image or 2D shape) while keeping parallel
lines parallel. It combines basic movements—rotating, scaling (resizing), shearing (slanting), and translating (moving)—into one 
step. It changes the position and shape but maintains the overall structure, often using a matrix to calculate the new coordinates.
'''
# Image rotation :

# def rotation(img,angle : int,rotpoint=None):
#     (height,width) = img.shape[:2]
#     if rotpoint == None:
#         rotpoint = (width //2, height // 2)
        
#     rotMat = cv.getRotationMatrix2D(rotpoint,angle,1.0)
#     dimensions = (width,height)
#     return cv.warpAffine(img,rotMat,dimensions)

# rotated = rotation(img,45)  # imges rotates 45 deg towards left . 
# cv.imshow("Image_Rotated",rotated) 

# flipping an image:
# flip = cv.flip(img,-1) # -1 flips image to 180 deg.
# cv.imshow("flip",flip)

# ----------------Contours detection - Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. 
# The contours are a useful tool for shape analysis and object detection and recognition.
# blank = np.zeros(img.shape,dtype='uint8')
# grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# # blurr = cv.GaussianBlur(grey,(7,7),cv.BORDER_DEFAULT)
# # canny = cv.Canny(grey,125,175)
# ret,thresh = cv.threshold(grey,125,255,cv.THRESH_BINARY) # threshold should be used after grey imaging.
# contours,heirarchy = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# print(len(contours))
# cv.drawContours(blank,contours,-1,(0,0,255),thickness=2)
# cv.imshow("Blank",blank)
# cv.imshow("Contours",thresh)

#--------------------------Color spaces  : System to represent pixels in an image eg: rgb, HSV,--------------------
# grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # gry scaling.
#hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV) # hsv color code
#lab = cv.cvtColor(img,cv.COLOR_BGR2LAB) # L.A.B color code
# rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow("IMAGE",rgb)

#----------------------------color channels : splitting the colors and displaying-----------------------
#b,g,r= cv.split(img)
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)
# cv.imshow(".",img)
# merged = cv.merge([b,g,r]) # to merge the splited color images.
# cv.imshow("Merged",merged)
# reproducing the colors specified in an image according like blue , green , red . 
# blank = np.zeros(img.shape[:2],dtype='uint8')
# blue = cv.merge([b,blank,blank])
# green = cv.merge([blank,g,blank])
# red = cv.merge([blank,blank,r])
# cv.imshow("blue",blue)
# cv.imshow("green",green)
# cv.imshow("red",red)

# ---------------------------------------Blurring techniques------------------------------------
# kernel is small matrix of pixels used to perform blurring , sharpening and edge detection using convolution calculation.
# blurr is applied to a middle pixel in a kernel which affect the surrounding pixels in that kernel window.

# Average : the cumputation of the middle concentrated pixel is the average of the intersity of the neighbor pixels.
# average = cv.blur(img,(3,3))
# cv.imshow("blurr",average)
# cv.imshow("OG",img)

# # Gaussian blur : little lesser blurring than average blurring.
# gauss = cv.GaussianBlur(img,(7,7),0)
# cv.imshow("Gauss",gauss)

# # median blur:
# median = cv.medianBlur(img,7)
# cv.imshow("Median",median) 

# # Bilateral blurring : retains the edges of the image even after applying blurr.
# bilateral = cv.bilateralFilter(img,5,15,15)
# cv.imshow("Bilateral",bilateral)

# -------------------------BITWISE OPERATORS---------------------------

#blank = np.zeros((400,400),dtype='uint8')
# rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
# circle = cv.circle(blank.copy(),(200,200),200,255,-1)

# AND: Returns intersection of two images.
# bit_and = cv.bitwise_and(rectangle,circle)
# cv.imshow("AND",bit_and)

# OR : returns both intersecting and non-intersecting areas as image.
# bit_or = cv.bitwise_or(rectangle,circle)
# cv.imshow("OR",bit_or)

# XOR : return non-intersecting regions
# bit_xor = cv.bitwise_xor(rectangle,circle)
# cv.imshow("XOR",bit_xor)

# NOT : inverts the image or contrast the image.
# bit_not = cv.bitwise_not(circle)
# cv.imshow("not",bit_not)

# ----------- MASKING : Focuses on specific region of an image.--------------------------------
# blank = np.zeros(img.shape[:2],dtype='uint8')
# mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1) # we can also use rectangle or any other shapes as per out combo for masking.

# masked = cv.bitwise_and(img,img,mask=mask)
# cv.imshow("MASKED",masked)

# ------------------HISTOGRAMS: allows us to visualize the pixel intensity of the pixel distribution in an image.
# import matplotlib.


# ------------------------Thresholding an image---------------------
# Converting an image to binary image.(1,0 or 255 )
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY",gray)

# simple thresholding:
# threshold , thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
# cv.imshow("SIMPLE_THRESH",thresh)

# threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) # Inversion of the binary image.
# cv.imshow("INV_Thershold",thresh_inv)

# Adaptive Thresholding : lets the computer decide the threshold values.
# adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
# cv.imshow("adaptive_thresh",adaptive_thresh)

#Gradients : Gradients measure change strength/direction, while edge detection uses these measurements to create a binary map of object boundaries. 
# Laplacian method: 
#convert first the image in gray.
# lap = cv.Laplacian(gray,cv.CV_64F)
# lap = np.uint8(np.absolute(lap))
# cv.imshow("laplacian",lap)

# sobel gradient detection. : focuses on grandients along side the axis directions be it x or y.

# sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
# sobely = cv.Sobel(gray,cv.CV_64F,0,1)
# combined_sobel = cv.bitwise_or(sobelx,sobely)
# cv.imshow("SobelX",sobelx)
# cv.imshow("sobely", sobely)
# cv.imshow("Combined",combined_sobel)

#Canny edge detection :
# can = cv.Canny(gray,150,175)
# cv.imshow("Canny", can)





cv.waitKey(0)
