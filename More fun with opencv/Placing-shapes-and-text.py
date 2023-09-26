import cv2
import numpy as np

image = cv2.imread('cat.jpg')

line_color = (0, 0, 255)
rectangle_color = (0, 255, 0)
circle_color = (255, 0, 0)
text_color = (255, 255, 255)

cv2.line(image, (50, 50), (200, 50), line_color, 2)

cv2.rectangle(image, (100, 100), (250, 250), rectangle_color, 2)

cv2.circle(image, (150, 150), 50, circle_color, 2)

text = "Umer"
cv2.putText(image, text, (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)

cv2.imshow('Image with Shapes and Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
