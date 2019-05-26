import cv2
import numpy as np
img = cv2.imread('C:/Users/Five/Documents/Bandicam/pictures/00000002.jpg', 0)
ret, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO)
#cv2.imshow('Image', thresh)
cv2.imwrite('C:/Users/Five/Documents/Bandicam/mask/mask.jpg', thresh)
cv2.waitKey()
