import cv2

img = cv2.imread('./sample.jpg')

#converting to binary (black and white)image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,bw = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

#show images
cv2.imshow('Original Image ', img)
cv2.imshow('Binary Image', bw)
cv2.waitKey(0)
cv2.destroyAllWindows()

