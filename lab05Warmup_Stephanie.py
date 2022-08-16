from PIL import Image

bear = Image.open( "bear.png" )

pixel = bear.getpixel( ( 100, 200) )
print(pixel)

# draw black line over image
bear.putpixel( (100, 200), (0, 0, 0) )
for i in range(100):
    bear.putpixel( (i, 200) , (0, 0, 0) )

bear.save("tmp_steph.png")

# invert color of image
def invert( im ):
    ''' Invert the colors in the input image, im '''
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range( width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            bear.putpixel( (x, y) , (255 - red, 255 - green, 255 - blue) )

invert(bear)
bear.save("tmp1_steph.png")

def invert_block( im ):
  (width, height) = im.size

  for x in range( int(width/2), width ):
    for y in range( int(height/2) ):
      (red, green, blue) = im.getpixel((x, y))
      bear.putpixel( (x, y) , (255 - red, 255 - green, 255 - blue) )

# inverts to normal colors
invert(bear)

# inverts only top right quadrant
invert_block(bear)
bear.save("tmp2_steph.png")
