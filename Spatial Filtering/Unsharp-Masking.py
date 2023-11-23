import cv2
import numpy as np

# Read the img
# Read the img
image = cv2.imread('two_cats.jpg')

# Convert the img to grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the Sobel filter for horizontal edges
horizontalSobel = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Define the Sobel filter for vertical edges
verticalSobel = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert the result matrices to absolute values
horizontalSobel = np.abs(horizontalSobel)
verticalSobel = np.abs(verticalSobel)

# Add the horizontal and vertical edge matrices
edge = cv2.add(horizontalSobel, verticalSobel)

# Normalize the result for display
edge = cv2.normalize(edge, None, 0, 255, cv2.NORM_MINMAX)

# Convert to uint8 for proper display
edge = np.uint8(edge)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Horizontal Edges', horizontalSobel)
cv2.imshow('Vertical Edges', verticalSobel)
cv2.imshow('Combined Edges', edge)

cv2.waitKey(0)
cv2.destroyAllWindows()
