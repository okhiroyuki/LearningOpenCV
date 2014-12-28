import cv2

g_switch_value = 0
namedWindows = "Demo Window"


def switch_callback(position):
	if position == 0:
		print "switch on"
	else:
		print "switch off"


cv2.namedWindow(namedWindows,1)

cv2.createTrackbar("Switch",namedWindows,g_switch_value,1,switch_callback)

while True:
	c = cv2.waitKey(15)
	if c == 27:
		break

