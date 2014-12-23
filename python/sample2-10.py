import cv2
import sys
import numpy as np

file1 = "/Users/okhiroyuki/Documents/python/avi/dfs.avi"
file2 = "/Users/okhiroyuki/Documents/python/avi/dfs_out.mp4"


cv2.namedWindow("Example",cv2.WINDOW_AUTOSIZE)
capture = cv2.VideoCapture(file1)
assert capture != None

fps = capture.get(cv2.cv.CV_CAP_PROP_FPS)
width = capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
size = (int(width),int(height))

out = cv2.VideoWriter(file2,cv2.cv.CV_FOURCC('m','p','4','v'),fps,size)

while (capture.isOpened()):
	ret, frame = capture.read()
	if ret == False:
		break

	out.write(frame)
	cv2.imshow("frame",frame)

	c = cv2.waitKey(1)
	if c == 27: #ESC
		break

capture.release()
out.release()
cv2.destroyAllWindows()