import cv2

from transformers.convertBW import *
from transformers.convertFourier import *
from transformers.convertLog import *
from transformers.contrast import *
from figures.figure1 import *
from figures.figure2 import *

image = cv2.imread("./inputs/input.jpg")
image = cv2.resize(image, (512, 512))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bw = gray.copy()
convertBW(bw)

magnitude = convertFourier(gray)
log = convertLog(magnitude)

image2 = cv2.imread("./inputs/input2.png")
image2 = cv2.resize(image2, (512, 512))
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
contrast(gray2)

showFig1(image, gray, bw, magnitude, log)
showFig2(image2, gray2)
