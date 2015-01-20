import cv2
import numpy as np

if __name__ == '__main__':
	threshold = 255
	threshold_type = cv2.THRESH_BINARY_INV
	adaptive_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
	block_size = 11
	offset = 2
	ll = './image/OpticalFlow0.jpg'
	img = cv2.imread(ll)
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	ret,It = cv2.threshold(img_gray,240,255,threshold_type)
	Iat = cv2.adaptiveThreshold(img_gray,threshold,adaptive_method,threshold_type,block_size,offset)

	cv2.namedWindow("RAW",1)
	cv2.namedWindow("Threshold",1)
	cv2.namedWindow("Adaptive Threshold",1)

	cv2.imshow("RAW",img)
	cv2.imshow("Threshold",It)
	cv2.imshow("Adaptive Threshold",Iat)

	while True:
		c = cv2.waitKey(0)
		if c == 27:
			break

	cv2.destroyAllWindows()
