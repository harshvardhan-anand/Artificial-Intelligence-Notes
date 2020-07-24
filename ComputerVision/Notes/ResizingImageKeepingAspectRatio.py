'''
Choice of Interpolation Method for Resizing
-----------------------------------------------------------------------------------
1. cv2.INTER_AREA: This is used when we need need to shrink an image.
2. cv2.INTER_CUBIC: This is slow but more efficient.
3. cv2.INTER_LINEAR: This is primarily used when zooming is required. This is the 
                   default interpolation technique in OpenCV.
--------------------------------------------------------------------------------------
'''
# Resizing by maintaing the aspect raio

import cv2
import  matplotlib.pyplot as plt

img = cv2.imread('image_path')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def resize(image, width=None, height=None):
    (h, w) = image.shape[:2]
    
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_LINEAR)   #()
    
    return resized

img = resize(img, width=600)

plt.imshow(img)