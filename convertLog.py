import math

def convertLog(image, c):
  for y in range(512): 
    for x in range(512):
      pixel_value = image[y, x]
      image[y, x] = c * math.log(1 + pixel_value)
