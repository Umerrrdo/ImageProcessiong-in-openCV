import cv2

originalImg = cv2.imread('img/wiki.jpg',0)

#Create an algorithm which applies contrast stretching to an image

def contrastStretching(img):
    # Create a new image
    new_img = img.copy()
    # Find the minimum and maximum pixel values in the image
    img_min = img.min()
    img_max = img.max()
    # Apply the formula to each pixel
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            new_img[i, j] = (img[i, j] - img_min) * (255 / (img_max - img_min))
            # print(new_img[i, j]," ",img[i, j])
    return new_img

#Apply the algorithm to the image
newImg = contrastStretching(originalImg)

#Applying the algorithm to "lowcon.tif"

lowcon = cv2.imread('img/lowcon.tif',0)
newLowcon = contrastStretching(lowcon)

#Displaying the images

cv2.imshow('Wiki Original', originalImg)
cv2.imshow('Wiki Contrast Stretched', newImg)
cv2.imshow('Lowcon Original', lowcon)
cv2.imshow('Lowcon Contrast Stretched', newLowcon)
cv2.waitKey(0)
cv2.destroyAllWindows()