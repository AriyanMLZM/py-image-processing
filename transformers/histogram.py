import cv2

def histogram(image):
  hist = cv2.calcHist([image], [0], None, [256], [0, 256])

  return hist
