import cv2
import sys
import numpy as np

box = [0,0,0,0]	#x,y,width,height
windowName = "Box Example"
drawing_box = False

def draw_box(img,box):
	cv2.rectangle(img,(box[0],box[1]),(box[0]+box[2],box[1]+box[3]),(255,0,0))

def onMouse(event,x,y,flags,param):
	global drawing_box
	global box
	if event == cv2.EVENT_MOUSEMOVE:
		if drawing_box:
			box[2] = x-box[0]
			box[3] = x-box[1]

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing_box = True
		box = [0,0,0,0]

	if event == cv2.EVENT_LBUTTONUP:
		drawing_box = False
		if box[2] < 0:
			box[0] += box[2]
			box[2] *= -1
		if box[3] < 0:
			box[1] += box[3]
			box[3] *= -1
		draw_box(img,box)

img = np.zeros((200,200,3),np.uint8)
temp = img.copy()
cv2.namedWindow(windowName,cv2.WINDOW_AUTOSIZE)

cv2.setMouseCallback(windowName,onMouse)

while True:
	temp = img.copy()
	if drawing_box:
		draw_box(temp,box)
	cv2.imshow(windowName,temp)
	c = cv2.waitKey(15)
	if c == 27:
		break

cv2.destroyAllWindows()