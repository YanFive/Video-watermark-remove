import cv2
import os
import glob as gb
#视频解码
cap = cv2.VideoCapture("C:/Users/Five/Documents/Bandicam/example.avi")
frame_count = 0
success = cap.isOpened()
while(success):
    frame_count +=1
    success, frame = cap.read()
    if success:
        cv2.imwrite("C:/Users/Five/Documents/Bandicam/pictures/"+str(frame_count).zfill(8)+".jpg", frame)
        cv2.waitKey(1)
    else:
        break
#循环读取图片去水印
img_path = gb.glob('C:/Users/Five/Documents/Bandicam/pictures/*.jpg')
i = 1
for pic in img_path:
    img = cv2.imread(pic, cv2.IMREAD_UNCHANGED)
    cv2.imshow('Image', img)
    k = cv2.waitKey(0)
    if k == ord('q'):
        break
    i = i+1
cap.release()
cv2.destroyAllWindows()
