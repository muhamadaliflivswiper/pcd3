import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def equal(image):
    hist,bins = np.histogram(image.flatten(),bins=256, range=[0,256])
    cdf = hist.cumsum()
    cdf_normal = (cdf/cdf.max) * 255
    image_equal = np.interp(image.flatten(),bins[:-1],cdf_normal)
    return img_equal.reshape(image.shape).astype(np.uint8)

path = "C:\\Users\\USE\\Downloads\\Tokyo to Chureito Pagoda train to see Mt Fuji.jpg"
image = img.imread(path)
imgEqual = equal(image)
hist,bins = np.histogram(image.flatten(),bins=256, range=[0,256])
hist_e,bins = np.histogram(imgEqual.flatten(),bins=256, range=[0,256])
plt.figure(figsize=(15,15))
plt.subplot(2,2,1)
plt.imshow(image)

plt.subplot(2,2,2)