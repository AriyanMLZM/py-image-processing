import matplotlib.pyplot as plt

def showFig2(image1, image2):
  fig = plt.figure(figsize=(8, 6))

  fig.add_subplot(1, 2, 1)
  plt.imshow(image1)
  plt.title('gray')
  
  fig.add_subplot(1, 2, 2)
  plt.imshow(image2, cmap='gray')
  plt.title('contrast')
