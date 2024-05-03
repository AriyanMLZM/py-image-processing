import cv2
import numpy as np

from convertBW import *
from convertFourier import *
from convertLog import *
from contrast import *

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

image2 = cv2.imread("input2.png")
resized_image2 = cv2.resize(image2, (512, 512))
gray2 = cv2.cvtColor(resized_image2, cv2.COLOR_BGR2GRAY)
con = gray2.copy()
contrast(con)
resultsImg3 = np.concatenate((gray2, con), axis=1)
cv2.imshow('results3', resultsImg3)

cv2.waitKey(0)
cv2.destroyAllWindows()
