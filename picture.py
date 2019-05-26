import glob as gb
import cv2
img_path = gb.glob('C:/Users/Five/Documents/Bandicam/pictures/*.jpg')
i = 1
for pic in img_path:
    img = cv2.imread(pic, cv2.IMREAD_UNCHANGED)
    cv2.imshow('Image', img)
    k = cv2.waitKey(0)
    if k == ord('q'):
        break
    i = i+1
