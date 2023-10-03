import cv2
import numpy as np

# Load the image
image = cv2.imread('img/persp.jpg')

# Define the four corners of the quadrilateral
quad_pts = np.array([[35, 18], [284, 62], [218, 548], [399, 392]], dtype='float32')

# Define the four corners of the desired output rectangle (3:4 aspect ratio)
rect_pts = np.array([[0, 0], [420, 0], [0, 560], [420, 560]], dtype='float32')

# Compute the perspective transform matrix
matrix = cv2.getPerspectiveTransform(quad_pts, rect_pts)

# Apply the perspective transformation
result = cv2.warpPerspective(image, matrix, (420, 560))

# Display the result
cv2.imshow('Perspective Transformation', result)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
