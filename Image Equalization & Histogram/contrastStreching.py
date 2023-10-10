import cv2

originalImg = cv2.imread('img/wiki.jpg',0)

#Create an algorithm which applies contrast stretching to an image

def contrastStretching(img):
    #Create a new image
    newImg = img.copy()
    #Find the minimum and maximum pixel values in the image
    min = img.min()
    max = img.max()
    #Apply the formula to each pixel
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            newImg[i,j] = (img[i,j] - min) * (255/(max - min))
    return newImg

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