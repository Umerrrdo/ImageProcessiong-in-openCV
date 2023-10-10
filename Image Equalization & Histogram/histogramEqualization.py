import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to perform histogram equalization (Manual Implementation)
def histogramEqualization(image):
    M, N = image.shape
    L = 256  # Number of intensity levels
    # Calculate the histogram of the input image
    hist = np.histogram(image.flatten(), bins=range(L+1), density=True)
    # Compute the CDF
    cdf = np.cumsum(hist[0])
    # Apply the histogram equalization transformation
    equalizedImage = np.interp(image, np.arange(L), np.floor((L - 1) * cdf))

    return equalizedImage.astype(np.uint8)

# Load and process each image
imagePaths = ['img/dark.tif', 'img/bright.tif', 'img/lowcon.tif', 'img/wiki.jpg']
imageLabels = ['Dark Image', 'Bright Image', 'Low Contrast Image', 'Wiki Image']

plt.figure(figsize=(16, 12))

for i, image_path in enumerate(imagePaths):
    # Load the image
    originalImage = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    manualEqualizedImage = histogramEqualization(originalImage)
    opencvEqualizedImage = cv2.equalizeHist(originalImage)

    # Plot histograms before and after equalization
    plt.subplot(4, 4, i * 4 + 1)
    plt.title(f'{imageLabels[i]} - Original Histogram')
    plt.hist(originalImage.flatten(), bins=256, range=(0, 256), density=True, color='blue', alpha=0.7)
    plt.subplot(4, 4, i * 4 + 2)
    plt.title(f'Manual Equalized Histogram')
    plt.hist(manualEqualizedImage.flatten(), bins=256, range=(0, 256), density=True, color='green', alpha=0.7)
    plt.subplot(4, 4, i * 4 + 3)
    plt.title(f'OpenCV Equalized Histogram')
    plt.hist(opencvEqualizedImage.flatten(), bins=256, range=(0, 256), density=True, color='red', alpha=0.7)

    # Display the images with labels
    plt.subplot(4, 4, i * 4 + 4)
    plt.title(f'Images')
    plt.imshow(np.hstack([originalImage, manualEqualizedImage, opencvEqualizedImage]), cmap='gray')
    # plt.xlabel(f'Original Image                  Manual Equalized Image              OpenCV Equalized Image')

plt.tight_layout()
plt.show()
