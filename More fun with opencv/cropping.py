import cv2

img = cv2.imread("cat.jpg")

height, width = img.shape[:2]

topLeft = img[:height//2, :width//2]
topRight = img[:height//2, width//2:]
bottomLeft = img[height//2:, :width//2]
bottomRight = img[height//2:, width//2:]

cv2.imshow("Top Left", topLeft)
cv2.imshow("Top Right", topRight)
cv2.imshow("Bottom Left", bottomLeft)
cv2.imshow("Bottom Right", bottomRight)
cv2.waitKey(0)
cv2.destroyAllWindows()
