import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def bright(image,factor):
    imBright =  image.astype(np.float32)
    imBright + imBright + factor
    imBright = np.clip(imBright,0,255)
    return bright_image.astype("np.uint8")

def contrast(image, factor):
    mean = 128
    img_contrast = image.astype(np.float32)
    img_contrast = (mean + factor) * (img_contrast -mean)
    img_contrast = np.clip(img_contrast,0,255)
    return img_contrast.astype(np.uint8)

path = "C:\\Users\\Abdul\\OneDrive\\Documents\\TUGAS AMI\\PCD\\images.jpeg"
image = img.imread(path)
hist,bins = np.histogram(image.flatten(),bins=255, range=[0,255])

imgContrast = contrast(image,1.5)

plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.imshow(image)
plt.title('Sebelum Kontras')

plt.subplot(2,2,2)
plt.imshow(imgContrast)
plt.title('Sesudah Kontras')
plt.subplot(2,2,3)
plt.plot(hist)

plt.show()

