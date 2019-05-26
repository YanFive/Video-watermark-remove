import cv2
img0 = cv2.imread('C:/Users/Five/Documents/Bandicam/pictures/00000002.jpg', 0)
ret, thresh = cv2.threshold(img0, 200, 255, cv2.THRESH_TOZERO)
cv2.imwrite('C:/Users/Five/Documents/Bandicam/mask/mask.jpg', thresh)
img = cv2.imread('C:/Users/Five/Documents/Bandicam/pictures/00000002.jpg')
mask = cv2.imread('C:/Users/Five/Documents/Bandicam/mask/mask1.jpg', 0)

cv2.imshow('img', img)
cv2.imshow('mask', mask)

#dst1 = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
#cv2.imshow('1', dst1)

dst2 = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
cv2.imshow('2', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()