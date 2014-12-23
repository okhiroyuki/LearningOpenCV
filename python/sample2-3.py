import cv2
import sys


file = "/Users/okhiroyuki/Documents/python/avi/dfs.avi"
updatalock = False
windowname = "Example3"
trackbarname = "Position"

cv2.namedWindow(windowname,cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(file)

def onTrackbarSlide(pos):
	updatalock = True
	cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos)
	undatalock = False

frames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))

if frames > 0:
	cv2.createTrackbar(
		trackbarname,
		windowname,
		0,
		frames,
		onTrackbarSlide)

while True:
	if updatalock:
		continue

	ret, frame = cap.read()

	if ret:
		cv2.imshow(windowname,frame)
		curpos = int(cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES))
		cv2.setTrackbarPos(trackbarname,windowname,curpos)
		c = cv2.waitKey(1)
		if c == 27 :	#ESC key
			break

video_capture.release()
cv2.destroyAllWindow(windowname)