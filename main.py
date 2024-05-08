import cv2

from transformers.convertBW import *
from transformers.convertFourier import *
from transformers.convertLog import *
from transformers.contrast import *
from transformers.histogram import *
from figures.figure1 import *
from figures.figure2 import *
from figures.figure3 import *

image = cv2.imread("./inputs/input.jpg")
image = cv2.resize(image, (512, 512))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bw = gray.copy()
convertBW(bw)

magnitude = convertFourier(gray)
log = convertLog(magnitude)

lowContrast = cv2.imread("./inputs/low.png")
lowContrast = cv2.resize(lowContrast, (512, 512))
con = lowContrast.copy()
con = cv2.cvtColor(con, cv2.COLOR_BGR2GRAY)
contrast(con)

bright = cv2.imread("./inputs/bright.png")
bright = cv2.resize(bright, (512, 512))
dark = cv2.imread("./inputs/dark.png")
dark = cv2.resize(dark, (512, 512))
highContrast = cv2.imread("./inputs/high.png")
highContrast = cv2.resize(highContrast, (512, 512))

hist1 = histogram(bright)
hist2 = histogram(dark)
hist3 = histogram(lowContrast)
hist4 = histogram(highContrast)

showFig1(image, gray, bw, magnitude, log)
showFig2(lowContrast, con)
showFig3(bright, hist1, dark, hist2, lowContrast, hist3, highContrast, hist4)
