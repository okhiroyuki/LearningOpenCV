import cv2
import sys
import numpy as np


windowname_in = "Example-in"
windowname_out = "Example-out"

ll = '/Users/okhiroyuki/Documents/python/image/Aerial.bmp'
img = cv2.imread(ll)

def doCanny(img,lowThresh,highThresh,aperture):
	width,height,channel = img.shape

	size = width,height,1
	out = np.zeros(size,dtype=np.uint8)
	out = cv2.Canny(img,lowThresh,highThresh,aperture)
	return out

def doPyrDown(img):
	width,height,channel = img.shape
	assert width%2 == 0 and height%2 == 0 , "error"

	size = width/2,height/2,channel
	out = np.zeros(size,dtype=np.uint8)
	cv2.pyrDown(img,out)
	return out

out = doPyrDown(img)
out = doPyrDown(out)
out = doCanny(out,0,500,3)	
cv2.imshow(windowname_in,img)
cv2.imshow(windowname_out,out)

cv2.waitKey(0)
cv2.destroyAllwindow()