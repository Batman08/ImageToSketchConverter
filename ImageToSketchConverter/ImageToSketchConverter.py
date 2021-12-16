import cv2

image_location = "C:/Users/asgha/Desktop/"
file_name = "test.jpg"

img = cv2.imread(image_location + file_name)

scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
image = (width, height)
  
# resize image
image = cv2.resize(img, image, interpolation = cv2.INTER_AREA)

# change image colour to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_gray_image = 255 - gray_image

# blur image
blurred_gray_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
inverted_blurred_gray_image = 255 - blurred_gray_image

# convert into pencil sketch
pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_gray_image, scale=256)

# display original and new image
cv2.imshow('Original Image', image)
cv2.imshow('New Image', pencil_sketch_image)
cv2.waitKey(0)