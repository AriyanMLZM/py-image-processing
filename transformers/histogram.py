import cv2

def histogram(image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
  
  eq = cv2.equalizeHist(gray)
  histeq = cv2.calcHist([eq], [0], None, [256], [0, 256])
  
  return [hist, eq, histeq]
