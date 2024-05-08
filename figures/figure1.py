import matplotlib.pyplot as plt

def showFig1(image1, image2, image3, image4, image5):
  fig = plt.figure(figsize=(12, 8))
  
  fig.add_subplot(2, 3, 1)
  plt.imshow(image1)
  plt.title('color')
  
  fig.add_subplot(2, 3, 2)
  plt.imshow(image2, cmap='gray')
  plt.title('gray')
  
  fig.add_subplot(2, 3, 3)
  plt.imshow(image3, cmap='gray')
  plt.title('bw')
  
  fig.add_subplot(2, 3, 4)
  plt.imshow(image4, cmap='gray')
  plt.title('fourier transform')
  
  fig.add_subplot(2, 3, 5)
  plt.imshow(image5, cmap='gray')
  plt.title('log transform')

