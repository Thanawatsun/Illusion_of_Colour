import cv2
import numpy as np

img = cv2.imread('pictures/room-1-with-obj.png')

#Green chair in room 1
lower = np.array([0, 50, 0])
upper = np.array([10, 255, 255])

mask = cv2.inRange(img, lower, upper)

res = cv2.bitwise_and(img, img, mask= mask)

cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()