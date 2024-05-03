def contrast(image):
  min = float('inf')
  max = float('-inf')
  for y in range(512): 
    for x in range(512):
      pixel_value = image[y, x]
      if(pixel_value < min): min = int(image[y, x])
      if(pixel_value > max): max = int(image[y, x])

  a = (255 - 0) / (max - min)

  print(a)
  for y in range(512): 
    for x in range(512):
      pixel_value = int(image[y, x])
      if(pixel_value <= min): image[y, x] = 0
      elif(pixel_value >= max): image[y, x] = 255
      else: image[y, x] = a * pixel_value - a * min

  