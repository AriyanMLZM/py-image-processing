import cv2
import numpy as np

from convertBW import *
from convertFourier import *

image = cv2.imread("input.jpg")
resized_image = cv2.resize(image, (512, 512))

gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

bw = gray.copy()
convertBW(bw)

magnitude = convertFourier(gray)

cv2.imshow('Color', resized_image)
resultsImg = np.concatenate((gray, bw, magnitude), axis=1)
cv2.imshow('results', resultsImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
