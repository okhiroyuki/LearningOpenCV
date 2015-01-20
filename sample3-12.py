import cv2
import sys
import numpy as np

ll = './image/adrian.jpg'
img=cv2.imread(ll, 1)

size = img.shape
roiWidth = size[1]/4
roiHeight = size[0]/4
sx = size[1]/2 - roiWidth
sy = size[0]/2 - roiHeight
ex = size[1]/2 + roiWidth
ey = size[1]/2 + roiHeight

roi = img[sy:ey,sx:ex]
img[sy:ey,sx:ex] = cv2.add(roi,150)

cv2.imshow('roi image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()