import matplotlib.pyplot as plt

def showFig3(image1, hist1, image2, hist2, image3, hist3, image4, hist4):
  fig = plt.figure(figsize=(12, 12))

  fig.add_subplot(4, 2, 1)
  plt.imshow(image1, cmap="gray")
  plt.axis('off')
  fig.add_subplot(4, 2, 2)
  plt.plot(hist1)
  
  fig.add_subplot(4, 2, 3)
  plt.imshow(image2, cmap="gray")
  plt.axis('off')
  fig.add_subplot(4, 2, 4)
  plt.plot(hist2)
  
  fig.add_subplot(4, 2, 5)
  plt.imshow(image3, cmap="gray")
  plt.axis('off')
  fig.add_subplot(4, 2, 6)
  plt.plot(hist3)
  
  fig.add_subplot(4, 2, 7)
  plt.imshow(image4, cmap="gray")
  plt.axis('off')
  fig.add_subplot(4, 2, 8)
  plt.plot(hist4)

  plt.show()
