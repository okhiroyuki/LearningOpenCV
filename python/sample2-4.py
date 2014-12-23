import cv2
import sys
import numpy as np

windowname_in = "Example-in"
windowname_out = "Example-out"

ll = '/Users/okhiroyuki/Documents/python/image/Aerial.bmp'
img = cv2.imread(ll)
cv2.imshow(windowname_in,img)

out = np.zeros(img.shape,dtype=np.uint8)
out = cv2.GaussianBlur(img,(3,3),0)
cv2.imshow(windowname_out,out)

cv2.waitKey(0)
cv2.destroyAllwindow()