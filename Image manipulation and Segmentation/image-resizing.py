import cv2

img = cv2.imread('./sample.jpg')

# Desired dimensions
width = 256
height = 256

# Resize image
resized = cv2.resize(img, (width, height))

# Show resized image
cv2.imshow('Original image', img)
cv2.imshow('Resized image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
