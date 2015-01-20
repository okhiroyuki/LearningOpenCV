import cv2
import numpy as np
import sys

if __name__ == '__main__':

	ll = './image/stuff.jpg'
	img = cv2.imread(ll)
	cimg = cv2.imread(ll,0)	#gray scale
	blur = cv2.GaussianBlur(cimg, (0,0), 1)

	circles = cv2.HoughCircles(blur,cv2.cv.CV_HOUGH_GRADIENT,2,500,param1=100,param2=30,minRadius=5,maxRadius=20)
	if circles is not None:
		for i in circles[0,:]:
			cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)  # draw the outer circle
			cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)     # draw the center of the circle

		cv2.imshow('detected circles',cimg)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	else:
		print "no circles"
