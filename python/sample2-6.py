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

out = doCanny(img,0,500,3)	
cv2.imshow(windowname_in,img)
cv2.imshow(windowname_out,out)

cv2.waitKey(0)
cv2.destroyAllwindow()