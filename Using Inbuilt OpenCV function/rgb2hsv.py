import cv2
import numpy as np

# Load the image
image = cv2.imread('img/shapes.bmp')

# Convert the image to the HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the HSV ranges for each of the specified colors
color_ranges = [
    ((160, 100, 100), (179, 255, 255)),    # Red color range
    ((100, 100, 100), (130, 255, 255)), # Blue color range
    ((80, 100, 100), (100, 255, 255)),  # Cyan color range
    ((35, 100, 100), (85, 255, 255))    # Green color range
]

# Create a window for each color
windows = ['Red', 'Blue', 'Cyan', 'Green']

for i, (lower, upper) in enumerate(color_ranges):
    mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
    cv2.imshow(windows[i], mask)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
