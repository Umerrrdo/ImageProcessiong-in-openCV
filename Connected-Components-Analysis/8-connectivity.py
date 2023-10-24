import cv2
import numpy as np


img = cv2.imread('sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binImage = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
labelEquivalence = {}
currLabel = 1

# Define 8-connectivity neighbors
neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1)]


def find_root(label):
    if label not in labelEquivalence:
        labelEquivalence[label] = label
    if label != labelEquivalence[label]:
        labelEquivalence[label] = find_root(labelEquivalence[label])
    return labelEquivalence[label]


# First pass to label connected components with 8-connectivity
for i in range(1, binImage.shape[0] - 1):
    for j in range(1, binImage.shape[1] - 1):
        if binImage[i, j] != 0:
            neighbors_labels = [binImage[i + dx, j + dy] for dx, dy in neighbors]
            neighbors_labels = [x for x in neighbors_labels if x != 0]
            if not neighbors_labels:
                binImage[i, j] = currLabel
                currLabel += 1
            else:
                min_neighbor = min(neighbors_labels)
                binImage[i, j] = min_neighbor
                for neighbor in neighbors_labels:
                    if neighbor != min_neighbor:
                        labelEquivalence[neighbor] = min_neighbor

for i in range(1, binImage.shape[0] - 1):
    for j in range(1, binImage.shape[1] - 1):
        if binImage[i, j] != 0:
            binImage[i, j] = find_root(binImage[i, j])
colorDic = {}

coloredImage = np.zeros((binImage.shape[0], binImage.shape[1], 3), dtype=np.uint8)

for i in range(1, binImage.shape[0] - 1):
    for j in range(1, binImage.shape[1] - 1):
        label = binImage[i, j]
        if label != 0 and label not in colorDic:
            colorDic[label] = np.random.randint(0, 256, 3)  # Generate random colors

for i in range(1, binImage.shape[0] - 1):
    for j in range(1, binImage.shape[1] - 1):
        label = binImage[i, j]
        if label != 0:
            coloredImage[i, j] = colorDic[label]

# Display the original img and the colored result
cv2.imshow("Original Image", img)
cv2.imshow("Colored Result", coloredImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
