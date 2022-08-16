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

mirrorHoriz(bear)                
bear.save("tmp3_bear.png")

''' Vertical Flipping '''
def flipVert(im):
  