import cv2
import numpy as np

# Load the image
image = cv2.imread('img/shapes.bmp')

# Convert the image to the HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the HSV ranges for each of the specified colors
color_ranges = [
    ((160, 100, 100), (179, 255, 255)),  # Red color range
    ((100, 100, 100), (130, 255, 255)),  # Blue color range
    ((80, 100, 100), (100, 255, 255)),  # Cyan color range (adjusted)
    ((35, 100, 100), (85, 255, 255))  # Green color range
]

# Define the window names
windows = ['Red', 'Blue', 'Cyan', 'Green']

# Define the color for the center points (yellow)
center_color = (0, 255, 255)

# Process each color range and display the result
for i, (lower, upper) in enumerate(color_ranges):
    mask = cv2.inRange(hsv, np.array(lower), np.array(upper))

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours to find and mark center points
    for contour in contours:
        # Calculate the center of mass (centroid) using the moments
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            # Draw a yellow circle at the center point
            cv2.circle(image, (cx, cy), 5, center_color, -1)  # -1 to fill the circle

# Show the image with center points marked
cv2.imshow('Shapes with Center Points', image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
