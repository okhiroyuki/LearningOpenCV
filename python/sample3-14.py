import cv2
import numpy as np
import sys


if __name__ == '__main__':

	ll1 = './image/adrian.jpg'
	ll2 = './image/faceTemplate.jpg'
	img1=cv2.imread(ll1, 1)
	img2=cv2.imread(ll2, 1)

	height,width,channles = img2.shape

	size1 = img1.shape
	sx = size1[1]/2 - width/2
	sy = size1[0]/2 - height/2
	ex = size1[1]/2 + width/2
	ey = size1[0]/2 + height/2
	roi1 = img1[sy:ey,sx:ex]
	roi2 = img2[0:height,0:width]
	img1[sy:ey,sx:ex] = cv2.addWeighted(roi1,0.3,roi2,0.3,0)

	cv2.imshow('roi image',img1)
	cv2.waitKey(0)
	cv2.destroyAllWindows()