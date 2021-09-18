def isRGB(img):
    """Check if an image is colored (3 channels)
        Input: 
            image
        Output:
            Boolean
    """

    if img.shape[2] == 3:
        return True
    else:
        return False

def new_shape(img,scale):
    if scale > 1:
        scale = 1 - scale/100
    else: 
        scale = 1 - scale
    x,y = img.shape
    x = round(x*scale)
    y = round(y*scale)
    print(f'new shape is {x} per {y} pixels')
    return x,y
