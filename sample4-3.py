import cv2

filename = "./avi/dfs_out.mp4"

movie = cv2.VideoCapture(filename)
print movie.get(cv2.cv.CV_CAP_PROP_FOURCC)
