import glob as gb
import cv2
fps = 25
img_path = gb.glob('C:/Users/Five/Documents/Bandicam/pictures/*.jpg')
file_path = r'C:/Users/Five/Documents/Bandicam/Video/dota2.mp4'
videoWriter = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (1920, 1280))

for pic in img_path:
    img = cv2.imread(pic)
    videoWriter.write(img)
videoWriter.release()