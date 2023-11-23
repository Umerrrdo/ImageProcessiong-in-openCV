import cv2
import numpy as np

# Read the img
img = cv2.imread('a.png')

# Convert the img to grayscale
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define the 3x3, 5x5, 15x15, and 35x35 averaging filters
filter3x3 = np.ones((3, 3), np.float32) / 9
filter5x5 = np.ones((5, 5), np.float32) / 25
filter15x15 = np.ones((15, 15), np.float32) / 225
filter35x35 = np.ones((35, 35), np.float32) / 1225

# Apply the filters using OpenCV's filter2D function
result_3x3 = cv2.filter2D(grayImage, -1, filter3x3)
result_5x5 = cv2.filter2D(grayImage, -1, filter5x5)
result_15x15 = cv2.filter2D(grayImage, -1, filter15x15)
result_35x35 = cv2.filter2D(grayImage, -1, filter35x35)

# Define the weighted averaging filter
weightedFilter = np.array([[1, 2, 1],
                            [2, 4, 2],
                            [1, 2, 1]], dtype=np.float32) / 16

# Apply the weighted filter
resultWeighted = cv2.filter2D(grayImage, -1, weightedFilter)

#Diamond averaging filter
diamond_filter = np.array([[0, 1, 0],
                            [1, 1, 1],
                            [0, 1, 0]], dtype=np.float32) / 5

# Apply the diamond filter
resultDiamond = cv2.filter2D(grayImage, -1, diamond_filter)

#7x7 averaging filter
sevenFilter = np.ones((7, 7), np.float32) / 49

# Apply the 7x7 filter
resultSeven = cv2.filter2D(grayImage, -1, sevenFilter)

# Display the result
cv2.imshow('Original Image', grayImage)
cv2.imshow('Weighted Averaging', resultWeighted)
cv2.imshow('Diamond Averaging', resultDiamond)
cv2.imshow('7x7 Averaging', resultSeven)

# # Display the results
cv2.imshow('Original Image', grayImage)
cv2.imshow('3x3 Averaging', result_3x3)
cv2.imshow('5x5 Averaging', result_5x5)
cv2.imshow('15x15 Averaging', result_15x15)
cv2.imshow('35x35 Averaging', result_35x35)

cv2.waitKey(0)
cv2.destroyAllWindows()
