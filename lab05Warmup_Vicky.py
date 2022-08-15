from PIL import Image
bear = Image.open( "bear.png" )

# This prints the pixel size of the image
print(bear.size)


# Basic PIL Functions
# Accessing a pixel at location (100, 200)
pixel = bear.getpixel( ( 100, 200) )
print(pixel)

# Modifying a pixel color at (100,200) to black
bear.putpixel( (100, 200), (0, 0, 0) )
bear.save("tmp_Vicky.png")


# Inverting colors
def invert(im):
    # Find the dimensions of the image
    (width, height) = im.size
    # Loop over the entire image
    for x in range( width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            im.putpixel((x,y), (255-red, 255-blue, 255-green))
invert(bear)
bear.save("tmp1_Vicky.png")
# invert again so the tmp2 will be the original image colors
invert(bear)

# Modifying part of the image
def invert_block(im):
    # for loop covers half of the width x and height y
    for x in range(300):
        for y in range(400):
            (red, green, blue) = im.getpixel((x, y))
            im.putpixel((x,y), (255-red, 255-blue, 255-green))
invert_block(bear)
bear.save("tmp2_Vicky.png")