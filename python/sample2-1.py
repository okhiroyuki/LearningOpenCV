import sys
import cv2

ll = '/Users/okhiroyuki/Documents/python/image/Aerial.bmp'
img = cv2.imread(ll)
cv2.namedWindow("Example1",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Example1",img)
cv2.waitKey(0)
cv2.destroywindow("Example1")