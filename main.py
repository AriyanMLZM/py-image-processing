import cv2
import numpy as np

image = cv2.imread("input.jpg")
resized_image = cv2.resize(image, (512, 512))

gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

bw = gray.copy()
threshold = int(input("Enter the threshold value (0-255): "))
threshold = max(0, min(255, threshold))
for y in range(512): 
    for x in range(512):
        pixel_value = bw[y, x]
        if pixel_value < threshold:
            bw[y, x] = 0
        else:
            bw[y, x] = 255  

fourier = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
fourier_shift = np.fft.fftshift(fourier)
magnitude = 20*np.log(cv2.magnitude(fourier_shift[:,:,0],fourier_shift[:,:,1])) 
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1) 

cv2.imshow('Color', resized_image)
resultsImg = np.concatenate((gray, bw, magnitude), axis=1)
cv2.imshow('results', resultsImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
