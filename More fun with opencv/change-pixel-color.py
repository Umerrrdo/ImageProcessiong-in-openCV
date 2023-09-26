import cv2
import numpy as np

image = cv2.imread('cat.jpg')
height, width = image.shape[:2]

result = image.copy()

# Set the line colors and gap width
green = (0, 255, 0)
white = (255, 255, 255)
thickness = 1
gap = 1

# Initialize a flag to alternate between green and white lines
is_green_line = True

# Loop through each row of pixels
for y in range(0, height, thickness + gap):
    if is_green_line:
        # Set the current row to green
        result[y:y + thickness, :, :] = green
    else:
        # Set the current row to white
        result[y:y + thickness, :, :] = white
    is_green_line = not is_green_line

cv2.imshow('Image with Alternating Lines', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
