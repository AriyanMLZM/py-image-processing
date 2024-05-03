import cv2
import numpy as np

from convertBW import *
from convertFourier import *
from convertLog import *

image = cv2.imread("input.jpg")
resized_image = cv2.resize(image, (512, 512))

gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

bw = gray.copy()
convertBW(bw)

magnitude = convertFourier(gray)

log = magnitude.copy()
convertLog(log, 1)

cv2.imshow('Color', resized_image)
resultsImg1 = np.concatenate((gray, bw), axis=1)
resultsImg2 = np.concatenate((magnitude, log), axis=1)
cv2.imshow('results', resultsImg1)
cv2.imshow('results2', resultsImg2)

cv2.waitKey(0)
cv2.destroyAllWindows()
