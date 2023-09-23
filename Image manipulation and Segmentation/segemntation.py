import cv2

img = cv2.imread('./sample.jpg')

#Converting Image to grayscale and then Binary
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,bw = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

#finding contours
contours, _ = cv2.findContours(bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
marked = img.copy()

# Filter contours by area to keep only the largest ones
min_contour_area = 1000
filtered_contours = [contour for contour in contours if cv2.contourArea(contour) >= min_contour_area]

#marking contours

for i,contour in enumerate(filtered_contours,0):
    cv2.drawContours(marked, contours, -1, (0,0,255), 2)
    cv2.putText(marked, str(i), tuple(contour[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)


#show images
cv2.imshow('Original Image ', img)
cv2.imshow('Marked Contours', marked)
cv2.waitKey(0)
cv2.destroyAllWindows()