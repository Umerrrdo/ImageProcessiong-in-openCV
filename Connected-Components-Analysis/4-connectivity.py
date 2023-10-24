import cv2
import numpy as np

img = cv2.imread('sample.jpg')
grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binaryImage = cv2.threshold(grayScale, 128, 255, cv2.THRESH_BINARY)
colorImage = np.zeros_like(img)

# Define 4-connectivity neighbors (top, bottom, left, right)
neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

counterLabel = 1
labelColorDic = {}

for i in range(binaryImage.shape[0]):
    for j in range(binaryImage.shape[1]):
        if binaryImage[i, j] == 255:
            connectedLabels = []

            # Check 4-connectivity neighbors for labels
            for dx, dy in neighbors:
                x, y = i + dx, j + dy
                if 0 <= x < binaryImage.shape[0] and 0 <= y < binaryImage.shape[1]:
                    neighbor_label = colorImage[x, y]
                    if neighbor_label.any():
                        connectedLabels.append(neighbor_label)

            # If no connected labels, assign a new label and color
            if not connectedLabels:
                uniqueColor = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
                labelColorDic[counterLabel] = uniqueColor
                labelColor = uniqueColor
                counterLabel += 1
            else:
                # Assign the pixel the color of the first connected neighbor
                labelColor = connectedLabels[0]

            colorImage[i, j] = labelColor

cv2.imshow("Original Image", img)
cv2.imshow("Labeled Image", colorImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
