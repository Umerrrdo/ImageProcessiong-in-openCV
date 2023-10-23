import cv2
import numpy as np

img = cv2.imread('sample.jpg')
grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binaryImage = cv2.threshold(grayScale, 128, 255, cv2.THRESH_BINARY)
# Label objects using connected components analysis
n_objects, labels, stats, centroids = cv2.connectedComponentsWithStats(binaryImage, connectivity=8)
coloredImage = np.zeros_like(img)        # Create an output img

# Generate random colors for each object
colors = [tuple(np.random.randint(0, 255, 3).tolist()) for _ in range(n_objects)]

for label in range(1, n_objects):
    mask = labels == label
    coloredImage[mask] = colors[label]

cv2.imshow("Original Image", img)
cv2.imshow("Labeled Image", coloredImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
