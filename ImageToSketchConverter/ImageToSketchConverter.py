import cv2

img_location = "C:/Users/asgha/Desktop/"
file_name = "test.jpg"

img = cv2.imread(img_location + file_name)

cv2.imshow('Original Image', img)
cv2.waitKey(0)