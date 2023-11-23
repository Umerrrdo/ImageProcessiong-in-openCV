import cv2
import numpy as np

# Read the img
img = cv2.imread('a.png')

# Convert the img to grayscale
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian filter with σ = 1.4
sigma = 1.4
resultGaussian = cv2.GaussianBlur(grayImage, (0, 0), sigma)

#Apply Gaussian filter with higher sigma
sigma = 5
resultGaussian2 = cv2.GaussianBlur(grayImage, (0, 0), sigma)

#Apply Gaussian filter with lower sigma
sigma = 0.5
resultGaussian3 = cv2.GaussianBlur(grayImage, (0, 0), sigma)


# Display the result
cv2.imshow('Original Image', grayImage)
cv2.imshow('Gaussian Filter (σ = 1.4)', resultGaussian)
cv2.imshow('Gaussian Filter (σ = 5)', resultGaussian2)
cv2.imshow('Gaussian Filter (σ = 0.5)', resultGaussian3)


cv2.waitKey(0)
cv2.destroyAllWindows()
