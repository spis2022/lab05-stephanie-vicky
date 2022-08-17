# print("Running lab05Warmup_Vicky.py")
# import lab05Warmup_Vicky

# print("Running lab05Warmup_Stephanie.py")
# import lab05Warmup_Stephanie

from PIL import Image

bear = Image.open( "bear.png" )

''' Grayscale '''
def grayscale(im):
  (width, height) = im.size
  for x in range( width ):
    for y in range( height ):
      (red, green, blue) = im.getpixel((x, y))
      luminosity = (red*.21 + green*.72 + blue*.07)
      im.putpixel( (x, y) , (int(luminosity), int(luminosity), int(luminosity)) )

# grayscale(bear)                
bear.save("tmp_bear.png")

''' Binarize '''
def binarize(im, thresh, startx, starty, endx, endy):
  if startx > 0 and starty > 0 and endx < 600 and endy < 800:
    print("Box not in bounds")
  else:
    for x in range(startx, endx):
      for y in range(starty, endy):
        (red, green, blue) = im.getpixel((x, y))
        luminosity = (red*.21 + green*.72 + blue*.07)
        if luminosity > thresh:
          im.putpixel((x, y), (255, 255, 255))
        else:
          im.putpixel((x, y), (0, 0, 0))

# binarize(bear, 100, 0, 0, 400, 600)                
bear.save("tmp1_bear.png")

''' Vertical Mirroring '''
def mirrorVert(im):

  (width, height) = im.size
  
  for x in range(width):
    for y in range(int(height/2), height):
      (red, green, blue) = im.getpixel((x, height - y))
      im.putpixel((x, y), (red, green, blue))

#mirrorVert(bear)                
bear.save("tmp2_bear.png")

''' Horizontal Mirroring '''
def mirrorHoriz(im):

  (width, height) = im.size
  
  for x in range(int(width/2), width):
    for y in range(height):
      (red, green, blue) = im.getpixel((width - x, y))
      im.putpixel((x, y), (red, green, blue))

#mirrorHoriz(bear)                
bear.save("tmp3_bear.png")

''' Vertical Flipping '''
def flipVert(im):
  (width, height) = im.size

  for x in range(width):
    for y in range(int(height/2)):
      (topR, topG, topB) = im.getpixel((x, y))
      (bottomR, bottomG, bottomB) = im.getpixel((x, height - y - 1))
      im.putpixel((x, height - y - 1), (topR, topG, topB))
      im.putpixel((x, y), (bottomR, bottomG, bottomB))

# tmp4_bear = Image.open( "tmp4_bear.png" )

#flipVert(bear)
bear.save("tmp4_bear.png")

''' Scale '''
def scale(im):
  (width, height) = im.size
  scaledIm = Image.new('RGB', (int(width/2),int(height/2)))
  for x in range(0, width-1, 2):
    for y in range(0, height-1, 2):
      (red, green, blue) = im.getpixel((x, y))
      scaledIm.putpixel((int(x/2),int(y/2)), (red, green, blue))
  # print(scaledIm.size)
  return scaledIm

#scale(bear).save("tmp5_bear.png")
    

''' Blur '''
def blur(im):
  (width, height) = im.size
  blurredIm = Image.new('RGB', (width, height))
  for x in range(width-1):
    for y in range(height-1):
      (r1, g1, b1) = im.getpixel((x, y))
      (r2, g2, b2) = im.getpixel((x+1, y+1))
      avgR = (r1 +r2)/2
      avgG = (g1 + g2)/2
      avgB = (b1 + b2)/2
      blurredIm.putpixel((x,y), (int(avgR), int(avgG), int(avgB)))

  return blurredIm

#blur(bear).save("tmp6_bear.png")