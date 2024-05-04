import cv2
import numpy as np
import matplotlib.pyplot as plt

from convertBW import *
from convertFourier import *
from contrast import *

image = cv2.imread("input.jpg")
image = cv2.resize(image, (512, 512))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bw = gray.copy()
convertBW(bw)

magnitude = convertFourier(gray, False)
log = convertFourier(gray, True)

image2 = cv2.imread("input2.png")
image2 = cv2.resize(image2, (512, 512))
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
contrast(gray2)

fig = plt.figure(figsize=(12, 8))
fig.add_subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('color')
fig.add_subplot(2, 3, 2)
plt.imshow(gray, cmap='gray')
plt.title('gray')
fig.add_subplot(2, 3, 3)
plt.imshow(bw, cmap='gray')
plt.title('bw')
fig.add_subplot(2, 3, 4)
plt.imshow(magnitude, cmap='gray')
plt.title('fourier transform')
fig.add_subplot(2, 3, 5)
plt.imshow(log, cmap='gray')
plt.title('log transform')

fig = plt.figure(figsize=(8, 6))
fig.add_subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('gray')
fig.add_subplot(1, 2, 2)
plt.imshow(gray2, cmap='gray')
plt.title('contrast')

plt.show()
