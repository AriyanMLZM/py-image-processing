import numpy as np

def convertLog(image):
  c = int(input("Enter c for log transform: "))
  log = c * np.log(image + 1)

  return log
