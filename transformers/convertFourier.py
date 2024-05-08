import cv2
import numpy as np

def convertFourier(gray, flag):
  fourier = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
  fourier_shift = np.fft.fftshift(fourier)
  magnitude = cv2.magnitude(fourier_shift[:,:,0],fourier_shift[:,:,1])
  if(flag): magnitude = 20*np.log(magnitude)
  magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

  return magnitude
