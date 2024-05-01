def convertBW(bw):
  threshold = int(input("Enter the threshold value (0-255): "))
  threshold = max(0, min(255, threshold))
  for y in range(512): 
    for x in range(512):
      pixel_value = bw[y, x]
      if pixel_value < threshold:
        bw[y, x] = 0
      else:
        bw[y, x] = 255
