import cv2
import sys
import numpy as np

windowname_in = "Example-in"
windowname_out = "Example-out"

ll = '/Users/okhiroyuki/Documents/python/image/Aerial.bmp'
img = cv2.imread(ll)

def doPyrDown(img):
	width,height,channel = img.shape
	assert width%2 == 0 and height%2 == 0 , "error"

	size = width/2,height/2,channel
	out = np.zeros(size,dtype=np.uint8)
	cv2.pyrDown(img,out)
	return out

out = doPyrDown(img)
cv2.imshow(windowname_in,img)
cv2.imshow(windowname_out,out)

cv2.waitKey(0)
cv2.destroyAllwindow()