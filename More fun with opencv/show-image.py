import cv2

img1 = cv2.imread("zoro.jpeg")
img2 = cv2.imread("zenitsu.jpeg")
img3 = cv2.imread("levi.jpeg")

cv2.imshow("Zoro", img1)
cv2.imshow("Zenitsu", img2)
cv2.imshow("Levi", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
