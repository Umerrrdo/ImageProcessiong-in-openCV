import cv2

img = cv2.imread('./sample.jpg')

#convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#show images
cv2.imshow('Original image', img)
cv2.imshow('Grayscale image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()