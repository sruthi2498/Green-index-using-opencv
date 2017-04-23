from __future__ import division
import cv
import cv2
import sys
import numpy as np
import copy

#sys.path.append('/usr/local/lib/python2.7/site-packages')

BLUE = [255,0,0]

if len(sys.argv) < 2:
	print "Usage: ", sys.argv[0], " <image filename>"
	sys.exit()

def cv_size(img):
    return tuple(img.shape[1::-1])
# Load image and split into RGB planes
image = cv2.imread(sys.argv[1])
print "Loaded"
size=cv_size(image)
print "size : ",size
area=size[0]*size[1]
print "area : ",area


#Total number of pixels
Total_Number_Of_Pixels=image.size
print "Total number of pixels : ",image.size

#making a border
image= cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)


GREEN_MIN = np.array([0, 25, 0], np.uint8)
GREEN_MAX = np.array([173, 255,154], np.uint8)

#CREATING A MASK
#JUST TO SHOW GREEN AREAS
mask = cv2.inRange(image, GREEN_MIN, GREEN_MAX)
output = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("masked image",output);
cv2.waitKey(0)


#REMOVES ALL COLORS EXCEPT GREEN
dst = cv2.inRange(image, GREEN_MIN, GREEN_MAX)
cv2.imshow("new image",dst);
cv2.waitKey(0)
Number_Of_Green_Pixels = cv2.countNonZero(dst)

print('The number of green pixels is: ' + str(Number_Of_Green_Pixels))

Index=Number_Of_Green_Pixels/Total_Number_Of_Pixels
print "Index: ",Index


