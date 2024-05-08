import cv2
import numpy as np

def convertFourier(gray):
  fourier = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
  fourier_shift = np.fft.fftshift(fourier)
  magnitude = cv2.magnitude(fourier_shift[:,:,0],fourier_shift[:,:,1])

  return magnitude
