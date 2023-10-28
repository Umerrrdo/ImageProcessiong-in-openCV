import cv2
import numpy as np


img = cv2.imread('sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binaryImage = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
labelEquivalence = {}
currLabel = 1


def find_root(label):
    if label not in labelEquivalence:
        labelEquivalence[label] = label
    if label != labelEquivalence[label]:
        labelEquivalence[label] = find_root(labelEquivalence[label])
    return labelEquivalence[label]


# First pass to label connected components
for i in range(1, binaryImage.shape[0] - 1):
    for j in range(1, binaryImage.shape[1] - 1):
        if binaryImage[i, j] != 0:
            neighbors = [binaryImage[i, j - 1], binaryImage[i - 1, j], binaryImage[i - 1, j - 1],
                         binaryImage[i - 1, j + 1]]
            neighbors = [x for x in neighbors if x != 0]
            if not neighbors:
                binaryImage[i, j] = currLabel
                currLabel += 1
            else:
                min_neighbor = min(neighbors)
                binaryImage[i, j] = min_neighbor
                for neighbor in neighbors:
                    if neighbor != min_neighbor:
                        labelEquivalence[neighbor] = min_neighbor

for i in range(1, binaryImage.shape[0] - 1):
    for j in range(1, binaryImage.shape[1] - 1):
        if binaryImage[i, j] != 0:
            binaryImage[i, j] = find_root(binaryImage[i, j])
color_dict = {}

coloredImage = np.zeros((binaryImage.shape[0], binaryImage.shape[1], 3), dtype=np.uint8)

for i in range(1, binaryImage.shape[0] - 1):
    for j in range(1, binaryImage.shape[1] - 1):
        label = binaryImage[i, j]
        if label != 0 and label not in color_dict:
            color_dict[label] = np.random.randint(0, 256, 3)  # Generate random colors

for i in range(1, binaryImage.shape[0] - 1):
    for j in range(1, binaryImage.shape[1] - 1):
        label = binaryImage[i, j]
        if label != 0:
            coloredImage[i, j] = color_dict[label]

# Display the labeled img and the colored result
cv2.imshow("Original Image", img)
cv2.imshow("Labelled Result", coloredImage)
cv2.waitKey(0)
cv2.destroyAllWindows()