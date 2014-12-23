import cv2
import sys

video_file = "/Users/okhiroyuki/Documents/python/avi/fp.avi"

cv2.namedWindow("Example2",cv2.WINDOW_AUTOSIZE)
video_capture = cv2.VideoCapture(video_file)

while True:
	is_successfully_read, img = video_capture.read()
	
	if is_successfully_read:
		cv2.imshow("Example2",img)
		c = cv2.waitKey(1)
		if c == 27 :	#ESC key
			break

video_capture.release()
cv2.destroyWindow("Example2")