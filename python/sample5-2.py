import cv2
import numpy as np

def sum_rgb(src):
	b,g,r = cv2.split(src)

	s = np.zeros(src.shape,dtype=np.uint8)
	dst = np.zeros(src.shape, dtype=np.uint8)
	s = cv2.addWeighted(r, 1./3., g, 1./3., 0.0)
	s = cv2.addWeighted(s, 2./3., b, 1./3., 0.0)
	
	ret, dst = cv2.threshold(s, 100, 100, cv2.THRESH_TRUNC)
	return dst

if __name__ == '__main__':
	namedwindow = "example"
	ll = './image/OpticalFlow0.jpg'

	cv2.namedWindow(namedwindow,1)

	src = cv2.imread(ll)
	dst = sum_rgb(src)

	cv2.imshow(namedwindow,dst)

	while True:
		c = cv2.waitKey(10)
		if c == 27:
			break

	cv2.destroyAllWindow()
